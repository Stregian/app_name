from __future__ import unicode_literals

from django.db import models
from projects.models import Project
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    article = models.TextField()
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project)
    date = models.DateTimeField(default = timezone.now)
