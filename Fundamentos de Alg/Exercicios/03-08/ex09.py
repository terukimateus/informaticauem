def primeiro_maximo (arranjo: list[int]) -> int:
    '''
    Recebe uma lista e devolve a **posição** do primeiro máximo encontrado.

    >>> primeiro_maximo([10,15,100,400])
    1

    >>> primeiro_maximo([0,4,200,100])
    1
    '''

    numero = arranjo[0]

    for num in arranjo:
        if num > numero:
            numero = num
            return arranjo.index(numero)
        
