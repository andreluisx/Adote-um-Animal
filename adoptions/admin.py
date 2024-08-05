from django.contrib import admin
from .models import Type, Animal, AnimalImage

admin.site.register(Type)
admin.site.register(AnimalImage)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'raca', 'genero', 'disponivel')

admin.site.register(Animal, AnimalAdmin)