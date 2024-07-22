from enum import Enum

class CustomerGender(Enum):
  MACHO = 'Macho'
  FEMEA = 'Femêa'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
  