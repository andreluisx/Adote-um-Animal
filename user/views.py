from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .utils.ValidationError import*
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    if request.method == 'POST':
        name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        state = request.POST.get('state')
        city = request.POST.get('city')
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        second_password = request.POST.get('second_password')

        context={
            'first_name': name,
            'username': username,
            'email': email,
            'number': number,
            'state': state,
            'city': city,
            'cpf': cpf,
        }
        
        cpf_numeros = extract_numbers(cpf)
        celular_numeros = extract_numbers(number)

        # validações
        if not name or not second_password or not username or not email or not state or not city or not cpf or not password:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'register.html', context)

        if not validate_phone_number(number):
            messages.error(request, 'Número de telefone inválido.')
            return render(request, 'register.html', context)
        
        if not validate_cpf(cpf):
            messages.error(request, 'CPF inválido.')
            return render(request, 'register.html', context)

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email inválido.')
            return render(request, 'register.html', context)
        
        if not validate_state(state):
            messages.error(request, 'Estado inválido.')
            return render(request, 'register.html', context)

        if len(password) < 8:
            messages.error(request, 'A senha deve ter pelo menos 8 caracteres.')
            return render(request, 'register.html', context)
        
        if password != second_password:
            messages.error(request, 'As senhas tem que ser iguais.')
            return render(request, 'register.html', context)
        
        if User.objects.filter(user_name=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'register.html', context)
        
        if User.objects.filter(number=celular_numeros).exists():
            messages.error(request, 'Número já cadastrado.')
            return render(request, 'register.html', context)
        
        if User.objects.filter(cpf=cpf_numeros).exists():
            messages.error(request, 'CPF já cadastrado.')
            return render(request, 'register.html', context)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já existe.')
            return render(request, 'register.html', context)
        


        user = User(
            name=name,
            user_name=username,
            email=email,
            estado=state,
            cidade=city,
            number=celular_numeros,
            cpf=cpf_numeros, 
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Usuário registrado com sucesso!')
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credenciais inválidas.')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('/usuario/entrar')