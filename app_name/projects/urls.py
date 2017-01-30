#urls for projects
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<slug>[-\w]+)/$', views.project, name = 'project')
]