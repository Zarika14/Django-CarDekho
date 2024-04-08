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
    
@api_view()
def car_list_view(request):
    car = Carlist.objects.all()
    serializer = CarSerializer(car, many = True)
    return Response(serializer.data)

@api_view()
def get_particular_car_details(request,id):
    car = Carlist.objects.get(id=id)
    serializer = CarSerializer(car)
    
    return Response(serializer.data)