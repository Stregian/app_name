"""app_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    

	   url(r'^studio/awards/$', views.awards, name='awards'),
    url(r'^studio/competitions/$', views.competitions, name='competitions' ),
    url(r'^studio/publications/$', views.publications, name='publications'),
   	url(r'^studio/', views.studio_index, name ='studio_index'),
    
	   url(r'^projects/$', views.project_index, name = 'project_index'),
    url(r'^projects/(?P<slug>[-\w]+)/$', views.project, name = 'project'),
    
	   url(r'^people/$', views.people_index, name = 'people_index'),
	   url(r'^people/(?P<slug>[-\w]+)/$', views.person, name = 'person'),
	
    url(r'^$',views.index, name = 'index'),
    url(r'^contact$', views.contact, name ='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
