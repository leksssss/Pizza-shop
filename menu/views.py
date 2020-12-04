from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "menu/home.html")

def menu(request):
    return render(request, "menu/index.html", {
       "categories": Category.objects.all()
    })

def show_items(request, c_name ):
    item_list =  Items.objects.filter(category_name__category_name=c_name)
    print(item_list)
    print(c_name)
    return render(request, "menu/items.html", {
        "items": Items.objects.filter(category_name__category_name=c_name)
    })