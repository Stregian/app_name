from django.contrib import admin
from models import Award, Competition, Publication
# Register your models here.

class CompetitionAdmin(admin.ModelAdmin):
	list_filter = ('result',)
	pass

admin.site.register(Award)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Publication)