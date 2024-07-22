from django.contrib import admin
from .models import Type, Animal, AnimalImage

admin.site.register(Type)
admin.site.register(Animal)
admin.site.register(AnimalImage)