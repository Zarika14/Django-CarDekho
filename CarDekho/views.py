from django.shortcuts import render
from .models import Carlist,Showroomlist
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .api_file.serializers import CarSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json


# Create your views here.
# def car_list_view(request):
    # cars = Carlist.objects.all()
    
    # # Serialize each car instance into a dictionary
    # car_data = [model_to_dict(car) for car in cars]
    
    # return JsonResponse(car_data, safe=False)

# def get_particular_car_details(request,id):
    
    # car = Carlist.objects.get(id=id)
    
    # data = model_to_dict(car)
    
    # return JsonResponse(data)
    
@api_view(['GET','POST'])
def car_list_view(request):
    
    if request.method == 'GET':
    
        car = Carlist.objects.all()
        print(car)
        serializer = CarSerializer(car, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        else:
            return Response(serializer.errors)
        
    
            
# @api_view()
# def get_particular_car_details(request,id):
#     if request.method == 'GET':
#         car = Carlist.objects.get(id=id)
#         serializer = CarSerializer(car)
    
#         return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def car_details(request,id):
    if request.method == 'GET':
        car = Carlist.objects.get(id=id)
        
        serializer = CarSerializer(car)
        
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(id=id)
        serializer = CarSerializer(car, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        car = Carlist.objects.get(id = id)
        car.delete()
        return Response({'message':'Car deleted Successfully'},status = 200)        


# @api_view(['DELETE'])
# def delete_car_details(request,id):
#     if request.method == 'DELETE':
#         car = Carlist.objects.get(id = id)
#         car.delete()
#         return Response({'message':'Car deleted Successfully'},status = 200)        
        

# APIs USING CLASS VIEW
class Showroom_view(APIView):
    
    def get(self, request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors) 

# APIs FOR UPDATE, GET AND DELETE

class Showroom_details(APIView):
    def get(self,request,id):
        try:
            showroom = Showroomlist.objects.get(id=id)
        except Showroomlist.DoesNotExist:
            return Response({'message':'Showroom not found'}, status = 400) 
         
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data) 
    
    def put(self,request,id):
        showroom = Showroomlist.objects.get(id = id)
        serializer = ShowroomSerializer(showroom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return(serializer.data)
        else:
            return Response(serializer.errors) 
        
    def delete(self,request,id):
        showroom = Showroomlist.objects.get(id = id)
        showroom.delete()  
        return Response({'message':'Showroom deleted Successfully'},status =200)      