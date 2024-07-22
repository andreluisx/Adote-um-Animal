from django.db import models
from .utils import gender, sim_nao
from django.db import models
from core.models import UserIndexedModel, BaseModelManager

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class AnimalManager(BaseModelManager):
    """Manager for the users"""
    pass

class Animal(UserIndexedModel):
    
    nome = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.ForeignKey(Type, on_delete=models.CASCADE)
    raca = models.CharField(max_length=200, blank=True, null=True)
    idade = models.IntegerField()
    genero = models.CharField(max_length=6, choices=gender.CustomerGender.choices())
    vacinado = models.CharField(max_length=4, choices=sim_nao.CustomerChoice.choices())
    disponivel = models.CharField(max_length=4, choices=sim_nao.CustomerChoice.choices(), default=sim_nao.CustomerChoice.SIM)
    cor = models.CharField(max_length=125, blank=True, null=True)
    descricao = models.TextField()
    mamando = models.CharField(max_length=4, choices=sim_nao.CustomerChoice.choices())

    objects = AnimalManager()

    def __str__(self):
        return str(self.nome) if self.nome else str(self.tipo)


class AnimalImage(models.Model):
    
    animal = models.ForeignKey(Animal, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='animal_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.animal.nome} - enviado em: {self.uploaded_at}'
        