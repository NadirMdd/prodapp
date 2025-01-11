from django.db import models
from django.core.exceptions import ValidationError

# sur ce fichier models.py on retrouve les entitées du projet avec ses attributs 
# L’identifiant da chaque entitée est inscrit en tête de la liste  
# attribueX = models.TextField() signie que l'attribue est de type text
#attribueX= models.fields.CharField(max_length=100) signie que l'attribue contient des chiffres et des lettres
#----------------------------------------------------------------------------------------------------------------------
#Client
class Client (models.Model):
  nom_client= models.fields.CharField(max_length=100)
  prenom_client= models.fields.CharField(max_length=100)
  adresse_client = models.TextField()
  cp_client= models.fields.CharField(max_length=100)
  phone_client = models.CharField(max_length=15, null=True, blank=True) 
  def __str__(self):
    return f"{self.nom_client} {self.prenom_client}" 

#Camion   
class Camion (models.Model):
  id_camion = models.CharField(max_length=20,null=True,blank=True)
  marque=models.CharField(max_length=50)
  modele=models.CharField(max_length=100)
  ptc=models.CharField(max_length=10)
  longueur=models.FloatField()
  empattement=models.FloatField()
  def __str__(self):
    return f"{self.id_camion} - {self.marque} - {self.modele}" 

#Benne 
class Benne(models.Model):
  id_benne=models.CharField(max_length=20,null=True,blank=True)
  nom_benne=models.CharField(max_length=50)
  poids_benne=models.CharField(max_length=10)
  tps_montage_standard=models.FloatField()
  tps_peinture_standard=models.FloatField()
  
  def __str__(self):
    return f"{self.id_benne} :{self.nom_benne}-{self.poids_benne}-{self.tps_montage_standard}-{self.tps_peinture_standard}"
      
#Option
class Option(models.Model): 
  id_option=models.CharField(max_length=20,null=True,blank=True)
  nom_option=models.CharField(max_length=50)
  tps_option_standard=models.FloatField()     
  def __str__(self):
    return f"{self.id_option} :{self.nom_option}-{self.tps_option_standard}"

#Montage possible
class MontagePossible(models.Model):
    id_manu_montage = models.CharField(max_length=100, null=True, blank=True)
    id_auto_montage = models.AutoField(primary_key=True)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    benne = models.ForeignKey(Benne, on_delete=models.CASCADE)
    allonge_chassis = models.BooleanField(default=True)
    surelevation = models.BooleanField(default=True)
    espacement_cabine = models.CharField(max_length=50)

    @property
    def id_montage(self):
        if self.id_manu_montage:
            return self.id_manu_montage
        return f'MT-{self.id_auto_montage:05d}'

    def __str__(self):
        return f"{self.id_montage} - {self.camion.marque} - {self.benne.nom_benne} - Châssis: {self.allonge_chassis}, Surélévation: {self.surelevation}, Espacement: {self.espacement_cabine}"

#Commande
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    MontagePossible = models.ForeignKey(MontagePossible, on_delete=models.CASCADE, default=1)
    date_commande = models.DateField()
    date_livraison_prevue = models.DateField()
    date_debut_montage = models.DateField()

    def __str__(self):
        return f"Commande {self.id} - {self.client}-{self.MontagePossible.id_montage}"

#Opperateur  
class Operateur (models.Model):
  id_operateur=models.CharField(max_length=100,null=True,blank=True)
  nom_operateur = models.CharField(max_length=100)
  prenom_operateur = models.CharField(max_length=100)
  statut_operateur = models.CharField(max_length=100)
  specialite_operateur = models.CharField(max_length=100)
  def __str__(self):
    return f"{self.id_operateur}:{self.nom_operateur} {self.prenom_operateur}"
        
def validate_positive(value):
    if value is not None and value < 0:
        raise ValidationError("La valeur doit être positive.")
class tps_travail(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, default=1)
    operateur_principal = models.ForeignKey(
        Operateur, on_delete=models.CASCADE, related_name='tps_principal', default=1
    )
    operateur_secondaire = models.ForeignKey(
        Operateur,
        on_delete=models.CASCADE,
        related_name='tps_secondaire',
        null=True,
        blank=True,
        default=None
    )
    operateur_2 = models.ForeignKey(
        Operateur,
        on_delete=models.CASCADE,
        related_name='tps_operateur_2',
        null=True,
        blank=True
    )
    operateur_3 = models.ForeignKey(
        Operateur,
        on_delete=models.CASCADE,
        related_name='tps_operateur_3',
        null=True,
        blank=True
    )

    tps_option_standard = models.ForeignKey(
        Option, on_delete=models.CASCADE, related_name='option_standards', default=1
    )
    tps_option_reel = models.FloatField(null=True, blank=True)

    tps_montage_standard = models.ForeignKey(
        Benne, on_delete=models.CASCADE, related_name='montage_standards', default=1
    )
    tps_montage_reel = models.FloatField(null=True, blank=True)

    tps_peinture_standard = models.ForeignKey(
        Benne, on_delete=models.CASCADE, related_name='peinture_standards', default=1
    )
    tps_peinture_reel = models.FloatField(null=True, blank=True)

    def get_tps_option_standard(self):
        """
        Retourne le temps standard de l'option associée.
        """
        return self.tps_option_standard.tps_option_standard

    def __str__(self):
        return (f"Commande: {self.commande.id}, "
                f"Option Réel: {self.tps_option_reel or 'N/A'} h, "
                f"Montage Réel: {self.tps_montage_reel or 'N/A'} h, "
                f"Peinture Réel: {self.tps_peinture_reel or 'N/A'} h")

