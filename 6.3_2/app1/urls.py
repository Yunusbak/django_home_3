from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('phones/<int:category_id>/', views.phone_list, name='phone_list'),
]
