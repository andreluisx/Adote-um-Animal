from django.shortcuts import render, get_object_or_404, redirect
from adoptions.models import Animal, Type
from user.models import User, ProfileImage
from adoptions.utils.states import STATES
from adoptions.utils.tipos import TIPOS
from django.contrib import messages
from app.utils.image import is_valid_image_pillow
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    animals = Animal.objects.all().order_by('-id')[:3]
    return render(request, 'home.html', {'animals': animals})

@login_required(login_url=reverse_lazy('user:entrar'))
def meus_dados(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        cidade = request.POST.get('cidade')
        profile_image = request.POST.get('profile_image')
        user.cidade = cidade

        if 'profile_image' in request.FILES:
            profile_image = request.FILES['profile_image']
            if is_valid_image_pillow(profile_image):
                if ProfileImage.objects.filter(user=user).exists():
                    ProfileImage.objects.filter(user=user).delete()
                ProfileImage.objects.create(user=user, image=profile_image)
            else:
                messages.error(request, 'Oarquivo não é uma imagem.')
                return  redirect('app:meus_dados')

        user.save()
        messages.success(request, 'Informações alteradas com sucesso.')
        return  redirect('app:meus_dados')

    return render(request, 'meus_dados.html', {'user': user})

@login_required(login_url=reverse_lazy('user:entrar'))
def favoritos(request):
    animais = Animal.objects.filter(favorited_by=request.user).order_by('-id')
   
    pesquisa = request.GET.get('pesquisa', '')
    estado = request.GET.get('states', '')
    tipo = request.GET.get('tipo', '')
    
    if tipo and tipo != '1': 
        animais = animais.filter(tipo=tipo)

    if estado and estado != 'TD':
        animais = animais.filter(user__estado=estado)

    if pesquisa:
        animais = animais.filter(raca__icontains=pesquisa)

    paginator = Paginator(animais, 4)
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

    return render(request, 'favoritos.html',  context)

@login_required(login_url=reverse_lazy('user:entrar'))
def meus_animais(request):
    animais = Animal.objects.filter(user=request.user).order_by('-id')
    
    pesquisa = request.GET.get('pesquisa', '')
    estado = request.GET.get('states', '')
    tipo = request.GET.get('tipo', '')
    
    if tipo and tipo != '1': 
        animais = animais.filter(tipo=tipo)

    if estado and estado != 'TD':
        animais = animais.filter(user__estado=estado)

    if pesquisa:
        animais = animais.filter(raca__icontains=pesquisa)

    paginator = Paginator(animais, 4)
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

    return render(request, 'meus_animais.html',  context)

@login_required(login_url=reverse_lazy('user:entrar'))
def excluir_conta(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Conta Deletada com sucesso.')
        return redirect('user:entrar')

    return render(request, 'excluir_conta.html', {'user': user})

def sair_tela(request):
    return render(request, 'sair.html')
