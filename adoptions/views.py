from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Animal
# Create your views here.


def all_animals(request):
    return HttpResponse('oi')

def animal(request, id):
    animal = get_object_or_404(Animal, pk=id)
    images = animal.images.all()
    return render(request, 'animal.html', {'animal':animal, 'images':images})