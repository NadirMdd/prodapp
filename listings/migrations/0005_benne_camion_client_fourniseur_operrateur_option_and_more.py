# Generated by Django 5.1.3 on 2024-11-19 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_benne', models.CharField(max_length=50)),
                ('poids_benne', models.CharField(max_length=10)),
                ('tps_montage_standard', models.FloatField()),
                ('tps_peinture_reel', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=100)),
                ('ptc', models.CharField(max_length=10)),
                ('longueur', models.FloatField()),
                ('empattement', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100)),
                ('prenom_client', models.CharField(max_length=100)),
                ('adresse_client', models.TextField()),
                ('cp_client', models.CharField(max_length=100)),
                ('phone_client', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fourniseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fourniseur', models.CharField(max_length=100)),
                ('phone_fourniseur', models.CharField(blank=True, max_length=15, null=True)),
                ('adresse_fournisseur', models.CharField(max_length=100)),
                ('cp_fournisseur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Operrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_operateur', models.CharField(max_length=100)),
                ('prenom_operateur', models.CharField(max_length=100)),
                ('statut_operateur', models.CharField(max_length=100)),
                ('specialite_operateur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_option', models.CharField(max_length=50)),
                ('tps_option_standard', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateField()),
                ('date_livraison_prevue', models.DateField()),
                ('date_debut_montage', models.DateField()),
                ('temps_actuel', models.FloatField(default=0.0)),
                ('benne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.benne')),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.camion')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.client')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.option')),
            ],
        ),
    ]
