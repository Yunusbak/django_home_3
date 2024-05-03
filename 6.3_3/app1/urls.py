from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('animals/<int:category_id>/', views.animal_list, name='animal_list'),
]   
