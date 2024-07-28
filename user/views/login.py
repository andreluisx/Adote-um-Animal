from django.shortcuts import render, redirect
from django.contrib import messages
from user.utils.ValidationError import*
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    wrongpass = None
    if request.method == 'GET':
        return render(request, 'login.html', {'wrongpass': wrongpass})
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('app:home')
        else:
            wrongpass = True
            messages.error(request, 'Credenciais inválidas.')
            return render(request, 'login.html', {'wrongpass': wrongpass, 'email': email})
