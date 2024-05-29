def multiplica_matriz(matriz: list[list], multiplicador: int) -> list[list]:
    '''
    Recebe uma matriz e um multiplicador e multiplica todos os elementos da lista pelo multiplicador

    >>> multiplica_matriz([[0,1,2],[3,3,3]],2)
    [[0, 2, 4], [6, 6, 6]]

    >>> multiplica_matriz([[10,15,25], [30,50,100]],3)
    [[30, 45, 75], [90, 150, 300]]

    '''
    for num in range(len(matriz)):
        for j in range(len(matriz[num])):
            matriz[num][j] *= multiplicador
     
    return matriz
