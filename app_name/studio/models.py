from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Award(models.Model):
	award_name = models.CharField(max_length = 50)
	award_year = models.IntegerField()
	award_project = models.CharField(max_length = 100)
	award_project_url = models.URLField()

class Competition(models.Model):
	competition_name = models.CharField(max_length = 100)
	competition_result = models.CharField(max_length = 50)
	competition_year = models.IntegerField()
	competition_url = models.URLField()
	
class Publication(models.Model):
	publication_name = models.CharField(max_length = 200)
	publication_year = models.IntegerField()
	publication_url = models.URLField()