from django.contrib import admin
from .models import Article
from .models import Stocker
from .models import Categorie
from .models import Depot

class Articles(admin.ModelAdmin):
    list_display  = ('Reference','Designation','Prixunitaire')
    ordering      = ('Reference',)
    search_fields = ('Reference',)

admin.site.register(Article , Articles)


class Depots(admin.ModelAdmin):
    list_display  = ('CodeDepot','AdresseDepot','VilleDepot')
    ordering      = ('CodeDepot',)
    search_fields = ('CodeDepot',)

admin.site.register(Depot, Depots)


class Stockers(admin.ModelAdmin):
    list_display  = ('CodeeDepot','Reference','QteEnStock','SeuilStock')
    ordering      = ('Reference',)
    search_fields = ('Reference',)

admin.site.register(Stocker,Stockers)

class Categories(admin.ModelAdmin):
    list_display  = ('Code_Categorie','Libelle','Illustration')
    ordering      = ('Code_Categorie',)
    search_fields = ('Code_Categorie',)
admin.site.register(Categorie,Categories)