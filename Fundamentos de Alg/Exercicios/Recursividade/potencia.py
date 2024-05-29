def potencia(x: int, k: int) -> int:
    '''
    Calcula o valor de **x** elevado a **k**, sendo **x** e **k**
    números naturais.
    Exemplos:
    >>> potencia(5, 2)
    25
    >>> potencia(9, 3)
    729
    >>> potencia(0, 10)
    0
    >>> potencia(10, 0)
    1
    '''
    if k == 0:
        return 1
    if k == 1:
        return x
    return (x * x) * potencia(x, k-2)
