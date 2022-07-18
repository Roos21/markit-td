from django.shortcuts import render
from accueil.models import *
# Create your views here.
def mk_apropos(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    return render(request,'apropos.html',locals())