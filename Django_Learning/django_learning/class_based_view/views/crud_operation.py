from django.shortcuts import render,redirect
from django.http import HttpResponse  
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from ..models import EducationDetail, CustomUser
from ..forms import EducationDetailForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class StudentForm(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EducationDetailForm
    template_name = 'education_form.html'
    success_url = reverse_lazy('stdnt_form')
    success_message = " Mark was created successfully"

class StudentList(ListView):    
    model = EducationDetail
    template_name = 'student_list.html'
    context_object_name = 'stnd_obj'

    def get(self, request, *args, **kwargs):
        
        if 'education' in cache:
            data = cache.get('education')
            print('Hit the cache')
        else:
            data = self.model.objects.all()
            cache.set('education', data, timeout=3600)
            print('Hit database')
        self.data = data
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.data
        return context
    
    
class StudentDetail(DetailView):
    model = EducationDetail
    template_name = 'student_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TESTING'] = 'HELLO THIS GOOD'
        return context
    
class StudentUpdate(UpdateView):
    model = EducationDetail
    template_name = 'student_update.html'
    fields = ['cgpa_10th']
    success_url = reverse_lazy('stdnt_list')

    def form_valid(self, form):
        print('DDDDDDD', form.cleaned_data['cgpa_10th'])
        # Add additional logic here
        return super().form_valid(form)
    
class StudentDelete(DeleteView): 
    model = EducationDetail
    success_url = reverse_lazy('stdnt_list')
    template_name = 'student_delete.html'
    context_object_name = 'user'

    def delete(self, request, *args, **kwargs):
        print(request,'DDDDD')
        print(kwargs,'DDDDD')
        return super().delete(request, *args, **kwargs)
    
def test_date(request):
    if request.method =='POST':
        print(request.POST['date_test'])
        exit()