from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html = 'the landing page for the site'
	return HttpResponse(html)