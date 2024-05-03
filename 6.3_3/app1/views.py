from django.shortcuts import render
from .models import Category, Animal  # Изменил импорт

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def animal_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    animals = Animal.objects.filter(category=category)  # Изменил переменную здесь
    return render(request, 'animal_list.html', {'category': category, 'animals': animals})
