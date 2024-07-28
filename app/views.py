from django.shortcuts import render, get_object_or_404
from adoptions.models import Animal
from user.models import User
# Create your views here.

def home(request):
    animals = Animal.objects.all().order_by('-id')[:3]
    return render(request, 'home.html', {'animals': animals})

def minha_conta(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'meus_dados.html', {'user': user})

def favoritos(request, id):
    animais = Animal.objects.all()
    return render(request, 'favoritos.html', {'animais': animais})

def meus_animais(request, id):
    animais = Animal.objects.all().filter(user=request.user)
    return render(request, 'meus_animais.html', {'animais': animais})