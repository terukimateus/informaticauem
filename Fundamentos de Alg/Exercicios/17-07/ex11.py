def azulejos (comp: int, altura: int) ->bool:
    '''
    Recebe a altura e comprimento de uma parede, calcula sua área fazendo altura x comprimento e calcula quanto um azulejo com 0,04m quadrados é necessário para azulejar a parede.

    4 metros de altura x 2 metros de comprimento = 8m2 / 0,04m2

    Exemplo 
    >>> azulejos(2,4)
    200

    >>> azulejos(6,3)
    450

    '''

    parede = altura * comp
    return int(parede / 0.04)

print(azulejos(2,4))

print(azulejos(6,3))

    
