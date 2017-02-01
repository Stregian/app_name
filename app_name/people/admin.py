from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from models import Staff, Category

class StaffAdmin(AdminImageMixin, admin.ModelAdmin):
    
    pass
    
admin.site.register(Staff, StaffAdmin)
admin.site.register(Category)