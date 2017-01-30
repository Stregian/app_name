#views for projects
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Project
# Create your views here.
def index(request):
	html = 'index for the projects page'
	return HttpResponse(html)
	
	
def project(request, slug):
	p = get_object_or_404(Project, slug=slug)
	
	html = p.title
	return HttpResponse(html)