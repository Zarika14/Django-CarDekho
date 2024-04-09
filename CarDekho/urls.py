from django.urls import path
from .import views



urlpatterns = [
    
    path('list/', views.car_list_view, name = 'car_list_view'),
    path('<int:id>/', views.get_particular_car_details, name = 'get_particular_car_details'),
    path('update/<int:id>/', views.update_car_details, name = 'update_car_details'),
    path('delete/<int:id>/', views.delete_car_details, name = 'delete_car_details'),
    path('showroom/',views.Showroom_view.as_view(),name = 'showroom_view')
    
]