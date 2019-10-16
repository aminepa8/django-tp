from django.db import models

# Create your models here.
from django.db import models

class Categorie(models.Model):
    CodeCategorie = models.CharField(max_length=10,primary_key=True)
    LibelleCategorie=models.CharField(max_length=35)
    Illustration = models.FileField(upload_to='uploads/',blank=True)


    def __str__(self):
        return self.LibelleCategorie

    class Meta:
        ordering = ('LibelleCategorie',)

class Articles(models.Model):
    Reference = models.CharField(max_length=10, primary_key=True)
    Designation = models.CharField(max_length=25)
    PrixUnitaire = models.DecimalField(decimal_places=2,max_digits=10)
    CodeCategorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.Designation

    class Meta:
        ordering = ('Designation',)

class Depot(models.Model):
    CodeDepot = models.CharField(max_length=10 , primary_key=True)
    AdresseDepot = models.CharField(max_length=50)
    VilleDepot = models.CharField(max_length=25)
    Articles = models.ManyToManyField(Articles , through="stock")

    def __str__(self):
        return self.CodeDepot

    class Meta:
        ordering = ('CodeDepot',)

class Stock(models.Model):
    CodeDepot = models.ForeignKey(Depot, on_delete=models.CASCADE)
    Reference = models.ForeignKey(Articles, on_delete=models.CASCADE)
    QteEnStock = models.IntegerField()
    SeuilStock = models.IntegerField()

    class Meta:
        unique_together = ['CodeDepot', 'Reference']

