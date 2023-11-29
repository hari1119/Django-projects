from django.forms import fields
from .models import Employee
from django import forms


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



