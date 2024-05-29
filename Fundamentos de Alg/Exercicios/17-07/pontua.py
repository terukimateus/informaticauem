def ponto(s: str) -> str:
    '''

    Exemplos: 

    >>> ponto('casa')
    'casa.'

    >>> ponto('')
    ''

    >>> ponto('casa.')
    'casa.'
    '''

    if s == "":
        return s
    elif s[-1] == ".":
        return s
    else:
        return s + "."