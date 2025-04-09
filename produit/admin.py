from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    # Colonnes visibles dans la liste admin
    list_display = ('nom', 'prix', 'quantite', 'description', 'image')
