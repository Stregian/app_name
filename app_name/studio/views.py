from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from models import Award, Competition, Publication

def index(request):
	html = 'this is an index page for the studio'
	return HttpResponse(html)

def awards(request):
	html = 'awards page'
	return HttpResponse(html)

def competitions(request):
	html = 'competitions page'
	return HttpResponse(html)

def publications(request):
	html = 'publications page'
	return HttpResponse(html)

