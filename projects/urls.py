from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'(?P<proj_id>\d+)/$', 'project_detail'),
    url(r'(?P<proj_id>\d+)/edit/$', 'project_edit'),
    url(r'(?P<proj_id>\d+)/delete/$', 'project_delete'),
    url(r'new/$', 'project_create'),
    url(r'saved/$', 'project_saved'),
)
