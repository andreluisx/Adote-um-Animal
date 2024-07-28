from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('entrar/', views.login, name='entrar'),
    path('sair/', views.logout, name='sair'),
    path('registro/', views.register, name='registro'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
    path("alterando_senha/<str:id>/<str:token>/", views.alterando_senha, name="alterando_senha")
]
