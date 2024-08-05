from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('meus_dados/', views.meus_dados, name='meus_dados'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('meus_animais/', views.meus_animais, name='meus_animais'),
    path('excluir_conta/', views.excluir_conta, name='excluir_conta'),
    path('sair/', views.sair_tela, name='sair_tela'),
]
