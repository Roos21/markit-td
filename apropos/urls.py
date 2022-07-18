from django.contrib import admin
from django.urls import path

from apropos import views

urlpatterns = [
    path('apropos/', views.mk_apropos),
]