# Generated by Django 5.1.3 on 2024-11-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Miscellaneous')], max_length=5),
        ),
    ]
