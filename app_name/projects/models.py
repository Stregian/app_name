from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import AutoSlugField
from sorl.thumbnail import ImageField
import time
import datetime
import os
from django.template.defaultfilters import slugify

# Create your models here.

def image_path(instance, filename):
    filename = os.path.splitext(filename)
    name = filename[0].replace("_", "-")
    extension = filename[1]
    timestamp = str(time.time())
    #filename = slugify(name+'-'+timestamp[-6:]) + extension
    project = instance.fk.slug
    filename = slugify(project+'-'+timestamp[-6:]) + extension # prints the filename as the project + extesion. 
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['uploads', filepath, filename])


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
    slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
    categories = models.ManyToManyField(Category)
    date = models.DateField(default = datetime.datetime.now())
    def __unicode__(self):
        return self.title
		

class Image(models.Model):
    fk = models.ForeignKey(Project, related_name='related_image')
	#number = models.IntegerField(default = 0)
    image = ImageField(upload_to=image_path)
	#thumbnail = ImageField(upload_to= 'projects/', null = True)
	#description = models.TextField(blank = True)
	
    def __unicode__(self):
        return os.path.basename(self.image.name)
	#def save(self):
