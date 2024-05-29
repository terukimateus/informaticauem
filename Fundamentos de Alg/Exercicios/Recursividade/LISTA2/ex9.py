def palindromo(palvra: str) -> bool:
    '''
    >>> palindromo('rapar')
    True

    >>> palindromo('reviver')
    True

    >>> palindromo('barata')
    False

    >>> palindromo('arara')
    True
    
    '''
    if len(palvra) == 1:
        return True
    if palvra[0] == palvra[-1]:
        return palindromo(palvra[1:-1])
    return False

print(palindromo('ararara'))