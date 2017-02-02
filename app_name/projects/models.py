from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import AutoSlugField
from sorl.thumbnail import ImageField
import time
import os
from django.template.defaultfilters import slugify
from general.models import Category
from general.general import get_year_list, file_path
from django.utils import timezone

# Create your models here.
YEAR_CHOICES = []
for y in range(1990,timezone.now().year + 5):
    YEAR_CHOICES.append((y,y))

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


class Project(models.Model):
    title = models.CharField(max_length=100, help_text="The name of this project")
    location = models.CharField(max_length=50, default="")
    information = models.TextField()
    slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
    categories = models.ManyToManyField('projects.Category', blank = True)
    date = models.DateField(default = timezone.now)
    year = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)
    def __unicode__(self):
        return self.title
        

class Image(models.Model):
    fk = models.ForeignKey('projects.Project', related_name='related_image')
    image = ImageField(upload_to=image_path)
    def __unicode__(self):
        return os.path.basename(self.image.name)


class Category(Category):
    pass
    #fk = models.ForeignKey('projects.Project', related_name='related_category', null = True)Z