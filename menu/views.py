from django.http import HttpResponse
from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    return render(request, "menu/index.html", {
        "categories": Category.objects.all()
    })
