from django.db import models

class Produit(models.Model):
    # Nom du produit
    nom = models.CharField(max_length=255)

    # Description facultative
    description = models.TextField(null=True, blank=True)

    # Prix du produit (utilisation d’un float simple)
    prix = models.FloatField()

    # Image du produit (enregistrée dans 'images/')
    image = models.ImageField(upload_to='images/')

    # Quantité en stock (IMPORTANT pour les statistiques)
    quantite = models.IntegerField(default=0)  # <-- Ajouté ici correctement

    def __str__(self):
        # Affichage lisible du produit dans l’admin ou le shell
        return self.nom

    def get_image_url(self):
        # Retourne l'URL de l'image si elle existe, sinon None
        if self.image:
            return self.image.url
        return None
