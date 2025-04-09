from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produit
from django.views import View
from django.shortcuts import get_object_or_404


# ✅ Vue pour créer un produit
class Create_produit(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'produit/create_produit.html')

    def post(self, request, *args, **kwargs):
        try:
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            prix = request.POST.get('prix')
            image = request.FILES.get('image')
            quantite = request.POST.get('quantite')

            produit = Produit.objects.create(
                nom=nom,
                description=description,
                prix=prix,
                image=image,
                quantite=quantite
            )

            messages.success(request, "Produit créé avec succès!")
            return redirect('produit:list_product')

        except Exception as e:
            messages.error(request, f"Erreur lors de la création du produit : {str(e)}")
            return redirect('produit:create_produit')


# ✅ Page d'accueil
def home_view(request):
    context = {
        'nom': 'Bienvenue dans la boutique !'
    }
    return render(request, 'Home/pages/index.html', context)


# ✅ Page du tableau de bord (dashboard)
def dashboard_home_page(request):
    produits = Produit.objects.all()
    noms = [p.nom for p in produits]
    quantites = [p.quantite for p in produits]
    prix = [float(p.prix) for p in produits]

    context = {
        'labels': noms,
        'quantites': quantites,
        'prix': prix
    }
    return render(request, 'Dashboard/pages/index.html', context)


# ✅ Liste des produits
def product_list(request):
    produits = Produit.objects.all()
    context = {
        'produits': produits
    }
    return render(request, 'Dashboard/pages/list_produit.html', context)

# Voir un produit
def product_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'Dashboard/pages/detail_produit.html', {'produit': produit})

# Modifier un produit
class UpdateProduit(View):
    def get(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        return render(request, 'produit/update_produit.html', {'produit': produit})

    def post(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        produit.nom = request.POST.get('nom')
        produit.description = request.POST.get('description')
        produit.prix = request.POST.get('prix')
        produit.image = request.FILES.get('image') or produit.image
        produit.quantite = request.POST.get('quantite')
        produit.save()
        return redirect('produit:list_product')

# Supprimer un produit
def delete_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('produit:list_product')