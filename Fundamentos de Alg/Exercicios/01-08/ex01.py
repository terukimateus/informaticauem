from dataclasses import dataclass
from enum import Enum, auto


@dataclass

class Numeros:
    N1: int
    N2: int
    N3: int
    N4: int
    N5: int
    N6: int
def checar_numeros(aposta: Numeros, sorteados: Numeros) -> int:
    '''
    Recebe o números sorteados e apostados e devolve quais números você acertou.

    Exemplo
    >>> checar_numeros(Numeros(14,20,10,55,100,44), Numeros(4,14,55,99,22,32))
    2
    '''

    acertos = 0

    if aposta.N1 == sorteados.N1 or aposta.N1 == sorteados.N2 or aposta.N1 == sorteados.N3 or aposta.N1 == sorteados.N4 or aposta.N1 == sorteados.N5 or aposta.N1 == sorteados.N6:
        acertos = acertos + 1
    if aposta.N2 == sorteados.N1 or aposta.N2 == sorteados.N2 or aposta.N2 == sorteados.N3 or aposta.N2 == sorteados.N4 or aposta.N2== sorteados.N5 or aposta.N2 == sorteados.N6:
        acertos = acertos + 1
    if aposta.N3 == sorteados.N1 or aposta.N3 == sorteados.N2 or aposta.N3 == sorteados.N3 or aposta.N3 == sorteados.N4 or aposta.N3 == sorteados.N5 or aposta.N3 == sorteados.N6:
        acertos = acertos + 1
    if aposta.N4 == sorteados.N1 or aposta.N4 == sorteados.N2 or aposta.N4 == sorteados.N3 or aposta.N4 == sorteados.N4 or aposta.N4 == sorteados.N5 or aposta.N4 == sorteados.N6:
        acertos = acertos + 1
    if aposta.N5 == sorteados.N1 or aposta.N5 == sorteados.N2 or aposta.N5 == sorteados.N3 or aposta.N5 == sorteados.N4 or aposta.N5 == sorteados.N5 or aposta.N5 == sorteados.N6:
        acertos = acertos + 1
    if aposta.N6 == sorteados.N6 or aposta.N6 == sorteados.N6 or aposta.N6 == sorteados.N3 or aposta.N6 == sorteados.N4 or aposta.N6 == sorteados.N5 or aposta.N6 == sorteados.N6:
        acertos = acertos + 1
    
    print(acertos)
    
checar_numeros(Numeros(55,14,99,101,49,22), Numeros(13,55,11,99,3,22))

