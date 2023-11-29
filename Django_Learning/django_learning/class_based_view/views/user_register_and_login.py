from django.shortcuts import render,redirect
from django.http import HttpResponse  
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View  
from django.views.generic.base import TemplateView
# Default Register Form :: Method 1     
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Modified Register Form :: Method 2    
from django.views.generic import CreateView
from ..forms import EmployeeRegistrationForm, LoginForm
from ..models import CustomUser

from django.contrib.auth.models import auth,User
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your views here.
class Employee(LoginRequiredMixin,View):
    def get(self, request):
        return HttpResponse('Hello -- > Class based view')
    
# sample Tempalte render
class DemoTempalte(LoginRequiredMixin,TemplateView):    
    template_name = 'base.html'
    success_message = " DONE was updated successfully"

# Default Django Register Form :: Method 1     
class DefaultSignUp(SuccessMessageMixin,CreateView):    
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    model = CustomUser
    success_message = "%(email)s was created successfully"

# Modified Django Register Form :: Method 2    
class CustomSignUp(SuccessMessageMixin,CreateView):    
    form_class = EmployeeRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    model = CustomUser
    success_message = "%(username)s was created successfully"
    

class EmpLoginForm(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):

        to_return = super().form_valid(form)

        user = auth.authenticate(
            username=form.cleaned_data["user"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            auth.login(self.request, user)
            messages.info(self.request, "Message sent." )
            return to_return
        else:
            return redirect('emp_login')

    
        