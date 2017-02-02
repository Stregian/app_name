#views for projects
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Project, Image

# Create your views here.
def index(request):
    project_list = Project.objects.order_by('slug')
    context ={'project_list': project_list} 
    return render(request, 'projects/project_index.html', context)
	
def project(request, slug):
   	project = get_object_or_404(Project, slug=slug)

	   for image in project.related_image.all():
	      	print image
	
	   context = {'project':project}
	   return render(request, 'projects/project.html', context)
