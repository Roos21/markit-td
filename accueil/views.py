from django.shortcuts import render, redirect
from accueil.models import *
import json
from django.contrib.auth import logout
from django.http import JsonResponse
# Create your views here.
PRODUIT     = []
NEW_PRODUIT = []
PARTENAIRE  = []
SERVICE     = []

def mk_index(request):
    global PRODUIT, NEW_PRODUIT, PARTENAIRE, SERVICE
    mk_categories  = CategorieProduit.objects.all()
    mk_produits    = Produit.objects.all()
    mk_partenaires = Partenaire.objects.all()
    PRODUIT        = mk_produits
    PARTENAIRE     = mk_partenaires
    mk_services    = Service.objects.all()
    SERVICE        = mk_services
    mk_pubs        = Publicite.objects.all()
    mk_news_products= Produit.objects.order_by('-id')
    NEW_PRODUIT    = mk_news_products
    if(mk_pubs.count()>0): first_pub      = mk_pubs[0]
    mk_pubs        = mk_pubs[1:]

    mk_first_produits = mk_produits[:1]
    mk_produits       = mk_produits.order_by("-vue")[:10]
    try:
        mk_filtre_width   = 100 / len(mk_categories) * 5
    except ZeroDivisionError:
        pass

   
    return render(request, 'index.html', locals())


def mk_filter(request):
    global PRODUIT
    filtres    = json.JSONDecoder().decode(request.POST.get('filtres'))
    list_filtre= []
    if(len(filtres) > 0) :
        for produit in PRODUIT :
            if produit.categorie_produit.categorie in filtres :
                list_filtre.append(produit)
    else :
        list_filtre = PRODUIT
    
    html = ''' ''';
    
    if(len(list_filtre) > 0) :
        for p in list_filtre :
            html += '''
                <a onclick="displayDetails(this)" id="{}" class="card product-item" href="/accueil/produit/?id={}">
                    <img class="card-img-top" src="{}" width="100%" height="100%"
                        alt="Card image cap">
                    <div class="card-body">
                        <hr class="my-6">
                        <span class="card-title fw-bold">{}</span>
                        <h6>{}</h6>
                    </div>
                </a>
            '''.format(p.id,p.id,p.image.url, p.intitule, p.prix)
    else :
            
        html = '''
            <div class="text text-center fw-bold">
                <p>Oups... La categorie choisie est indisponible pour le moment...</p>
            </div>
        '''
        
    return JsonResponse({'r': {'filtres': html}})

def mk_produit_info(request):
    global PRODUIT, NEW_PRODUIT, SERVICE, PARTENAIRE
    mk_news_products  = []
    try:
        id                = request.GET.get('id')
        produit           = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        print("Produit does not exist")
    for p in PRODUIT:
        if p.categorie_produit.categorie == produit.categorie_produit.categorie :
            mk_news_products.append(p)
    
    mk_partenaires    = PARTENAIRE
    mk_services       = SERVICE
    mk_produits       = PRODUIT
    
    return render(request,'produit_info.html',locals())



def mk_commander(request):
    id_client = request.POST.get('client')
    paye = request.POST.get('paye')
    livre = request.POST.get('livre')
    client = Consommateur.objects.get(id=id_client)
    panier = Panier.objects.filter(consommateur=client)
    payement = Payement.objects.get(id=int(paye))
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

def mk_logout(request):
    logout(request)     
    return redirect('/')    
