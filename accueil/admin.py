from django.contrib import admin

# Register your models here.

from accueil.models import *

admin.site.register(Fournisseur)
admin.site.register(Produit)
admin.site.register(Ville)
admin.site.register(CategorieProduit)
admin.site.register(Categorie)
admin.site.register(Consommateur)
admin.site.register(Commentaire)
admin.site.register(Resrevation)
admin.site.register(Payement)
admin.site.register(Administrateur)
admin.site.register(TypeService)
admin.site.register(Solliciter)
admin.site.register(Livreur)
admin.site.register(Publicite)
admin.site.register(Administrer)
admin.site.register(ModeDePayementFournisseur)
admin.site.register(Partenaire)
admin.site.register(Service)
admin.site.register(Panier)
admin.site.register(Plat)
admin.site.register(Restaurant)
