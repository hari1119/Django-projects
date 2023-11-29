from django.shortcuts import render,redirect
from django.http import HttpResponse  
from datetime import datetime
import pytz
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.views import View  
from django.contrib.auth.models import auth,User
from django.views import View  
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from ldap3 import Server, Connection, ALL, SUBTREE
import os
# Create your views here.

class ValidateUser(View):
    def post(self, request):
        user_name = request.POST["username"]
        password = request.POST["password"]

        if not User.objects.filter(username=user_name).exists():
            newuser = User.objects.create_user(username=user_name,password=password)
            newuser.save()
        user = auth.authenticate(username=user_name, password=password)
        auth.login(request,user)            

        return redirect('info_data:home_page')