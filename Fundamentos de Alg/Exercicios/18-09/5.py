def matriz_simetrica(matriz: list[list]) -> bool:
    '''
    Uma matriz simétrica é uma matriz que qualquer elemento dela inverso tem o mesmo valor
    

    >>> matriz_simetrica([[5,1,2],[1,6,3],[2,3,8]])
    True

    >>> matriz_simetrica([[-3,0,7],[0,5,-1],[7,-1,4]])
    True

    >>> matriz_simetrica([[0,0,1],[0,5,3],[1,2,3]])
    False
    '''

    for i in range(len(matriz)):
        for num in range(len(matriz[i])):
            if matriz[i][num] == matriz[num][i]:
                pass
            else:
                return False
    return True

