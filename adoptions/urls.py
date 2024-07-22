from django.urls import path
from . import views

app_name = 'adoptions'

urlpatterns = [
    path('', views.all_animals, name='all_animals'),
    path('animal/<int:id>', views.animal, name='animal'),
]
