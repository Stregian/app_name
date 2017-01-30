# views for people 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	html = 'index page for people'