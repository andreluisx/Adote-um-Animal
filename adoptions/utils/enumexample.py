from enum import Enum

class CustomerConditions(Enum):
  APT_FOR_SLAUGHTER = 'Apto para o abate'
  SICK_OR_INJURED = 'Doente ou machucado'
  WRONG_BATCH = 'Animal está no lote errado'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
  