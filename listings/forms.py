from django import forms

from listings.models import  Client,Commande,tps_travail

# cette partie est en cours de devloppement (Vue.js)
class ClientForm(forms.ModelForm):
   class Meta:
     model = Client
     fields = '__all__'

class CommandeForm(forms.ModelForm):
   class Meta:
     model = Commande
     fields = '__all__'

class tps_travailForm(forms.ModelForm):
   class Meta:
     model = tps_travail
     fields = '__all__'