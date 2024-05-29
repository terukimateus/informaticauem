def jogo_sapo(canos: list[int], pulo: int) -> bool:
    '''
    Verifica se o sapo conseguiria vencer a fase, verificando a distancia do pulo entre os canos com a altura de seu pulo

    >>> jogo_sapo([1,3],1)
    False

    >>> jogo_sapo([1,3,5,7],2)
    True

    >>> jogo_sapo([1,3,6,9,7,2,4,5,8,3],5)
    True

    >>> jogo_sapo([1,3,5,8],2)
    False
    '''
    
    for num in canos:
        posicao_n = int(canos.index(num)) + 1

        if posicao_n >= len(canos):
            return True

        if num > canos[posicao_n]:
            if (num - canos[posicao_n]) > pulo:
                return False
        else:
            if (canos[posicao_n] - num) > pulo:
                return False
    return True
        
print(jogo_sapo([1,3,5,8],2))