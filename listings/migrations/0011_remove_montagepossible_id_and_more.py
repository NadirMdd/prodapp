# Generated by Django 5.1.3 on 2024-11-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_montagepossible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='montagepossible',
            name='id',
        ),
        migrations.RemoveField(
            model_name='montagepossible',
            name='id_montage',
        ),
        migrations.AddField(
            model_name='montagepossible',
            name='id_auto_montage',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='montagepossible',
            name='id_manu_montage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
