from django.urls import path

from .views import index, city_add, city_detail, all_cities

app_name = 'details'

urlpatterns = [
    path('', index, name='index'),
    path('add/', city_add, name='add-city'),
    path('cities/', all_cities, name='cities'),
    path('<int:pk>/', city_detail, name='city-detail')
]