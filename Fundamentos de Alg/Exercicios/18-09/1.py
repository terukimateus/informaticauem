def matriz(matriz: list[list], indice: int) -> list[int]:
    '''
    Recebe uma matriz e retorna os números de uma coluna baseada em um índice.

    >>> matriz([[0,1,2],[3,4,5],[6,7,8]],2)
    [2, 5, 8]

    >>> matriz([[7,8,9],[12,13,14],[20,21,22],[103,102,100]],1)
    [8, 13, 21, 102]


    '''

    lista = []
    for j in range(len(matriz)):
        lista.append(matriz[j][indice])
    return lista