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
    c_name = c_name.strip('/')
    items = Items.objects.filter(category_name__category_name=c_name)
    columns = findItems(c_name)
    #toppings = None
    if c_name == "Regular Pizza" or c_name == "Sicilian Pizza":
        toppings = Toppings.objects.all()
    context = {
        "items" : items,
        "columns" : columns,
        "category" : c_name,
        "toppings" : toppings,
        "login_id" : "Login"
    }
    
    return render(request, "menu/items.html", context)

def findItems(category:str):
    if category == "Regular Pizza":
        columns = 3
    elif category == "Sicilian Pizza":
        columns = 3
    elif category == "Subs":
        columns = 3
    elif category == "Salads":
        columns = 2
    elif category == "Pasta":
        columns = 2
    elif category == "Dinner Platters":
        columns = 3
    return columns