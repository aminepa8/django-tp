from django.contrib import admin
from .models import Categorie,Articles,Depot,Stock
# Register your models here.
admin.site.register(Categorie)
admin.site.register(Articles)
admin.site.register(Depot)
admin.site.register(Stock)
