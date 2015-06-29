from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^project/(?P<pk>[0-9]+)/$',
        views.ProjectView.as_view(), name='project'),
]
