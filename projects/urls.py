# pylint: disable=missing-docstring
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<proj_id>\d+)/$', views.project_detail, name='project_detail'),
    url(r'(?P<proj_id>\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'(?P<proj_id>\d+)/delete/$', views.project_delete, name='project_delete'),
    url(r'new/$', views.project_create, name='project_create'),
    url(r'saved/$', views.project_saved, name='project_saved'),
]
