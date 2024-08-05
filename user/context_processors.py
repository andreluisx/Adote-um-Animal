from django.contrib.auth.models import AnonymousUser

def auth_user(request):
    return {'auth_user': request.user if request.user.is_authenticated else AnonymousUser()}

#metodo pra verificar se ta logado em todas as telas