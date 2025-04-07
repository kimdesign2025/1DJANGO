from django.shortcuts import render ,HttpResponse  
from .models import Produit
from django.views import View
def index(request, *args, **kwargs):
    liste_produit = Produit.objects.all()
    context = {
        'liste_produit': liste_produit,
        'nom':'Produit de la boutique kim',
    }
    return render(request, 'index.html', context)

#creation du produit
class Create_produit(View):
    def get(self, request ,*args, **kwargs):
        return render(request, 'produit/create_produit.html') #renvoie le fichier entre ''
    def post(self, request ,*args, **kwargs):
        try:
            nom = request.POST.get('nom')
            description = request.POST.get('description')
            prix = request.POST.get('prix')
            image = request.FILES.get('image')
            produit = Produit.objects.create(nom=nom, description=description, prix=prix, image=image)
        
            if produit:
                    return HttpResponse('Produit créé avec succès')
        except Exception as e:
            return HttpResponse(f'Erreur lors de la création du produit : {str(e)}')
        