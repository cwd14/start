from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'version1.views.home', name='home'),
    # url(r'^version1/', include('version1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^VS/register/$','videoShare.views.register'),
    url(r'^VS/login/$','videoShare.views.login'),
    url(r'^VS/submitvideo/$','videoShare.views.submitvideo'),
    url(r'^VS/watchvideo/$','videoShare.views.watchvideo'),
    url(r'^VS/changeinfo/$','videoShare.views.changeinfo'),
)
