from django.db import models
from .utils import animal_conditions
# Create your models here.
from django.db import models
from core.models import UserIndexedModel, BaseModelManager


class AnimalManager(BaseModelManager):
    """Manager for the users"""
    pass

class Animal(UserIndexedModel):
    
    identifier           = models.CharField(max_length=5, editable=True)
    animal_conditions    = models.CharField(max_length=26, choices=animal_conditions.CustomerConditions.choices(), default=animal_conditions.CustomerConditions.APT_FOR_SLAUGHTER)
    breed                = models.CharField(max_length=125)
  
    objects = AnimalManager()

    def __str__(self):
        return str(self.identifier)

