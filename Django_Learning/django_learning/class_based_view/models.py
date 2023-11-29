from django.db import models
from django.contrib.auth.models import AbstractUser
from auditlog.registry import auditlog


# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.IntegerField(null=True)
    def __str__(self):
        return self.username
    
class PlacementCompany(models.Model):
    company = models.CharField(max_length=100, verbose_name="Company", blank=False, null=True)
    def __str__(self):
        return self.company
    class Meta:
        verbose_name_plural = "Companies"
        db_table = 'placement_company'


class EducationDetail(models.Model):
    username = models.OneToOneField(CustomUser,  on_delete=models.CASCADE,  blank=True,  null=True, db_constraint=False)
    cgpa_10th = models.CharField(max_length=100, verbose_name="CGPA of 10", blank=True, null=True)
    cgpa_12th = models.CharField(max_length=100, verbose_name="CGPA of 12", blank=True,  null=True)
    cgpa_ug = models.CharField(max_length=100,   verbose_name="CGPA of UG", blank=True, null=True)
    cgpa_pg = models.CharField(max_length=100,   verbose_name="CGPA of PG", blank=True, null=True)
    # companys  = models.ManyToManyField(PlacementCompany)
    
    def __str__(self):
        return self.username.username
    
    class Meta:
        verbose_name_plural = "Education"
        db_table = 'education_info'




auditlog.register(CustomUser)
auditlog.register(EducationDetail)
auditlog.register(PlacementCompany)