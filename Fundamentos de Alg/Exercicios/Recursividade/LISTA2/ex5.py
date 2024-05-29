def negativo(lista: list[int]) -> list[int]:
    '''
    >>> negativo([10,-100,15])
    [10, 15]
    '''

    if len(lista) == 0:
        return []
        
    if lista[0] >= 0:
        return [lista[0]] + negativo(lista[1:])
    return negativo(lista[1:])

