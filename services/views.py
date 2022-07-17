from django.shortcuts import render
from accueil.models import *
from accueil.forms import *
# Create your views here.

def mk_service_depannage(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    return render(request,'service_depannage.html',locals())

def mk_service_location(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    return render(request,'service_location.html',locals())

def mk_service_livraison(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    return render(request,'service_livraison.html',locals())

def mk_autres_service(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()
    from_solicitation_service = SolliciterForm()
    return render(request,'autres_service.html',locals())

def mk_solicitation_service(request):
    mk_partenaires = Partenaire.objects.all()
    mk_services    = Service.objects.all()

    from_solicitation_service = SolliciterForm()

    return render(request, 'service_solicitation.html', locals())

