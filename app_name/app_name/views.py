from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from projects.models import Project, Image
from projects.models import Category as ProjectCategory
from news.models import Article 
from people.models import Staff
from people.models import Category as StaffCategory
from studio.models import Award, Publication, Competition



def index(request):
    image = get_object_or_404(Image,id = 5)
    context = {'image':image}
    return render(request, 'base_index.html', context)

def contact(request):
    return render(request,'contact.html')
	

def people_index(request):
    staff_list = Staff.objects.order_by('slug')
    context ={'staff_list': staff_list} 
    return render(request, 'people_index.html', context)

	
def person(request, slug):
    person = get_object_or_404(Staff, slug=slug)
    context = {'person':person}
    return render(request, 'people.html',context)
	

def studio_index(request):
    image = get_object_or_404(Image,id = 5)
    news = Article.objects.order_by('date').reverse()[0:2]
    context = {'image':image, 'news':news}
    return render (request,'studio.html',context)
	
def awards(request):
    awards_list = Award.objects.order_by('year')
    context ={'awards_list': awards_list} 
    return render(request, 'awards.html', context)
	
def competitions(request):
    competition_list = Competition.objects.order_by('year')
    context ={'competition_list': competition_list} 
    return render(request, 'competitions.html', context)
	
def publications(request):
    publication_list = Publication.objects.order_by('year')
    context ={'publication_list': publication_list} 
    return render(request, 'publications.html', context)

def pdf_return(request,slug):
    pdf = get_object_or_404(Publication, slug=slug)
    pdf_data = pdf.pdf.read()
    return HttpResponse(pdf_data, content_type='application/pdf')

def project_index(request):
    project_list = Project.objects.order_by('date')
    context ={'project_list': project_list} 
    return render(request, 'project_index.html', context)
	
def project(request, slug):
    project = get_object_or_404(Project, slug=slug)

    for image in project.related_image.all():
        print image

    context = {'project':project}
    return render(request, 'project.html', context)

