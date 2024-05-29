from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Votos(Enum):
    branco =  auto()
    candidato1 =  auto()
    candidato2 = auto()

votos = [Votos.candidato1, Votos.candidato2, Votos.candidato1, Votos.candidato2, Votos.candidato2, Votos.branco]


def eleicao(votos: list[Votos]):
    '''
    Recebe a quantidade de votos para Candidato 1, Candidato 2 ou Nulo, e devolve o vencedor ou no caso de 50% dos votos forem nulos refazer as eleições

    Exemplo:

    >>> eleicao(Votos(14,100,120))
    candidato2

    >>> eleicao(Votos(100,200,89))
    candidato1

    '''

    candidato1 = 0
    candidato2 = 0
    branco = 0
    
    for i in votos:
        print(i)
        if i.value == Votos.candidato1:
            candidato1 += 1
        elif i.value == Votos.candidato2:
            candidato2 += 1
        else: 
            branco += 1

    print(candidato1)
    print(candidato2)

    if candidato1 > candidato2 > branco:
        return Votos.candidato1
    elif candidato2 > candidato1 > branco:
        return Votos.candidato2
    else:
        return Votos.branco    
    
print(eleicao(votos))