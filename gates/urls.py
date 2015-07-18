from django.conf.urls import url

from . import views

urlpatterns = [
    # Basic group list and record list
    url(r'^$',
        views.GroupListView.as_view(), name='index'),
    url(r'^group/(?P<pk>[0-9]+)/$',
        views.GroupDetailView.as_view(), name='group'),

    # User auth
    url(r'^accounts/login/$',
        views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$',
        views.LogoutView.as_view(), name='logout'),

    # Group model add/update/delete
    # @yq0283: Change group add url to 'create',
    #          otherwise will cause abnormal behavior in admin-end
    url(r'group/create/$',
        views.GroupCreateView.as_view(), name='group_add'),
    url(r'group/(?P<pk>[0-9]+)/update/$',
        views.GroupUpdateView.as_view(), name='group_update'),
    url(r'group/(?P<pk>[0-9]+)/delete/$',
        views.GroupDeleteView.as_view(), name='group_delete'),

    # Record model add/update/delete
    url(r'group/(?P<pid>[0-9]+)/record/add/$',
        views.RecordCreateView, name='record_add'),
    url(r'group/(?P<pid>[0-9]+)/record/(?P<pk>[0-9]+)/$',
        views.RecordUpdateView.as_view(), name='record_update'),
    url(r'group/(?P<pid>[0-9]+)/record/(?P<pk>[0-9]+)/delete/$',
        views.RecordDeleteView.as_view(), name='record_delete'),
]
