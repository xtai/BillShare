from django.contrib.auth import authenticate, decorators, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import generic

# from django.contrib.auth.models import User
from .models import Group, Record


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
        record_set = context['group'].record_set.order_by('-creation_date')
        context['record_set'] = record_set
        return context

    def get(self, *args, **kwargs):
        object = super(GroupDetailView, self).get_object()
        if self.request.user in object.members.all():
            # only visiable to mebmers within the group
            return super(GroupDetailView, self).get(self, *args, **kwargs)
        else:
            # throw forbidden for non-member
            raise Http404()


class GroupCreateView(generic.edit.CreateView):
    model = Group
    fields = ['name', 'desc']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        r = super(GroupCreateView, self).form_valid(form)
        self.object.members.add(self.request.user)
        return r


class GroupUpdateView(generic.edit.UpdateView):
    model = Group
    fields = ['name', 'desc']
    template_name_suffix = '_update_form'


class GroupDeleteView(generic.edit.DeleteView):
    model = Group
    success_url = reverse_lazy('gates:index')


class RecordCreateView(generic.edit.CreateView):
    model = Record
    fields = ['name', 'amount', 'note',
              'payer', 'receiver']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        pid = self.kwargs['pid']
        form.instance.group = self.request.user.group_set.get(pk=pid)
        self.success_url = '/group/' + str(pid)
        return super(RecordCreateView, self).form_valid(form)


class RecordUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Record
    fields = ['name', 'amount', 'note',
              'payer', 'receiver']
    template_name_suffix = '_update_form'

    def get(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(RecordUpdateView, self).get(self, *args, **kwargs)
        else:
            raise Http404()

    def post(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(RecordUpdateView, self).post(self, *args, **kwargs)
        else:
            raise Http404()

    def form_valid(self, form):
        self.success_url = '/group/' + str(form.instance.group.pk)
        return super(RecordUpdateView, self).form_valid(form)


class RecordDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Record

    def get(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            return super(RecordDeleteView, self).get(self, *args, **kwargs)
        else:
            raise Http404()

    def post(self, *args, **kwargs):
        # check if the record belongs to the group
        # throw forbidden otherwise
        if self.kwargs['pid'] == str(self.get_object().group.pk):
            self.success_url = '/group/' + str(self.kwargs['pid'])
            return super(RecordDeleteView, self).post(self, *args, **kwargs)
        else:
            raise Http404()
