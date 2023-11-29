from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from class_base_view.models import Employee
from .forms import UserForm, UserRegistrationForm
from django.core.mail import send_mail  
from CBV import settings  

# Create your views here.

def index(request):
    return render(request, 'authentication/index.html', {})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect('/user')
    else:
        form = UserForm()
        return render(request, 'authentication/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/signup.html', {'form': form})



def display_tasks(request):
    tasks =Employee.objects.all()
    return render(request, 'authentication/display_tasks.html', {'tasks': tasks})

@require_http_methods(['DELETE'])
def delete_task(request, id):
    Employee.objects.filter(id=id).delete()
    tasks = Employee.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})


def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "selvakt123@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  