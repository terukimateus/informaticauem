def indica_combustivel (alcool: float, gasolina: float) -> str:
    '''
    Exemplos:

    >>> indica_combustivel(4.200,6.000)
    'alcool'

    >>> indica_combustivel(4.000,6.000)
    'alcool'

    >>> indica_combustivel(4.000,5.000)
    'gasolina'
    '''
    
    if alcool <= gasolina * 0.7:
        return 'alcool'
    return 'gasolina'