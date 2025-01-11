from rest_framework import viewsets
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from listings.models import  Client, Camion,Benne,Option,Commande,MontagePossible,Operateur
from listings.serializers import ClientSerializer, BenneSerializer, CamionSerializer,OptionSerializer, CommandeSerializer
#from listings.forms import ContactUsForm
from listings.forms import  ClientForm,CommandeForm,tps_travailForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

def about (request):
    return HttpResponse('<h1>aAbout-us.</h1> <p>We still we rise.</p>')

def tps_travail(request):
    if request.method == 'POST':
        form = tps_travailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le travail a été enregistré avec succès.")
            return HttpResponseRedirect(reverse('planning'))
        else:
            messages.error(request, "Erreur lors de l'enregistrement du formulaire.")
    else:
        form = tps_travailForm()

    commandes = Commande.objects.all()
    operateurs = Operateur.objects.all()

    options = Option.objects.values('tps_option_standard')
    bennes_montage = Benne.objects.values('tps_montage_standard')
    bennes_peinture = Benne.objects.values('tps_peinture_standard')

    context = {
        'form': form,
        'commandes': commandes,
        'operateurs': operateurs,
        'options': options,
        'bennes_montage': bennes_montage,  
        'bennes_peinture': bennes_peinture,  
    }
    return render(request, 'listings/planning.html', context)

def commandes_en_cours(request):
    commandes = Commande.objects.all() 
    commandes_with_ecart = []

    for commande in commandes:
        ecart = (commande.date_livraison_prevue - commande.date_commande).days
        commandes_with_ecart.append({
            'commande': commande,
            'ecart': ecart
        })
    return render(request, 'listings/prod.html', {'commandes':  commandes_with_ecart})

def contact(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Vos informations ont été transmises avec succès.")
           return HttpResponseRedirect(reverse('home')) 
    else:
        form = ClientForm()

    return render(request, 'listings/contact.html', {'form': form})


def commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Vos informations ont été transmises avec succès.")
           return HttpResponseRedirect(reverse('home')) 
    else:
        form = CommandeForm()

    return render(request, 'listings/commande.html', {'form': form})

def home(request):
    return render(request, 'listings/home.html')

# cette partie est en cours de devloppement (VUe.js)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class BenneViewSet(viewsets.ModelViewSet):
    queryset = Benne.objects.all()
    serializer_class = BenneSerializer
    
class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer