# Generated by Django 5.2 on 2025-04-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_produit_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='quantite',
            field=models.IntegerField(default=0),
        ),
    ]
