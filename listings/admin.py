from django.contrib import admin
from listings.models import  Client, Camion, Benne, Option, Commande, Operateur, MontagePossible, tps_travail

#Ce fichier admin facilite la gestion des données dans l'intreface d'administration django (http://127.0.0.1:8000/admin/)
#Cela permet a l'administrateur d'Créer, Lire, Modifier et Supprimer (CRUD) les données. exemple si l'adminsitrateur veut modifier l'adresse clientX il peut le faire sur (http://127.0.0.1:8000/admin/listings/client/) 
#Comportement dans l'interface :
#Les champs définis dans list_display seront affichés comme colonnes dans la vue liste.
#Une barre de recherche apparaîtra pour rechercher des clients à l'aide des champs définis dans search_fields.
# ----------------------------------------------------------------------------------------------------------

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'prenom_client', 'adresse_client', 'cp_client', 'phone_client')  
    search_fields = ['nom_client', 'prenom_client', 'adresse_client', 'cp_client', 'phone_client']

admin.site.register(Client, ClientAdmin)

class CamionAdmin(admin.ModelAdmin):
    list_display = ('id_camion','marque', 'modele', 'ptc', 'longueur', 'empattement') 
    search_fields = ['marque', 'modele', 'ptc', 'longueur', 'empattement']

admin.site.register(Camion, CamionAdmin)

class BenneAdmin(admin.ModelAdmin):
    list_display = ('id_benne','nom_benne', 'poids_benne', 'tps_montage_standard', 'tps_peinture_standard')  
    search_fields = ['nom_benne', 'poids_benne', 'tps_montage_standard', 'tps_peinture_standard']

admin.site.register(Benne, BenneAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('id_option','nom_option', 'tps_option_standard') 
    search_fields = ['nom_option', 'tps_option_standard']

admin.site.register(Option, OptionAdmin)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'MontagePossible', 'option', 'date_commande', 'date_livraison_prevue', 'date_debut_montage')
    search_fields = ['client__nom_client', 'client__prenom_client', 'MontagePossible__camion__marque', 'MontagePossible__benne__nom_benne']

admin.site.register(Commande, CommandeAdmin)

class OperateurAdmin(admin.ModelAdmin):
    list_display = ('id_operateur','nom_operateur', 'prenom_operateur', 'statut_operateur', 'specialite_operateur')  
    search_fields = ['nom_operateur', 'prenom_operateur', 'statut_operateur', 'specialite_operateur']

admin.site.register(Operateur, OperateurAdmin)

class MontageAdmin(admin.ModelAdmin):
    list_display = ('id_montage', 'camion', 'benne', 'allonge_chassis', 'surelevation', 'espacement_cabine')
    search_fields = ['camion__marque', 'benne__nom_benne', 'allonge_chassis', 'surelevation', 'espacement_cabine']

admin.site.register(MontagePossible, MontageAdmin)

class tps_travailAdmin(admin.ModelAdmin):
    list_display = ('commande', 'operateur_principal',  'operateur_2', 'operateur_3', 'tps_option_standard', 'tps_option_reel', 'tps_montage_standard', 'tps_montage_reel', 'tps_peinture_standard', 'tps_peinture_reel')
    list_filter = ('commande', 'operateur_principal')
    search_fields = ('commande__id', 'operateur_principal__nom')
    ordering = ('commande', 'operateur_principal')

    def tps_montage_reel_display(self, obj):
        return f"{obj.tps_montage_reel:.2f} h"
    tps_montage_reel_display.short_description = "Temps Montage Réel"

admin.site.register(tps_travail, tps_travailAdmin)





