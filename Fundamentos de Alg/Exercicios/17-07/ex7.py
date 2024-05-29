def name_checker (name: str) ->bool:
    '''
    Recebe o nome da pessoa e verifica se é Paula

    Exemplo
    >>> name_checker('Paula')
    True
    >>> name_checker('Beatriz')
    False
    '''
    if name == 'Paula':
        return True
    else:
        return False
    
print(name_checker('Lucas'))