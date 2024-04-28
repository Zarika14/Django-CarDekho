
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('showroom',views.Showroom_viewset,basename='showroom')

urlpatterns = [
    path('list/', views.car_list_view, name='car_list_view'),
    path('<int:id>/', views.car_details_view, name='car_details_view'),
    path('',include(router.urls)),
    # path('showroom/', views.Showroom_view.as_view(), name='showroom_view'),
    # path('showroom/<int:id>/', views.Showroom_details.as_view(), name='showroom_details'),
    path('review',views.Review_view.as_view(),name='review_list'),
    path('review/<int:pk>',views.Review_details.as_view(),name='review_details'),
    
]

