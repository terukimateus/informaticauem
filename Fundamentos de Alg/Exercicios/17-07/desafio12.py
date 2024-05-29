def comparador (x: float, y: float) -> str:
    '''
    Devolve o máximo entre dois inteiros x e y.

    Exemplo
    >>> 
    '''

    if x > y:
        return x
    else:
        return y

def maximo3 (x: float, y: float, z: float) -> float:
    '''
    Devolve o máximo entre três números, x y e z.

    Exemplo

    >>> maximo3(3,9,12)
    12

    >>> maximo3(15,20,12)
    20

    >>> maximo3(32,15,22)
    32
    '''

    if x > y:
        if x > z:
            return x
        else:
            return z
    if y > x:
        if y > z:
            return y
        else:
            return z
        

def maximos (x: float, y: float, z: float) -> float:
    '''
    Devolve o máximo entre três números, x y e z.

    Exemplo

    >>> maximo3(3,9,12)
    12

    >>> maximo3(15,20,12)
    20

    >>> maximo3(32,15,22)
    32
    '''

    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
def versao3 (x: float, y: float, z: float) -> float:
    '''
    Devolve o máximo entre três números, x y e z.

    Exemplo

    >>> maximo3(3,9,12)
    12

    >>> maximo3(15,20,12)
    20

    >>> maximo3(32,15,22)
    32
    '''
    if x > y:
        return comparador(x,z)
    else:
        return comparador(y,z)
    
    