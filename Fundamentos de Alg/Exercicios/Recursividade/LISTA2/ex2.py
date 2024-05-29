def maximo(lista: list[int]) -> int:
    '''
    >>> maximo([22, 29, 37, 59])
    59

    >>> maximo([31,76,99,2])
    99

    >>> maximo([43,87,31,50])
    87
    
    '''
    if len(lista) == 1:
        return lista[0]
    if lista[-1] < lista[-2]:
        return maximo(lista[:-1])
    lista.remove(lista[-2])
    return maximo(lista)


def maximo2(lista: list[int]) -> int:
    '''
    >>> maximo([22, 29, 37, 59])
    59

    >>> maximo([31,76,99,2])
    99

    >>> maximo([43,87,31,50])
    87
    
    '''

    if len(lista) == 1:
        return lista[0]
    
    if lista[-1] > maximo(lista[-1]):
        return lista[-1]
    return maximo(lista[:-1])