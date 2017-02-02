# some useful general tools
import time
import os
from django.template.defaultfilters import slugify
from django.utils import timezone

def file_path(instance, filename):
    filename = os.path.splitext(filename)
    name = filename[0].replace("_", "-")
    extension = filename[1]
    timestamp = str(time.time())
    filename = slugify(name+'-'+timestamp[-6:]) + extension
    filepath = slugify( instance._meta.app_label.lower()) +'/'+ slugify(instance.__class__.__name__.lower())
    return '/'.join(['uploads', filepath, filename])
    
def get_year_list(start, future):
	print 'Generating year choices'
	YEAR_CHOICES = []
	for y in range(start,timezone.now().year+future):
		YEAR_CHOICES.append((y,y))
	return YEAR_CHOICES