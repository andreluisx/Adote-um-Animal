from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('minha_conta/<str:id>', views.minha_conta, name='minha_conta'),
    path('favoritos/<str:id>', views.favoritos, name='favoritos'),
    path('meus_animais/<str:id>', views.meus_animais, name='meus_animais'),
]
