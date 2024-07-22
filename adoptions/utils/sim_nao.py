from enum import Enum

class CustomerChoice(Enum):
  SIM = 'Sim'
  NAO = 'Não'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
  