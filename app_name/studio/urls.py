#urls.py for studio 
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^awards/$', views.awards, name='awards'),
    url(r'^competitions/$', views.competitions, name='competitions' ),
    url(r'^publications/$', views.publications, name = 'publications'),
]
