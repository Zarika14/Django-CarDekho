from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .api_file.serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
        serializer = CarSerializer(car, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
    
            
        
        

@api_view()
def get_particular_car_details(request,id):
    car = Carlist.objects.get(id=id)
    serializer = CarSerializer(car)
    
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def update_car_details(request,id):
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
        

