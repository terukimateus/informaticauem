import math

def renova_estoque(estoque: int, vendas:int) -> int:
    '''
    Contabiliza o giro de estoque, basicamente quantas vezes o estoque foi vendido e reposto completamente.

    Se o volume médio de estoque é 3 mil e foram vendidas 12 mil ao ano, quer dizer que o giro de estoque foi 4.

    >>> renova_estoque(3,12)
    4

    >>> renova_estoque(4,10)
    2

    >>> renova_estoque(4,3)
    0

    '''

    giro = vendas / estoque

    giro = math.floor(giro)


    return giro