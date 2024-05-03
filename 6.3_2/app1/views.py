# views.py

from django.shortcuts import render
from .models import Category, telephone

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def phone_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    phones = telephone.objects.filter(category=category)
    return render(request, 'phone_list.html', {'category': category, 'phones': phones})
