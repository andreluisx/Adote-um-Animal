from django.shortcuts import render
from adoptions.models import Animal
# Create your views here.

def home(request):
    animals = Animal.objects.all().order_by('-id')[:3]
    return render(request, 'home.html', {'animals': animals})