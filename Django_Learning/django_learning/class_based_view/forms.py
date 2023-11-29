from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import EducationDetail

EducationDetail = get_user_model()

# validation field 
def mobile_no(value):
    mobile = str(value)
    if len(mobile) != 10:
        raise forms.ValidationError("Mobile Number Should 10 digit")
    
class EmployeeRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(help_text='Proper Email')
    mobile = forms.IntegerField(required=True, validators=[mobile_no])

    class Meta:
        model = EducationDetail
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email','mobile':'Mobile'}

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())



class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(max_length=50)