from django.shortcuts import render
from accueil.models import *
import json
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
    first_pub      = mk_pubs[0]
    mk_pubs        = mk_pubs[1:]

    mk_first_produits = mk_produits[0]
    mk_produits       = mk_produits.order_by("-vue")[:10]
    mk_filtre_width   = 100 / len(mk_categories) * 5

   
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
    id                = request.GET.get('id')
    produit           = Produit.objects.get(id=id)
    for p in PRODUIT:
        if p.categorie_produit.categorie == produit.categorie_produit.categorie :
            mk_news_products.append(p)
    
    mk_partenaires    = PARTENAIRE
    mk_services       = SERVICE
    mk_produits       = PRODUIT
    
    return render(request,'produit_info.html',locals())