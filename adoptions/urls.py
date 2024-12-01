from django.urls import path
from . import views

app_name = 'adoptions'

urlpatterns = [
    path('animal/<int:id>', views.animal, name='animal'),
    path('toggle_favorite/<int:animal_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('todos/', views.todos, name='todos'),
]
