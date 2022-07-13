from django.shortcuts import render
from accueil.models import *
from accueil.fonctions import*
import json
from accueil.forms import ClientLoginForm,ConsomateurForm
from django.http import JsonResponse
# Create your views here.
def mk_client_add_to_card(request):
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            try:
                client = Consommateur(login=login, password=password)
                if client.id>0:
                    envoi = client.id
                else:
                    envoi = -1
            except Exception as e:
                print(e)
    else:
        form = ClientLoginForm()
    return render(request,'client_login.html',locals())


def mk_client_add(request):
    if request.method == 'POST':
        envoi = 0
        form = ConsomateurForm(request.POST)
        
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            numero_tel = form.cleaned_data['numero_tel']
            adresse = form.cleaned_data['adresse']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            password = mk_hash(password)
            client = Consommateur(
                nom=nom, 
                prenom=prenom, 
                numero_tel=numero_tel,
                adresse=adresse,
                login=login, 
                password=password,
                email=email
                )
            client.save()
            save_client = True
    else:
        form = ConsomateurForm()  
    return render(request,'client_add.html',locals())
    
def mk_client_save(request):
    
    form = ConsomateurForm(request.POST) 
    return render(request,'client_add.html',locals())
    
    
def mk_check_password(request):
    result = 0
    key = request.POST.get('key')
    if mk_check_password(key) == True:
        result = 1
        
    print(key)
    return JsonResponse({'r': {'filtres': result}})