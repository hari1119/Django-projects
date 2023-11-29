from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

app_name = 'info_data'

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='home_page'),

    path('create_record/', login_required(TemplateView.as_view(template_name='create_contact.html')), name='create_record'),
    
    path('employee_create/', views.EmployeeCreate.as_view(), name='employee_create'),

    path('employee/<int:pk>/update', views.EmployeeUpdate.as_view(), name='employee_update'),

    path('employee/<int:pk>/delete', views.EmployeeDelete.as_view(), name='employee_delete'),

    path('employee/<int:pk>/detail', views.EmployeeDetails.as_view(), name='employee_details'),

]