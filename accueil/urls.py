from django.contrib import admin
from django.urls import path

from accueil import views

urlpatterns = [
    path('', views.mk_index),
    path('filtre',views.mk_filter,name='filtre'),
    path('accueil/produit/',views.mk_produit_info),
]