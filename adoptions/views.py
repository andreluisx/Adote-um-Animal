from django.shortcuts import render, get_object_or_404
from .models import Animal, Type
from .utils.states import STATES
from .utils.tipos import TIPOS
from django.core.paginator import Paginator
# Create your views here.

def animal(request, id):
    animal = get_object_or_404(Animal, pk=id)
    images = animal.images.all()
    return render(request, 'animal.html', {'animal':animal, 'images':images})
    
def todos(request):
    animais = Animal.objects.all().order_by('-id')

    pesquisa = request.GET.get('pesquisa', '')
    estado = request.GET.get('states', '')
    tipo = request.GET.get('tipo', '')

    if tipo and tipo != '1': 
        animais = animais.filter(tipo=tipo)

    if estado and estado != 'TD':
        animais = animais.filter(user__estado=estado)

    if pesquisa:
        animais = animais.filter(raca__icontains=pesquisa)

    paginator = Paginator(animais, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'animais': page_obj,
        'tipos': TIPOS, 
        'tipo_id': tipo if tipo != '1' else '',
        'pesquisa': pesquisa,
        'estado': estado if estado != 'TD' else '',
        'states': STATES
    }

    return render(request, 'all_animals.html', context)