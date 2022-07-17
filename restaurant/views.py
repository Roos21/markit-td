from operator import contains
from django.shortcuts import render,redirect
from accueil.forms import*
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.models import User
from accueil.models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from PIL import Image
#from accueil.fonctions import *

# Create your views here.

def mk_resraurant_index(request):
    if request.user.is_authenticated:
        return redirect('/restaurant/index')
    else :
        if request.method == 'POST':

            form = RestaurantFormLogin(request.POST)
    
            if form.is_valid():
                _login = form.cleaned_data['login']
                password = form.cleaned_data['password']
                user = authenticate(username=_login, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/restaurant/index')
                else:
                    error = True
        
        form = RestaurantFormLogin()

        return render(request, 'restaurant_index.html',locals())


def mk_restaurant_creer(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST,request.FILES)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            adresse = form.cleaned_data['adresse']
            logo = form.cleaned_data['logo']
            email = form.cleaned_data['email']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            specialite = form.cleaned_data['specialite']
            
            restaurant = Restaurant(
                nom=nom,
                adresse=adresse,
                logo=logo,
                email=email,
                login=login,
                password=password,
                specialite=specialite
            )
            
            if Restaurant.objects.filter(Q(email=email)|Q(login=login)).exists():
                error_exist  = True
            else:
                user = User.objects.create_user(first_name=nom, last_name=nom, username=login, email=email, password=password)
                restaurant.save()
                before_post = False
                succes = True
                return redirect('../restaurant/index')
            
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_creer.html', locals())
    
    
def mk_restaurant_page(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()    

    if request.user.is_authenticated :
        page    = request.GET.get('page')
        action = request.GET.get('action')
        plat = request.GET.get('plat')
        
        if request.method ==  'POST':
            form_plat = PlatForm(request.POST,request.FILES)
            
            if form_plat.is_valid():
                nom = form_plat.cleaned_data['nom']
                prix = form_plat.cleaned_data['prix']
                note = form_plat.cleaned_data['note']
                image = form_plat.cleaned_data['image']
                
                plat = Plat(
                    nom = nom,
                    prix=prix,
                    note=note,
                    image=image
                )
                plat.save()
                succes_create = True
                
            else:
                error_create = True
                
        if action != '' and action is not None:
            a = int(action)
            
            if a == 1 :
               d_palt = Plat.objects.get(id=plat)
               d_palt.delete()
               return redirect("../restaurant/index")   
        form_plat = PlatForm()
        products  = Plat.objects.all().order_by("id")
        paginator = Paginator(products,5)
        products  = paginator.get_page(page)
        current_restaurant = Restaurant.objects.get(login=request.user.username)
    
    else:
        return redirect('../restaurant/index')
    return render(request,'restaurant_page.html',locals())
    
    
def mk_search_plat(request):
    key_word = request.POST.get('key_word')
    plat = Plat.objects.filter(nom__contains=key_word)
    html = ""
    compteur = 0
    for p in plat:
        compteur += 1
        html += """
                    <tr>
                      <th scope="row">%s</th>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td class="col-lg-2">
                        <a class="btn btn-danger" id="delete">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
                            <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
                          </svg>
                        </a>
                        <a class="btn btn-primary" id = "edit-modal" >
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                          </svg>
                        </a>
                    
    
                        <div class="modal fade" id="edit-form" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                          <div class="modal-dialog">
                            <div class="modal-content">
                              <div class="modal-header">
                                <img src="/static/img/logo.png" width="100" alt="">
                              </div>
                              <div class="modal-body">
                                edit
                              </div>
                              <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="cancel-edit">Fermer</button>
                                <a type="button" class="btn btn-primary" href="?action=2&plat=%s">Modifier</a>
                              </div>
                            </div>
                          </div>
                        </div>
                      
                        <div class="modal fade" id="delete-form" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                          <div class="modal-dialog">
                            <div class="modal-content">
                              <div class="modal-header">
                                <img src="/static/img/logo.png" width="100" alt="">
                              </div>
                              <div class="modal-body">
                                Voulez vous vraiment Supprimer cet élément ????
                              </div>
                              <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="cancel-delete">Fermer</button>
                                <a type="button" class="btn btn-primary" href="?action=1&plat=%s">Supprimer</a>
                              </div>
                            </div>
                          </div>
                        </div>
                        
                        
                        <div class="modal fade" id="add-form" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                          <div class="modal-dialog">
                            <div class="modal-content">
                              <div class="modal-header">
                                <img src="/static/img/logo.png" width="100" alt="">
                              </div>
                              <div class="modal-body">
                                <input  type="text" class="form-control" placeholder="Quantitté" id="qte">
                              </div>
                              <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="cancel-add">Fermer</button>
                                <a type="button" class="btn btn-primary" href="?action=3&plat=%s" value="?action=3&plat=%s"  id="add-link">Ajouter la nouvelle valeur</a>
                              </div>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <script type="text/javascript">
      $("#delete").on('click',function(event){
        $("#delete-form").modal('show');
      })
      $("#cancel-delete").on('click',function(event){
        $("#delete-form").modal('hide');
      })
      
      $("#edit-modal").on('click',function(event){
        $("#edit-form").modal('show');
      })
      
      $("#cancel-edit").on('click',function(event){
        $("#edit-form").modal('hide');
      })
      
      $("#add-link").on('click',function(event){
        var a = document.getElementById("add-link");
        var qte = document.getElementById('qte').value;
        var link = a+"&qte="+qte;
      })

        
        """%(compteur,p.nom,p.prix,p.note,p.id,p.id,p.id,p.id)
        
    return JsonResponse({'r':{'rr':html}})
    
def mk_restaurant_menu(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all() 

    mk_plat        = Plat.objects.all()


    return render(request,'service_restauration_menu.html',locals())
    
    