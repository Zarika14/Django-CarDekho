from django.urls import path
from . import views



urlpatterns = [
    
    path('list/', views.car_list_view, name = 'car_list_view'),
    path('<int:id>/', views.get_particular_car_details, name = 'get_particular_car_details'),
    # path('update/<int:id>/', views.update_blog, name = 'update_blog'),
    # path('delete/<int:id>/', views.delete_blog, name = 'delete_blog'),
    # path('listAll/', views.list_all_blog, name = 'list_all_blog'),
]