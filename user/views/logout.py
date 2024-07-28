from django.shortcuts import redirect
from django.contrib import messages
from user.utils.ValidationError import*
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('user:entrar')
