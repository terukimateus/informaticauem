def name_check(name: str) ->str:
    '''
    Recebe o nome da pessoa e verifica se é um nome curto, longo ou mediano.

    Exemplos:
    >>> name_check("Mateus")
    Mediano
    >>> name_check("Bia")
    Curto
    >>> name_check('Antonella')
    Longo
    '''
    if len(name) >= 8:
        print('Longo')
    elif len(name) <= 3:
        print('Curto')
    else:
        print('Mediano')

name_check('Antonella')