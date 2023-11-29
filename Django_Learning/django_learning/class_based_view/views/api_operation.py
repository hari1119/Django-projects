from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.views import APIView  
from rest_framework.response import Response 
from rest_framework import status  
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from ..models import EducationDetail, CustomUser
from ..serializers import EducationSerializer, CustomUserSerializer
import json
from django.db import IntegrityError

class StudentData(APIView):  
    
    data = CustomUser.objects.all()
    serializer = CustomUserSerializer(data, many=True)
    # print(serializer.data) # IT CONVERT LIST OF TUPLE

    def get(self,request, *args, **kwargs):
        bytes_data = JSONRenderer().render(self.serializer.data)
        dict_data = json.loads(bytes_data)
        return Response(data= dict_data, status=status.HTTP_200_OK)
    
    def post(self,request):
        
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        mobile = request.data['mobile']
        email = request.data['email'] 
        print(request.data, 'DDDDDDDDDDDD')
        try:
            CustomUser(username=first_name+last_name ,first_name = first_name,last_name = last_name,mobile = mobile, email = email).save()     
            
            return Response(data={'Success':'Success','USER':self.serializer.data}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={'Success':'Failure', 'error': 'User with this username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request):
        update = CustomUser.objects.get(id=request.data['id'])
        update.first_name = request.data['first_name']
        update.last_name = request.data['last_name']
        update.mobile = request.data['mobile']
        update.email = request.data['email']
        update.save()
        return Response(data={'Success':'Success', "UPDATE":self.serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request):
        update = CustomUser.objects.get(id=request.data['id'])
        update.first_name = request.data['first_name']
        update.last_name = request.data['last_name']
        update.mobile = request.data['mobile']
        update.email = request.data['email']
        update.save()
        return Response(data={'Success':'Success', "UPDATE":self.serializer.data}, status=status.HTTP_200_OK)

        
    def delete(self,request):
        delete = CustomUser.objects.get(id=request.data['id'])
        delete.delete()
        return Response(data= {'done':'Success', "DELETE":self.serializer.data}, status=status.HTTP_200_OK)
