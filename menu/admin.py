from django.contrib import admin

from .models import Category,Toppings, Items, Pricing
#Register your models here.
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Toppings)
admin.site.register(Pricing)