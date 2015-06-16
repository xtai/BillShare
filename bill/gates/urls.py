from django.conf.urls import patterns, url
from gates import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.signin),
)
