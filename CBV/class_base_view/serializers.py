from rest_framework import serializers  
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=30)  
    last_name = serializers.CharField(max_length=30)  
    mobile = serializers.CharField(max_length=10)  
    email = serializers.EmailField()

    class Meta:  
        model = Employee  
        fields = ('__all__')  