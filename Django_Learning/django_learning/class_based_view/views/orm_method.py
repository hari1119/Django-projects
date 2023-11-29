from django.shortcuts import render,redirect
from django.http import HttpResponse  
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from ..models import EducationDetail, CustomUser
from ..forms import EducationDetailForm
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

class OrmFunction(ListView):

   model = CustomUser 

   # def get_queryset(self):
   #    all_data = CustomUser.objects.filter(id=1)
   #    print(all_data)
   #    return all_data
    
   # def get_context_data(self, **kwargs):
   #    context = super().get_context_data(**kwargs)
   #    all_datas = self.get_queryset().first()  
   #    print(all_datas)
   #    dmd = model_to_dict(all_datas)
   #    context['dmd'] = dmd
   #    return context

   def get(self, request):
      # self.object_list = self.get_queryset()
      # context = self.get_context_data()
      
      # print(all_data)
      # all_data = model_to_dict(all_data)
      print('###################')
      all_data = CustomUser.objects.filter(email__startswith='praba@').order_by('id').values('id','username', 'email')
      tay = CustomUser.objects.all().values()
      # &CustomUser.objects.filter(username__iendswith='a').order_by('id').values('id','username')
      print(all_data)
      print('###################')
      print(tay)
      return HttpResponse('Hello --> Class based view')
   # where_data = CustomUser.objects.filter(username='praba').values_list()
   # print(where_data,'----')
   
   
   # asc_order_by  = CustomUser.objects.all().order_by('id').values()
   # des_order_by  = CustomUser.objects.all().order_by('-id').values()
   # print(asc_order_by)
   # print(des_order_by)
   

   # where_orderby = CustomUser.objects.filter(username__istartswith='P').order_by('id').values('username','first_name', 'last_name','id')

   # create_data = CustomUser.objects.create(username='jhone', email='john@example.com').save()

   # update_data_for_one_obj = CustomUser.objects.get(usernam ='praba')
   # update_data_for_one_obj.mobile = 824801582
   # update_data_for_one_obj.save()

   # update_data_for_mul_obj=CustomUser.objects.filter(is_active=True).update(mobile=1231231232)

   # delete_one_obj = CustomUser.objects.get(name='John')
   # delete_one_obj.delete()

   # delete_mul_obj = CustomUser.objects.filter(name='John').delete()

    