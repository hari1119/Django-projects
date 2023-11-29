from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EducationDetail, PlacementCompany
from .forms import EducationDetailForm
# Register your models here.


# class ChildModelInline(admin.TabularInline):
#     model = EducationDetail
#     extra = 1


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile'] # DISPLAY FIELDS IN MENU
    # fields = ['username', 'email', 'mobile']     # DISPLAY FIELDS IN CREATE
    list_filter = ['username', 'email']            # DISPLAY FIELDS IN FILTER SIDE    
    search_fields = ['username', 'email']          # SEARCH FIELDS IN MENU TOP 
    # ordering = ['username']                      # SORTING COLUMN IN MENU
    # list_per_page = 2                            # PAGINATE DATA
    # readonly_fields = ['username']               # READONLY FIELDS IN CREATE
    # exclude = ['first_name']                     # HIDE FIELDS IN CREATE
    # inlines = [ChildModelInline]                 # INHERITE CHILD MODEL IN PARENT MODEL (CRUD)
    # fieldsets = (                                # CREATE HEADING FOR FIELDS & HIDE AND SHOW
    #     ('General', {
    #         'fields': ('username', 'email')
    #     }),
    #     ('Contact', {
    #         'fields': ('mobile',),
    #         'classes': ('collapse',)
    #     })
    # )
    # form = ''
    # date_hierarchy = ''
    # actions = ''
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EducationDetail)
admin.site.register(PlacementCompany)