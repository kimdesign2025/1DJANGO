from django.db import models
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    prix = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nom
