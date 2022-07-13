from django.urls import path,include
from client import views
urlpatterns = [
    path('add_to_card/', views.mk_client_add_to_card),
    path('add_client/', views.mk_client_add),
    path('add_client/save/', views.mk_client_save),
    path('check_password',views.mk_check_password,name='check_password'),
]