from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$', include('members.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^notifications/', include('notification.urls')),
)
