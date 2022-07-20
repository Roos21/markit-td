from django.urls import path,include
from client import views
urlpatterns = [
    path('',views.mk_client_login),
    path('login/', views.mk_client_login),
    path('ajouter-client/', views.mk_client_ajouter),
    path('page/', views.mk_client_page),
    path('ajouter-au-panier',views.mk_ajouter_au_panier),
    path('abandonner',views.mk_client_abandonner),
    path('reserver/',views.mk_commander),
]