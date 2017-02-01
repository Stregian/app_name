from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from django.db import models
from projects.models import Project
import time
import os
from django.template.defaultfilters import slugify
import datetime
# Create your models here.


def file_path(instance, filename):
    filename = os.path.splitext(filename)
    name = filename[0].replace("_", "-")
    extension = filename[1]
    timestamp = str(time.time())
    filename = slugify(name+'-'+timestamp[-6:]) + extension
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['uploads', filepath, filename])

class Award(models.Model):
	project = models.ForeignKey(Project, null = True)
	title = models.CharField(max_length = 50)
	#year = models.IntegerField()
	slug = AutoSlugField(populate_from=('project'), unique=True, max_length=100,editable=True)  
	date = models.DateField(default = datetime.datetime.now())
	
	
	def __unicode__(self):
		return self.title

class Competition(models.Model):
	title = models.CharField(max_length = 100)
	result = models.CharField(max_length = 50)
	#year = models.IntegerField()
	project = models.ForeignKey(Project, null = True)
	slug = AutoSlugField(populate_from=('project'), unique=True, max_length=100,editable=True)  
	date = models.DateField(default = datetime.datetime.now())
	
	def __unicode__(self):
		return self.title	
	
class Publication(models.Model):
	title = models.CharField(max_length = 200)
	#year = models.IntegerField()
	pdf = models.FileField(upload_to = file_path)
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	date = models.DateField(default = datetime.datetime.now())

	
	def __unicode__(self):
		return self.title
