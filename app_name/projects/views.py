#views for projects
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	html = 'index for the projects page'
	return HttpResponse(html)
	