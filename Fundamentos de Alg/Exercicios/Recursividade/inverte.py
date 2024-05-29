def inverte(palavra: str) -> str:
    '''
    Inverte a string em **palavra**.

    Exemplos:
    >>> inverte('abracadabra')
    'arbadacarba'
    >>> inverte('ola mundo')
    'odnum alo'
    >>> inverte('arara')
    'arara'
    '''

    if len(palavra) == 0:
        return ''
    return palavra[-1] + inverte(palavra[:-1])