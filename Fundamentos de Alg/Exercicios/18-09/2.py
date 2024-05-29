def soma_matriz(m1: list[list], m2: list[list]) -> list[list]:
    '''
    Recebe duas matrizes e retorna a soma dessas duas matrizes.

    
    >>> soma_matriz([[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]])
    [[6, 8, 10], [12, 14, 16]]

    >>> soma_matriz([[10,100,15],[20,30,40]],[[20,30,50],[100,200,300]])
    [[30, 130, 65], [120, 230, 340]]
    '''
    m3 = []
    for num in range(len(m1)):
        linha = []
        for i in range(len(m1[num])):
            linha.append(m1[num][i] + m2[num][i])
        m3.append(linha)

    return m3