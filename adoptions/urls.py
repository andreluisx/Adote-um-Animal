from django.urls import path
from . import views

app_name = 'adoptions'

urlpatterns = [
    path('animal/<int:id>', views.animal, name='animal'),
    path('todos/', views.todos, name='todos'),
]
