from django.contrib import admin

# Register your models here.

from .models import EmployeeDetail

class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    fields = ['first_name', 'last_name', 'email'] 
    list_filter = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['first_name'] 
    list_per_page = 10

admin.site.register(EmployeeDetail, EmployeeDetailAdmin)