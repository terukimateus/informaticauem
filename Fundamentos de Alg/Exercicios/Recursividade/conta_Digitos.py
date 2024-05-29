def conta_digitos(num: int) -> int:
    '''
    Devolve a quantidade de dígitos do número natural **num**. 

    Exemplos:
    >>> conta_digitos(101)
    3
    >>> conta_digitos(123456789)
    9
    >>> conta_digitos(0)
    1
    '''

    if num < 10:
        return 1
    return 1 + conta_digitos(num/10)