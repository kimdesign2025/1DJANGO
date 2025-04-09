from django.urls import path
from .views import home_view, Create_produit, dashboard_home_page, product_list, product_detail, UpdateProduit, delete_produit

app_name = 'produit'

urlpatterns = [
    path('', home_view, name='home_view'),  # Définition d'une url pour la page d'accueil
    path('dashboard/', dashboard_home_page, name='dashboard_home_page'),
    path('list_product/', product_list, name='list_product'),
    path('create-produit/', Create_produit.as_view(), name='create_produit'),  # Création de produit
]

# Ajouter les URLs pour afficher les détails d'un produit, le mettre à jour, ou le supprimer
urlpatterns += [
    path('produit/<int:pk>/', product_detail, name='product_detail'),  # Détails d'un produit
    path('produit/<int:pk>/update/', UpdateProduit.as_view(), name='product_update'),  # Mise à jour d'un produit
    path('produit/<int:pk>/delete/', delete_produit, name='product_delete'),  # Suppression d'un produit
]
