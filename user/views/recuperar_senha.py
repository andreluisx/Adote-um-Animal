from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import User
from django.conf import settings
from user.utils.ValidationError import*
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from core.models import Token

def recuperar_senha(request):
    if request.method == 'GET':
        return render(request, 'recuperar_senha.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            token = Token.objects.create(user=user)
            token_str = str(token.token)
            reset_url = f"http://127.0.0.1:8000/usuario/alterando_senha/{user.id}/{token_str}/"
            html_content = render_to_string('emails/senha.html', {'user': user, 'reset_url': reset_url})
            text_content = strip_tags(html_content)

            send_email = EmailMultiAlternatives(
                'Recuperação de Senha', 
                text_content,
                settings.EMAIL_HOST_USER,
                [email]
            )

            send_email.attach_alternative(html_content, 'text/html')
            send_email.send()
            messages.success(request, 'Email enviado com sucesso.')
            return redirect('user:recuperar_senha')
        else:
            messages.error(request, 'Este email não está cadastrado.')
            return redirect('user:recuperar_senha')
        
    return render(request, 'recuperar_senha.html')
