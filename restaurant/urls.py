from django.contrib import admin
from django.urls import path

from restaurant import views

urlpatterns = [
    path('',views.mk_resraurant_index),
    path('creer',views.mk_restaurant_creer),
    path('index',views.mk_restaurant_page),
    path('search',views.mk_search_plat,name='search'),
    path('menu',views.mk_restaurant_menu),
]