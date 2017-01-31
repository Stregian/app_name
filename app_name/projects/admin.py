from django.contrib import admin
from projects.models import Project, Image, Category


class ImageInline(admin.TabularInline):
    max_num = 1
    extra = 1
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)