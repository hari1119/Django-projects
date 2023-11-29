from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):  
        return "%s %s %s %s" % (self.first_name, self.last_name,self.mobile,self.email)  
