from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField
import time
import os
from django.template.defaultfilters import slugify
from general.models import Category
from django_extensions.db.fields import AutoSlugField


def image_path(instance, filename):
    filename = os.path.splitext(filename)
    name = filename[0].replace("_", "-")
    extension = filename[1]
    timestamp = str(time.time())
    filename = slugify(name+'-'+timestamp[-6:]) + extension
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['uploads', filepath, filename])
   
    
	
class Category(Category):
    fk = models.ForeignKey('people.Staff', related_name='related_category', null=True)

	
	
class Staff(models.Model):
	name = models.CharField(max_length=255)
	slug = AutoSlugField(populate_from=('name'), unique=True, max_length=100,editable=True)
	category = models.ManyToManyField('people.Category', blank = True)
	profile = ImageField(upload_to = image_path)
	description = models.TextField(blank = True, default='')
	
	def __unicode__(self):
		return self.name
	class Meta:	
		verbose_name_plural = "Staff"