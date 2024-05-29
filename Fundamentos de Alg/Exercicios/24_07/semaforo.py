from dataclasses import dataclass
from enum import Enum, auto

@dataclass

class Cor(Enum):
    VERMELHO = auto()
    AMARELO = auto()
    VERDE = auto()



def proxima_cor(c: Cor) -> Cor:
    ''''''

    if c == Cor.VERMELHO:
        return Cor.VERDE 
    elif c == Cor.AMARELO:
        return Cor.VERMELHO
    else:
        return Cor.AMARELO 
    
proxima_cor(Cor.VERMELHO).name