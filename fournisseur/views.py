from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from accueil.models import *
from accueil.forms import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
    
def mk_fournisseur_form(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    if request.method == 'POST':
        fournisseur_data = FournisseurForm(request.POST,request.FILES)

        if fournisseur_data.is_valid() :
            _login = fournisseur_data.cleaned_data['login']
            passe = fournisseur_data.cleaned_data['passe'] 
            mail  = fournisseur_data.cleaned_data['mail']
            nom   = fournisseur_data.cleaned_data['nom']
            nif   = fournisseur_data.cleaned_data['nif']
            adresse= fournisseur_data.cleaned_data['adresse']
            mrc   = fournisseur_data.cleaned_data['mrc']
            logo  =fournisseur_data.cleaned_data['logo']
            numero_tel = fournisseur_data.cleaned_data['numero_tel']

            fournisseur = Fournisseur(
                numero_tel= numero_tel,
                passe =passe,
                mail = mail,
                nom = nom,
                mrc = mrc,
                logo =logo,
                login = _login,
                adresse = adresse,
                nif = nif)

            if Fournisseur.objects.filter(Q(mail=mail)|Q(login=_login)).exists():
                error = "Un fournisseur avec ce e-mail ou login exist dejà !"
            else:
                user = User.objects.create_user(first_name=nom, last_name=nom, username=_login, email=mail, password=passe)
                fournisseur.save()
                before_post = False
        else :
            error = "Formulaire invalid !"
    else :
        mk_fournisseur_form = FournisseurForm()
        before_post = True

    return render(request, 'fournisseur_form.html', locals())

def mk_fournisseur_login(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()
    
    if request.user.is_authenticated :
        return redirect('/fournisseur/page')

    else:
        if request.method == 'POST' :
            login_data = FournisseurLoginForm(request.POST)
            if login_data.is_valid():
                _login      = login_data.cleaned_data['login']
                passe       = login_data.cleaned_data['passe']
                
                user = authenticate(username=_login, password=passe)

                if user is not None : 
                    login(request, user)
                    return redirect('/fournisseur/page')

                else: 
                    error = "Le login ou mot de passe est incorrect."

        login_form = FournisseurLoginForm()
        return render(request, 'fournisseur_login.html', locals())

def mk_fournisseur_page(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    if request.user.is_authenticated :    
        if request.method == 'POST' :
            product1 = ProduitForm1(request.POST, request.FILES)
            product2 = ProduitForm2(request.POST, request.FILES)

            if product1.is_valid() and product2.is_valid() :
                intitule    = product1.cleaned_data['intitule']
                prix        = product1.cleaned_data['prix']
                image       = product1.cleaned_data['image']
                description = product1.cleaned_data['description']
                mu          = product1.cleaned_data['mu']
                quantite    = product1.cleaned_data['quantite']
                
                dp          = product2.cleaned_data['dp']
                fabriquant  = product2.cleaned_data['fabriquant']
                marque      = product2.cleaned_data['marque']
                made_in     = product2.cleaned_data['made_in']
                pp          = product2.cleaned_data['pp']
                categorie_produit = product2.cleaned_data['categorie_produit']

                            
                produit     = Produit(
                    intitule=intitule,
                    prix= prix,
                    marque=marque,
                    fabriquant= fabriquant,
                    made_in=made_in,
                    pp=pp,
                    mu=mu,
                    description=description,
                    image=image,
                    fournisseur=current_fournisseur,
                    dp=dp,
                    quantite=quantite,
                    categorie_produit=categorie_produit
                )
                
                if action == 2 and (produit_id is not None and produit_id != '' ):
                    produit.id = produit_id
                
                produit.save() 
                products      = Produit.objects.filter(fournisseur=current_fournisseur)
                paginator     = Paginator(products, 10)
                page_number   = request.GET.get('page')
                products      = paginator.get_page(page_number)
        
        else :
            categories     = CategorieProduit.objects.all()
            form_products1 = ProduitForm1()
            form_products2 = ProduitForm2()
            
            action         = request.GET.get('action')
            produit_id     = request.GET.get('produit')
            quantite       = request.GET.get('quantite')
            
            if quantite != '' and quantite is not None:
                try :
                    quantite   = int(quantite)
                    u_product  = Produit.objects.get(id=produit_id)
                    u_product.quantite = u_product.quantite + quantite
                    u_product.save()
                    products   = Produit.objects.filter(fournisseur=current_fournisseur)
                except BaseExsception :
                    return redirect('/fournisseur/page')
    

            if action is not None :
                action = int(action)
                        
            
            if action == 1 :
                try :
                    d_produit = Produit.objects.get(id=produit_id)
                    if d_produit is not None :
                        d_produit.delete()
                except BaseExsception :
                    return redirect('/fournisseur/page')
            try :
                current_fournisseur = Fournisseur.objects.get(login=request.user.username)
                products            = Produit.objects.filter(fournisseur=current_fournisseur).order_by('id')    
                paginator           = Paginator(products, 10)
                page_number         = request.GET.get('page')
                products            = paginator.get_page(page_number)  
                
                all_achat           = Resrevation.objects.all()
            
                chiffre_affaire= 0.0
                for p in products :
                    chiffre_affaire += (p.quantite * p.prix)
                
                historique_achat    = []
                for achat in all_achat :
                    if achat.produit.fournisseur.id == current_fournisseur.id :
                        historique_achat.append(achat)
                
                clients         = len(historique_achat)
                all_fournisseur = Fournisseur.objects.all()
                rang = 0
                for i, f in enumerate(all_fournisseur):
                    if f.id == current_fournisseur.id:
                        rang = i + 1
                        break                
                                
            except BaseException as e:
                logout(request)
                return redirect('/fournisseur/login')  
                        
        return render(request, 'fournisseur_page.html', locals())
    else :
        return redirect('/fournisseur/login')
    