from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# from django.contrib.auth.models import User
from .models import Project, Record


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class ProjectListView(LoginRequiredMixin, generic.ListView):
    template_name = 'gates/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """
        Only display current logged in user's projects
        """
        return self.request.user.project_set.order_by('-creation_date')


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'gates/project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        # newer record at first
        record_set = context['project'].record_set.order_by('-creation_date')
        context['record_set'] = record_set
        return context

    def get(self, request, *args, **kwargs):
        object = super(ProjectDetailView, self).get_object()
        if self.request.user in object.members.all():
            # only visiable to mebmers within the project
            return super(ProjectDetailView, self).get(self, **kwargs)
        else:
            # throw 404 for non-member
            raise Http404()


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


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'desc', 'members', 'creation_date']
    template_name_suffix = '_create_form'


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'desc', 'members', 'creation_date']
    template_name_suffix = '_update_form'


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')


class RecordCreateView(CreateView):
    model = Record
    fields = ['group', 'name', 'amount', 'note',
              'payer', 'receiver', 'creation_date']
    template_name_suffix = '_create_form'


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['group', 'name', 'amount', 'note',
              'payer', 'receiver', 'creation_date']
    template_name_suffix = '_update_form'


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('record-list')
