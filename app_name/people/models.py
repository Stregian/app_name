from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField
import time
import os
from django.template.defaultfilters import slugify

def image_path(instance, filename):
    filename = os.path.splitext(filename)
    name = filename[0].replace("_", "-")
    extension = filename[1]
    timestamp = str(time.time())
    filename = slugify(name+'-'+timestamp[-6:]) + extension
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['uploads', filepath, filename])
    
    
	
class Category(models.Model):
	category = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.category
	class Meta:
		verbose_name_plural = "Categories"
	
	
class Staff(models.Model):
	name = models.CharField(max_length=255)
	category = models.ManyToManyField(Category)
	profile = ImageField(upload_to = image_path)
	description = models.TextField(null = True)
	
	def __unicode__(self):
		return self.name
	class Meta:	
		verbose_name_plural = "Staff"