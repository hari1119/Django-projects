from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from .models import CustomUser, EducationDetail, PlacementCompany

    
@receiver(pre_save, sender=EducationDetail)
def check_user(sender, instance, **kwargs):
    print(sender.objects.get(id=instance.id))
    print('pre_save')
    

@receiver(post_save, sender=EducationDetail) 
def create_user(sender, instance, created, **kwargs):
    print(sender.objects.get(id=instance.id).cgpa_10th)
    print("Save method is called")
    
   
@receiver(pre_delete, sender=EducationDetail)         
def delete_user(sender, instance, **using):
    print(sender)
    print(instance)
    print(using)
    print(sender.objects.get(id=instance.id).cgpa_10th)
    print("pre_delete")


@receiver(post_delete, sender=EducationDetail)         
def delete_user(sender, instance, **using):
    print(sender)
    print(instance)
    print(using)
    print("post_delete")
