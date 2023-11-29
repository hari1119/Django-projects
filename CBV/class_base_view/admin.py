from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]
    search_fields = ['first_name','last_name']
    

admin.site.register(Employee,EmployeeAdmin) # Employee is registered 
