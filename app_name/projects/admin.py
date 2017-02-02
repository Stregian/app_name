from django.contrib import admin
from projects.models import Project, Image, Category
from sorl.thumbnail.admin import AdminImageMixin

class ImageInline(AdminImageMixin, admin.TabularInline):
    extra = 1
    model = Image

class ProjectAdmin(admin.ModelAdmin):
	list_filter = ('categories','location')
	inlines = [ImageInline]

   

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)