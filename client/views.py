from django.shortcuts import render, redirect
from accueil.models import *
from accueil.fonctions import*
import json
from accueil.forms import ClientLoginForm,ConsomateurForm
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.db.models import Q, Max
import datetime
from django.contrib.auth.models import User


# fonction d'authentification d'un utilisateur à la base de données
def mk_client_login(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()
    if request.user.is_authenticated :
        return redirect('/client/page')
    else:
        if request.method == 'POST':
            form = ClientLoginForm(request.POST)
            
            if form.is_valid():
                
                _login = form.cleaned_data['login']
                
                passe = form.cleaned_data['password']
                passe = mk_hash(passe)
                
                # authentification d'un nouvel utilisateur par la politique de django
                
                user = authenticate(username=_login, password=passe)
                print("[NEW USER] ==> %s"%user)
                if user is not None : 
                    login(request, user)
                    return redirect('/client/page')
                else:
                    erreur = True
                
            
        else:
            
            form = ClientLoginForm()
        
    return render(request,'login_client.html',locals())


def mk_client_ajouter(request):
    
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all() 
    # Si le formulaire d'inscription a été soumis
    
    if request.method == 'POST':
        
        form = ConsomateurForm(request.POST)
        
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            numero_tel = form.cleaned_data['numero_tel']
            adresse = form.cleaned_data['adresse']
            _login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            password_h = mk_hash(password)
            client = Consommateur(
                nom=nom, 
                prenom=prenom, 
                numero_tel=numero_tel,
                adresse=adresse,
                login=_login, 
                password=password_h,
                email=email
                )
            user = User.objects.create_user(first_name=prenom, last_name=nom, username=_login, email=email, password=password_h)
            client.save()
            save_client = True
            return redirect('/client/login')
            
        else:
            error_form = True
    else:
        
        form = ConsomateurForm()
    return render(request,'ajouter_client.html',locals()) 

# fonction pour gerer la page d'un client plus précisement son panier

def mk_client_page(request):
    balance = 0
    if not request.user.is_authenticated :
        return redirect('/client/login')
    if request.session.get('produit_selectionner'):
        try:
            produit = Produit.objects.get(id=request.session.get('produit_selectionner'))
            if produit is not None:
                try:
                    client = Consommateur.objects.get(login=request.user.username)
                    p = Panier.objects.get(Q(produit=produit) & Q(consommateur=client))
                    p.quantite += 1
                    p.save()
                    paniers = Panier.objects.filter(consommateur=client).order_by('-date')
                    total_article = len(paniers)
                    sms = True
                except Exception as e:
                    
                    panier = Panier(
                        produit=produit,
                        consommateur=client,
                        quantite=1
                    )
                    panier.save()
                    paniers = Panier.objects.filter(consommateur=client).order_by('-date')
                    total_article = len(paniers)
                    sms = True 
            for entre in paniers:
                balance += entre.produit.prix*entre.q
        except Exception as e:
            print("Lors de la page ",e)
    else:
       client = Consommateur.objects.get(login=request.user.username)
       paniers = Panier.objects.filter(consommateur=client).order_by('-date')
       total_article = len(paniers)
       sms = True 
       for entre in paniers:
           balance += entre.produit.prix*entre.quantite
    return render(request,'page_client.html',locals())

def mk_ajouter_au_panier(request):
    balance = 0
    try:
        id = int(request.GET.get('id'))
        request.session['produit_selectionner'] = id
        # Si l'utilisateur n'est pas connecté 
        try :
            
            if not request.user.is_authenticated :
                return redirect('/client/login')
            produit = Produit.objects.get(id=id)
            if produit is not None:
                client = Consommateur.objects.get(Q(login=request.user.username))
                try :
                    p = Panier.objects.get(Q(produit=produit) & Q(consommateur=client))
                    print(p)
                    if p.id>0:
                        p.quantite += 1
                        p.save()
                        
                except Exception as e:
                    print("Hum ", e)
                    panier = Panier(
                        produit=produit,
                        consommateur=client,
                        quantite=1
                    )
                    panier.save()
                paniers = Panier.objects.filter(consommateur=client).order_by('-date')
                total_article = len(paniers)
                for entre in paniers:
                    balance += entre.produit.prix*entre.quantite
        
                
            else:
                sms = "Produit inexistant"
                
        except Exception as e:
            
            print("Exception produit : ",e)
                    
    except:
        return redirect('/client')
    
    return render(request,'page_client.html',locals())


def mk_client_abandonner(request):
    try:
        id = int(request.GET.get('id'))
        panier = Panier.objects.get(id=id)
        if panier is not None:
            panier.delete()
            return redirect('/client/page')
    except Panier.DoesNotExist:
        print("Panier does not exist")
    return render(request,'page_client.html',locals())

def mk_commander(request):
    id_client = request.POST.get('client')
    paye = request.POST.get('paye')
    livre = request.POST.get('livre')
    client = Consommateur.objects.get(id=id_client)
    panier = Panier.objects.filter(consommateur=client)
    payement = Payement.objects.get(id=paye)
    livreur = Livreur.objects.get(id=1)
    ok = 0
    if int(livre) ==  1:
        for p in panier:
            reservation = Resrevation(
                client=client,
                payement=payement,
                livreur=livreur,
                produit=p.produit,
                quantite=p.quantite
            )
            reservation.save()
            p.delete()
        ok=1
    elif int(livre) == 2:
        for p in panier:
            reservation = Resrevation(
                client=client,
                payement=payement,
                livreur=livreur,
                produit=p.produit,
                quantite=p.quantite,
                livrer=2
            )
            reservation.save()
            p.delete() 
        ok = 2
    elif int(livre) == 3:
        for p in panier:
            reservation = Resrevation(
                client=client,
                payement=payement,
                livreur=livreur,
                produit=p.produit,
                quantite=p.quantite,
                livrer=3
            )
            reservation.save()
            p.delete() 
        ok = 3
        mk_partenaires = Partenaire.objects.all()
    return  render(request, 'client_login.html', locals())