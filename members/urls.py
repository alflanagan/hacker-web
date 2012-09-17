from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('goals.views',
    url(r'^$', 'index'),
)
