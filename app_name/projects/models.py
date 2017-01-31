from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import AutoSlugField
from sorl.thumbnail import ImageField
import os
# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=50)
	
	class Meta:
		verbose_name_plural = "Categories"
	
	def __unicode__(self):
		return self.category	


class Project(models.Model):
	title = models.CharField(max_length=100, help_text="The name of this project")
	location = models.CharField(max_length=50, default="")
	information = models.TextField()
	year = models.IntegerField()
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	categories = models.ManyToManyField(Category)
	
	def __unicode__(self):
		return self.title
		

class Image(models.Model):
	project = models.ForeignKey(Project, related_name='related_image')
	number = models.IntegerField(default = 0)
	image = ImageField(upload_to= 'projects/')
	thumbnail = ImageField(upload_to= 'projects/', null = True)
	description = models.TextField(blank = True)
	
	def __unicode__(self):
		return os.path.basename(self.image.name)