from django.contrib import admin
from django.urls import path

from fournisseur import views

urlpatterns = [
    path('fournisseur/', views.mk_fournisseur_form),
    path('fournisseur/login', views.mk_fournisseur_login),
    path('fournisseur/page', views.mk_fournisseur_page),
]