from rest_framework import serializers
from .models import Client, Camion, Benne, Option, Commande

# cette partie est en cours de devloppement (VUe.js)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['nom_client', 'prenom_client', 'adresse_client', 'cp_client', 'phone_client']
class CamionSerializer(serializers.ModelSerializer):
    class Meta :       
        model = Camion
        fields = ['id_camion','marque', 'modele', 'ptc', 'longueur', 'empattement'] 
class BenneSerializer(serializers.ModelSerializer):
    class Meta :      
        model = Benne
        fields = ['id_benne','nom_benne', 'poids_benne', 'tps_montage_standard', 'tps_peinture_standard']
class OptionSerializer(serializers.ModelSerializer):
    class Meta :      
        model = Option
        fields = ['id_option','nom_option', 'tps_option_standard']
    
class CommandeSerializer(serializers.ModelSerializer):
    class Meta :      
        model = Commande
        fields =  ['client', 'benne', 'camion', 'option', 'date_commande', 'date_livraison_prevue', 'date_debut_montage']
        