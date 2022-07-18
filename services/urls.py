from django.contrib import admin
from django.urls import path

from services import views

urlpatterns = [
    path('service_depannage/', views.mk_service_depannage),
    path('service_location/', views.mk_service_location),
    path('service_livraison/', views.mk_service_livraison),
    path('autre/', views.mk_autres_service),
    path('service/solicitation/', views.mk_solicitation_service),
]