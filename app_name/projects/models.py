from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length = 100)
	project_year = models.IntegerField()
	#project_gallery = models.URLField()
	project_categories = models.CharField(max_length = 50)