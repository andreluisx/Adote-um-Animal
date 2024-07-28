from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import User
from core.models import Token
from django.utils import timezone

def alterando_senha(request, id, token):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            token_obj = Token.objects.get(token=token, user=user)

            if not token_obj.is_valid():
                messages.error(request, 'Este link de redefinição de senha expirou.')
                return redirect('user:recuperar_senha')

            return render(request, 'alterando_senha.html', {'user': user, 'token': token})

        except (User.DoesNotExist, Token.DoesNotExist):
            messages.error(request, 'Link inválido.')
            return redirect('user:recuperar_senha')

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return redirect(request.path)

        try:
            user = User.objects.get(id=id)
            token_obj = Token.objects.get(token=token, user=user)

            if not token_obj.is_valid():
                messages.error(request, 'Este link de redefinição de senha expirou.')
                return redirect('user:recuperar_senha')

            user.set_password(password)
            user.save()
            token_obj.delete()

            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('user:entrar')

        except (User.DoesNotExist, Token.DoesNotExist):
            messages.error(request, 'Link inválido.')
            return redirect('user:recuperar_senha')

    return render(request, 'alterando_senha.html')
