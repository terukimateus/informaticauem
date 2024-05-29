def indice(lista: list[int], x: int) -> int:
    '''
    >>> indice([10,15,30,5], 5)
    3

    >>> indice([121,32,1001,159], 32) 
    1

    >>> indice([100], 100)
    0

    >>> indice([0,50,22,100,1500], 32)
    

    '''
    if len(lista) == 1:
        if x == lista[0]:
            return 0
        return None
        
    if lista[-1] != x:
        return indice(lista[:-1], x)
    return len(lista) - 1