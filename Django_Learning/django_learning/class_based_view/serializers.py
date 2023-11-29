from rest_framework import serializers
from .models import EducationDetail, CustomUser

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile']
