#views for projects
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Project

# Create your views here.
def index(request):
    project_list = Project.objects.order_by('slug')
    context ={'project_list': project_list} 
    return render(request, 'projects/index.html', context)
	
def project(request, slug):
	p = get_object_or_404(Project, slug=slug)
	
	html = p.title
	return HttpResponse(html)
