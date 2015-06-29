from django.conf.urls import url

from . import views

urlpatterns = [
    # Basic project list and record list
    url(r'^$',
        views.ProjectListView.as_view(), name='index'),
    url(r'^project/(?P<pk>[0-9]+)/$',
        views.ProjectDetailView.as_view(), name='project'),
    # User auth
    url(r'^accounts/login/$',
        views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$',
        views.LogoutView.as_view(), name='logout'),
    # Project model add/update/delete
    url(r'project/add/$',
        views.ProjectCreateView.as_view(), name='project_add'),
    url(r'project/(?P<pk>[0-9]+)/update/$',
        views.ProjectUpdateView.as_view(), name='project_update'),
    url(r'project/(?P<pk>[0-9]+)/delete/$',
        views.ProjectDeleteView.as_view(), name='project_delete'),
    # Record model add/update/delete
    url(r'record/add/$',
        views.RecordCreateView.as_view(), name='record_add'),
    url(r'record/(?P<pk>[0-9]+)/$',
        views.RecordUpdateView.as_view(), name='record_update'),
    url(r'record/(?P<pk>[0-9]+)/delete/$',
        views.RecordDeleteView.as_view(), name='record_delete'),
]
