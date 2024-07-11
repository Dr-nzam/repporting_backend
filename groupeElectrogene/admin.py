from django.contrib import admin
from .models import (Donneegroupeelectrogene, Equipementsite,Site, 
                     Donneesenergetiques, Donneesonduleur, Client,
                     Donneessallesarchives, Journal)
# Register your models here.

admin.site.register(Donneegroupeelectrogene)
admin.site.register(Equipementsite)
admin.site.register(Site)
admin.site.register(Client)
admin.site.register(Donneesenergetiques)
admin.site.register(Donneesonduleur)
admin.site.register(Donneessallesarchives)
admin.site.register(Journal)