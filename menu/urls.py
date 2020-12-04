from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="home"),
    path("menu", views.menu, name="menu"),
    re_path(r'^show_items/(?P<c_name>.+?$)',views.show_items, name="show_items") #match urls when the name of my model has a space in it
]
