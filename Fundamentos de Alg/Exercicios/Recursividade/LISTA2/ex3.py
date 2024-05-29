def pares(arranjo: list[int]):
    '''
    >>> pares([22, 29, 32, 100])
    False

    >>> pares([100,22,40,2])
    True

    >>> pares([2,3,10,50,100])
    False
    
    '''

    if len(arranjo) == 1:
        if arranjo[0] % 2 == 0:
            return True
        return False
    
    if arranjo[-1] % 2 == 0:
        return pares(arranjo[:-1])
    return False