# General models.py 

from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=50, default = '')

	
	class Meta:
		abstract = True
		verbose_name_plural = 'Categories'
	
	def __unicode__(self):
		return self.title