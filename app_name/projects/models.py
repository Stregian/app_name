from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import AutoSlugField
# Create your models here.
class Project(models.Model):
	
	title = models.CharField(max_length = 100)
	year = models.IntegerField()
	slug = AutoSlugField(populate_from=('title'), unique=True, max_length=100,editable=True)  
	categories = models.CharField(max_length = 50)
	def __str__(self):
		return self.title