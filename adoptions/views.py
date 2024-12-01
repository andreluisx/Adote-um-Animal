from django.shortcuts import render, get_object_or_404
from .models import Animal
from .utils.states import STATES
from .utils.tipos import TIPOS
from user.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@require_POST
def toggle_favorite(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    user = request.user

    if animal in user.favoritos.all():
        user.favoritos.remove(animal)
        is_favorited = False
    else:
        user.favoritos.add(animal)
        is_favorited = True

    return JsonResponse({'is_favorited': is_favorited})

@login_required(login_url='/usuario/entrar/')
def animal(request, id):
    animal = get_object_or_404(Animal, pk=id)
    is_favorited = User.objects.filter(user_name=request.user.user_name, favoritos=animal.id).exists()
    images = animal.images.all()
    return render(request, 'animal.html', {'is_favorited':not is_favorited ,'animal':animal, 'images':images})


def todos(request):
    animais = Animal.objects.all().order_by('-id').filter(deleted_at=None)

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