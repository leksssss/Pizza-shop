from django.contrib import admin

from .models import Category, Items, Toppings, Pricing
# Register your models here.
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Toppings)
admin.site.register(Pricing)