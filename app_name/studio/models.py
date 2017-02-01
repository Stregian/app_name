from __future__ import unicode_literals
from django_extensions.db.fields import AutoSlugField
from django.db import models
from projects.models import Project
# Create your models here.


class Award(models.Model):
	title = models.CharField(max_length = 50)
	year = models.IntegerField()
	project = models.ForeignKey(Project)
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	
	def __unicode__(self):
		return self.title

class Competition(models.Model):
	title = models.CharField(max_length = 100)
	result = models.CharField(max_length = 50)
	year = models.IntegerField()
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	
	def __unicode__(self):
		return self.title	
	
class Publication(models.Model):
	title = models.CharField(max_length = 200)
	year = models.IntegerField()
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	
	def __unicode__(self):
		return self.title
