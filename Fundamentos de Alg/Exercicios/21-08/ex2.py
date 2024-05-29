def digitos(n: int) -> int:
    '''
    Recebe um número N e devolve quantos dígitos ele possui, sem converter para str.

    Exemplo:

    >>> digitos(10)
    2
    
    >>> digitos(333)
    3

    >>> digitos(15000)
    5

    '''
    digitos = 1

    while(n >= 10):
        n = n / 10
        digitos += 1

    return digitos
            


print(digitos(0))
