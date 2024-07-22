from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('entrar/', views.login, name='entrar'),
    path('sair/', views.logout, name='sair'),
    path('registro/', views.register, name='registro')
]
