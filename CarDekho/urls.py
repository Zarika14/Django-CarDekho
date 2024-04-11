
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.car_list_view, name='car_list_view'),
    path('<int:id>/', views.car_details_view, name='car_details_view'),
    path('showroom/', views.Showroom_view.as_view(), name='showroom_view'),
    path('details/<int:id>/', views.Showroom_details.as_view(), name='showroom_details')
]

