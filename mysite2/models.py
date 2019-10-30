# Create your models here.
from django.db import models

# Create your models here.
#la table categorie
class Categorie(models.Model):
    Code_Categorie = models.CharField(max_length=200 , primary_key=True)
    Libelle        = models.CharField(max_length=300)
    Illustration   = models.CharField(max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.Code_Categorie

#la table article
class Article(models.Model):
    Reference      = models.CharField(max_length=200 , primary_key=True)
    Designation    = models.CharField(max_length=200)
    Prixunitaire   = models.IntegerField(null=True)
    Code_Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.Reference

class Depot(models.Model):
    CodeDepot      = models.CharField(max_length=200 , primary_key=True)
    AdresseDepot   = models.CharField(max_length=200)
    VilleDepot     = models.CharField(max_length=200)

    def __str__(self):
        return self.CodeDepot

class Stocker(models.Model):
    Reference      = models.ForeignKey(Article, on_delete=models.CASCADE)
    CodeeDepot     = models.ForeignKey(Depot, on_delete=models.CASCADE)
    QteEnStock     = models.CharField(max_length=200 )
    SeuilStock     = models.CharField(max_length=200 )

    def __str__(self):
        return self.Reference
    class Meta:
        unique_together = ['CodeeDepot', 'Reference']






