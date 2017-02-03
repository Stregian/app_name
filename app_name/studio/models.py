from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from django.db import models
from projects.models import Project
import time
import os
from django.template.defaultfilters import slugify
from django.utils import timezone
from general.general import file_path, get_year_list
# Create your models here.


def file_path(instance, filename):
    filename = os.path.splitext(filename)
    name = instance.title
    extension = filename[1]
    timestamp = str(time.time())
    filename = slugify(name+'-'+timestamp[-6:]) + extension
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['pdfs', filename])


class Award(models.Model):
    project = models.ForeignKey(Project, null = True)
    title = models.CharField(max_length = 50)
    year = models.IntegerField(choices = get_year_list(1990,5), default = timezone.now().year)
    slug = AutoSlugField(populate_from=('project'), unique=True, max_length=100,editable=True)  
    date = models.DateField(default = timezone.now)
    
    def __unicode__(self):
         
        return self.title


class Competition(models.Model):
    title = models.CharField(max_length = 100)
    result = models.CharField(max_length = 50)
    year = models.IntegerField(choices = get_year_list(1990,5), default = timezone.now().year)
    project = models.ForeignKey(Project, null = True)
    slug = AutoSlugField(populate_from=('project'), unique=True, max_length=100,editable=True)  
    date = models.DateField(default = timezone.now)
  
    def __unicode__(self):
        return self.title  


class Publication(models.Model):
    title = models.CharField(max_length = 200)
    year = models.IntegerField(choices = get_year_list(1990,5), default = timezone.now().year)
    pdf = models.FileField(upload_to = file_path)
    slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
    date = models.DateField(default = timezone.now)
    journal = models.CharField(max_length = 50, blank=True)
  
    def __unicode__(self):
        return self.title
