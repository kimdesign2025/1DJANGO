from django.urls import path
from.views import index ,Create_produit #pour importer la vues de index

app_name = 'produit'
urlpatterns =[
    path('',index, name='index'), #définition d'une url pour la page d'accueil qui renvoie vers la fonction index
    path('create-produit/',Create_produit.as_view(), name='create_produit'), #

]