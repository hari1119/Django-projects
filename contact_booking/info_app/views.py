from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse  
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from .models import EmployeeDetail
from contact_booking.settings import SUCCESS_URL
from django.forms.models import model_to_dict

class EmployeeList(LoginRequiredMixin, ListView):
    template_name = 'contact_list.html'
    model = EmployeeDetail
    context_object_name = 'Employee_list_obj'


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = EmployeeDetail
    success_url = SUCCESS_URL

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            employee = EmployeeDetail(
                first_name=request.POST.get('first-name'),
                last_name=request.POST.get('last-name'),
                email=request.POST.get('email-address'),
                mobile_number=request.POST.get('phone-number'),
                date_of_birth=request.POST.get('dob'),
                blood_group=request.POST.get('blood_group'),
                gender=request.POST.get('gender'),
                whatsapp_number=request.POST.get('whatsapp-phone-number') if request.POST.get('whatapp_no') == 'no' else request.POST.get('phone-number'),
                address_line_1=request.POST.get('address'),
                address_line_2=request.POST.get('address-2'),
                city=request.POST.get('address-city'),
                state=request.POST.get('address-state'),
                postal_code=request.POST.get('address-zip'),
                father_name=request.POST.get('father_name'),
                mother_name=request.POST.get('mother_name'),
                martial_statue=request.POST.get('martial'),
                wife_name=request.POST.get('wife_name') if request.POST.get('martial') == 'married' else None,
                language=request.POST.getlist('language'),
                sports=request.POST.getlist('sports'),
                hobby=request.POST.get('hobby'),
                current_company=request.POST.get('current_company'),
                current_company_location=request.POST.get('current_company_location'),
                previous_company=request.POST.get('previous_company') if request.POST.get('previous_cmpy') == 'yes' else None,
                previous_company_location=request.POST.get('previous_company_location') if request.POST.get('previous_cmpy') == 'yes' else None,
                designation=request.POST.get('designation'),
                year_of_experience=request.POST.get('experience')
            )
            employee.save()
            return redirect(self.success_url)

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = EmployeeDetail
    

class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = EmployeeDetail
    success_url = SUCCESS_URL

    def get(self, request, *args, **kwargs):
        emp_id  = kwargs.get('pk')
        delete_one_obj = EmployeeDetail.objects.get(id=emp_id)
        delete_one_obj.delete()
        return redirect(self.success_url)

class EmployeeDetails(LoginRequiredMixin, DetailView):    
    model = EmployeeDetail
    # success_url = SUCCESS_URL

    def get(self, request, *args, **kwargs):

        emp_id  = kwargs.get('pk')
        
        detail_one_obj = EmployeeDetail.objects.get(id=emp_id)
        view_data = model_to_dict(detail_one_obj)

        view_data

        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if request.method == 'GET':
                return JsonResponse(view_data)
            else:
                return JsonResponse({'status': 'Invalid request'}, status=400)


    
    

    