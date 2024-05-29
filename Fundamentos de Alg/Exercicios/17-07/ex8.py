def subname_checker (name: str) ->str:
    '''
    Recebe o nome da pessoa, nome e sobrenome e verifica se o sobrenome corresponde a Silva.

    Exemplos

    >>> subname_checker('João Silva ')
    True
    >>> subname_checker('Joao Paulo')
    False

    >>> subname_checker('Silva de OLiveira')
    False


    '''
    return ' Silva ' in name or \
        ' Silva ' == name[:-6]