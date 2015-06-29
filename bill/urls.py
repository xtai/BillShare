from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('gates.urls', namespace="gates")),
    url(r'^admin/', include(admin.site.urls)),
]
