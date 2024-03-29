from django.contrib.auth import authenticate, decorators, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect, render, render_to_response
from django.views import generic
from django.template import RequestContext

# from django.contrib.auth.models import User
from .models import Group, Cost, CostDetail, Balance
from .forms import *
from django.contrib.auth.forms import UserCreationForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return decorators.login_required(view)


class LoginView(generic.View):
    template_name = 'gates/login.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            context = {}
            if 'next' in request.GET:
                context = {'next': request.GET['next']}
            return render(request, self.template_name, context)
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            next_url = request.POST['next']
            if next_url == '':
                next_url = '/'
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next_url)
                else:
                    context = {
                        'error_message': "Your account has been disabled.",
                        'next': next_url
                    }
            else:
                context = {
                    'error_message': "Invalid login.",
                    'next': next_url
                }
            return render(request, 'gates/login.html', context)
        else:
            return redirect('/')


class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
        return redirect('/accounts/login/')


class GroupListView(LoginRequiredMixin, generic.ListView):
    template_name = 'gates/index.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """
        Only display current logged in user's groups
        """
        return self.request.user.group_set.order_by('-creation_date')


class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Group
    template_name = 'gates/group.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        # newer record at first
        cost_set = context['group'].cost_set.order_by('-creation_date')
        context['cost_set'] = cost_set
        return context

    def get(self, *args, **kwargs):
        object = super(GroupDetailView, self).get_object()
        if self.request.user in object.members.all():
            # only visiable to mebmers within the group
            return super(GroupDetailView, self).get(self, *args, **kwargs)
        else:
            # throw forbidden for non-member
            raise Http404()


class GroupCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Group
    fields = Group.get_form_fields()
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        r = super(GroupCreateView, self).form_valid(form)
        self.object.members.add(self.request.user)
        return r


class GroupUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Group
    fields = Group.get_form_fields()
    template_name_suffix = '_update_form'


class GroupDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Group
    success_url = reverse_lazy('gates:index')


# class RecordCreateView(LoginRequiredMixin, generic.edit.CreateView):
#     model = Record
#     fields = Record.get_form_fields()
#     template_name_suffix = '_create_form'
#
#     def form_valid(self, form):
#         pid = self.kwargs['pid']
#         form.instance.group = self.request.user.group_set.get(pk=pid)
#         self.success_url = reverse_lazy('gates:group', kwargs={'pk': pid})
#         return super(RecordCreateView, self).form_valid(form)


def CostCreateView(request, pid):
    cost_form = CostForm(request.POST or None)
    CostDetailFormSet = formset_factory(CostDetailForm, extra=2, max_num=2)
    if request.POST and cost_form.is_valid():
        record = cost_form.save(commit=False)
        costdetail_formset = CostDetailFormSet(request.POST)
        if costdetail_formset.is_valid():
            record.save()
            costdetail_formset.save()
            return reverse_lazy('gates:group', kwargs={'pk': pid})
    else:
        costdetail_formset = CostDetailFormSet(request.POST or None)
    for c in costdetail_formset:
        print c

    return render_to_response(
        'gates/record_create_form.html',
        {
            'cost_form': cost_form,
            'costdetail_formset': costdetail_formset,
        },
        context_instance=RequestContext(request),
    )


class CostUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Cost
    fields = Cost.get_form_fields()
    template_name_suffix = '_update_form'

    def get(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(CostUpdateView, self).get(self, *args, **kwargs)
        else:
            raise Http404()

    def post(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(CostUpdateView, self).post(self, *args, **kwargs)
        else:
            raise Http404()

    def form_valid(self, form):
        groupID = self.get_object().group.pk
        self.success_url = reverse_lazy('gates:group', kwargs={'pk': groupID})
        return super(CostUpdateView, self).form_valid(form)


class CostDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Cost

    def get(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(CostDeleteView, self).get(self, *args, **kwargs)
        else:
            raise Http404()

    def post(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        groupID = self.get_object().group.pk
        if self.kwargs['pid'] == str(groupID):
            self.success_url = reverse_lazy(
                'gates:group', kwargs={'pk': groupID})
            return super(CostDeleteView, self).post(self, *args, **kwargs)
        else:
            raise Http404()
