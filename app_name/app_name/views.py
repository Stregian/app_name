from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html = 'the landing page for the site'
	return HttpResponse(html)

def contact(request):
	html = 'contact page'
	return HttpResponse(html)
	
	
	
def studio_index(request):
	return ''
	
def awards(request):
	return ''
	
def competitions(request):
	return ''
	
def publications(request):
	return ''



def project_index(request):
	return ''
	
def project(request):
	return ''



def people_index(request):
	return ''
	
def person(request):
	return ''
