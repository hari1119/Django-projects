from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class EmployeeDetail(models.Model):

    first_name = models.CharField(max_length=50, verbose_name="First Name", blank=False, null=False)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", blank=False, null=False)
    email = models.EmailField(max_length=50, verbose_name="Email", blank=False, null=False) 
    mobile_number = models.CharField(max_length=13, verbose_name="Mobile Number", blank=False, null=False)
    date_of_birth = models.DateField(verbose_name="D.O.B",null=False)
    blood_group = models.CharField(max_length=5, verbose_name="Blood Group", blank=False, null=False)
    gender = models.CharField(max_length=10, verbose_name="Gender", blank=False, null=False)
    whatsapp_number = models.CharField(max_length=13, verbose_name="Whatsapp Number", blank=False, null=False)

    address_line_1 = models.TextField(max_length=100, verbose_name="Address Line 1", blank=False, null=False)
    address_line_2 = models.TextField(max_length=100, verbose_name="Address Line 2", blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name="City", blank=False, null=False)
    state = models.CharField(max_length=50, verbose_name="state", blank=False, null=False)
    postal_code = models.CharField(max_length=10, verbose_name="Postal code", blank=False, null=False)

    father_name = models.CharField(max_length=50, verbose_name="Father Name", blank=False, null=False)
    mother_name = models.CharField(max_length=50, verbose_name="Mother Name", blank=False, null=False)
    martial_statue = models.CharField(max_length=10, verbose_name="Martial Status", blank=True, null=True)
    wife_name = models.CharField(max_length=50, verbose_name="Wife Name", blank=True, null=True)

    language = ArrayField(models.CharField(max_length=20, verbose_name="Languages", blank=False, null=False))
    sports = ArrayField(models.CharField(max_length=20, verbose_name="Spors", blank=True, null=True))
    hobby = models.CharField(max_length=100, verbose_name="Hobbies", blank=True, null=True)

    current_company = models.CharField(max_length=100, verbose_name="Current company", blank=False, null=False)
    current_company_location = models.CharField(max_length=150, verbose_name="Current company location", blank=False, null=False)
    previous_company = models.CharField(max_length=100, verbose_name="Previous company", blank=True, null=True)
    previous_company_location = models.CharField(max_length=150, verbose_name="Previous company location", blank=True, null=True)
    designation = models.CharField(max_length=50, verbose_name="Designation", blank=False,null=True)
    year_of_experience = models.CharField(max_length=10, verbose_name="Years of Experience", blank=False, null=False)


    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = "Employee Details"
        db_table = 'employee_details'