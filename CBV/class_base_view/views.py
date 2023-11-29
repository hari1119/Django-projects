from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .serializers import EmployeeSerializer  
from .models import Employee
import requests
from .forms import EmpForm


class NewView(View):
    about = 'Hello Jack'

    def get(self, request):
        # View logic will place here
        return HttpResponse(self.about)


class EmployeeCreate(CreateView):
    
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('response')
    # success_url = 'retrieve/'
    # form_class =EmpForm

    # another_method to show form ########
    # stu = EmpForm()
    # def get(self, request):
    #     return render(request,"class_base_view/emp_form.html",{'form':self.stu})


class EmployeeRetrieve(ListView):
    model = Employee
    template_name = 'class_base_view/employee_list.html' # html file to display the list of contacts
    
    context_object_name = 'contacts'


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmpForm
    success_url = '/'


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/'



class EmployeeNote(APIView):  
    def post(self,request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        mobile = request.data['mobile']
        email = request.data['email']

        # emp = Employee.objects.create(first_name=first_name, last_name=last_name, mobile=mobile, email=email)
        Employee(first_name = first_name,last_name = last_name,mobile = mobile,email = email).save()
             
        return Response(data={'Success':'Success'}, status=status.HTTP_200_OK)

    def get(self,request):

        emp = Employee.objects.filter(is_active = True)
        emp_data = EmployeeSerializer(emp, many=True).data
        return Response(data={'sonsnsns':'ssdsadasdas'}, status=status.HTTP_200_OK)
    
    def put(self,request):

        update = Employee.objects.get(id=request.data['id'])
        update.first_name = request.data['first_name']
        update.last_name = request.data['last_name']
        update.mobile = request.data['mobile']
        update.email = request.data['email']
        update.save()

        emp_data = EmployeeSerializer(instance=update, many=False).data
        return Response(data=emp_data, status=status.HTTP_200_OK)

    def delete(self,request):

        delete = Employee.objects.get(id=request.data['id'])
        # method 1 
        
        # delete.is_active = False
        # delete.save()

        # method 2
        delete.delete()

        return Response(data= {'done':'Success'}, status=status.HTTP_200_OK)


# def index(request):
#     if request.method == "POST":
#         form = EmpForm(request.POST)
#         if form.is_valid():

#             store = Employee(first_name = form.cleaned_data['first_name'],
#                             last_name = form.cleaned_data['last_name'],
#                             mobile = form.cleaned_data['mobile'],
#                             email = form.cleaned_data['email'])
#             store.save()

#             try:
#                 data = Employee.objects.all().values()

#                 data_condition = Employee.objects.values_list('first_name', 'last_name')

#                 data_row = Employee.objects.filter(first_name='Praba').values()

#                 data_row_and = Employee.objects.filter(first_name='Praba', last_name='SPARROW').values()

#                 data_row_or = Employee.objects.filter(first_name='Praba').values() | Employee.objects.filter(last_name='Karan').values()

#                 data_row_like = Employee.objects.filter(last_name__startswith='SPA').values()

#                 data_row_like_2 = Employee.objects.filter(last_name__istartswith='spa').values()

#                 data_row_range = Employee.objects.filter(id__range=('2','4' )).values()

#                 data_row_in = Employee.objects.filter(id__in=['2','4', '20','40']).values()

#                 data_delete = Employee.objects.filter(first_name='padas').delete()

#                 select_specific = Employee.objects.get(id='2')

#                 print(data)
#                 print(data_condition)
#                 return HttpResponse(data_row)
#             except:
#                 pass
#     else:
#         form = EmpForm()
#     return render(request,'emp_form.html',{'form':form})

# Create your views here.

def api(request):

    url = 'http://10.30.100.21:8000/api/login/'
    data = {'id':'12',
            'first_name':'sad', 
            'last_name':'ing', 
            'mobile':'1234554321',
            'email':'anirudh@gmail.com'}
   
   
    headers = {'Content-Type': 'application/json'}        

    # get_response = requests.post(url=url)
    # print(get_response, '-----GET')
    # if get_response.status_code == 200:
    #     print(get_response.text)

    post_response = requests.post(url=url, data=data)        
    print(post_response, '-----POST')
    
    if post_response.status_code == 200:
        # url_po = 'http://10.30.100.21:8069/api/fleet_student_data/'
        # acc_token = post_response.json()
        # headers = {'Authorization':acc_token['data'][0]['access_token']}        
        # data = requests.post(url=url_po, headers=headers)
        print(post_response.json())        
    else:
        print(post_response.json())        


    # put_respsonse = requests.put(url=url, headers=headers, json=data)        
    # print(put_respsonse, '-----PUT')
    # if put_respsonse.status_code == 200:
    #     print(put_respsonse.text)

    # patch_respsonse = requests.patch(url=url, headers=headers, json=data)        
    # print(patch_respsonse, '-----PATCH')
    # if patch_respsonse.status_code == 200:
    #     print(patch_respsonse.text)

    # delete_respsonse = requests.delete(url=url, headers=headers, json=data)        
    # print(delete_respsonse, '-----DELETE')
    # if delete_respsonse.status_code == 200:
    #     print(delete_respsonse.text)        

    return HttpResponse('OK OK OK')        