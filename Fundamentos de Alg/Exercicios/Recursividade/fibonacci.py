def fibonacci(n: int) -> int:
    '''
    Calcula o n-ésimo número na sequência de Fibonacci (sequência em que cada número
    seguinte corresponde à soma dos dois anteriores.

    n            | 0 1 2 3 4 5 6  7  8  9 10
    fibonacci(n) | 0 1 1 2 3 5 8 13 21 34 55

    Exemplos:
    >>> fibonacci(4)
    3
    >>> fibonacci(6)
    8
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    '''
    if n == 2:
        return 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-2) + fibonacci(n-1)
