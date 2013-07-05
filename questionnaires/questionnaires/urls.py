from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('utils.urls')),
    url(r'^backend/', include('backend.urls')),
    url(r'^', include('render.urls')),
)
