def matriz_identidade(matriz: list[list]) -> bool:
    '''
    Matriz identidade é uma matriz que tem todos os elementos da diagonal principal são iguais a 1 e os outros elementos igual a 0.
    Retorna true se for matriz identidade e false se não.

    >>> matriz_identidade([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) 
    True

    >>> matriz_identidade([[1,0,0],[0,1,0],[0,0,1]])
    True

    >>> matriz_identidade([[1,0],[0,1]])
    True

    >>> matriz_identidade([[0,1,0],[1,0,1],[0,0,1]])
    False
    '''
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][contador] == 1:
            contador += 1
        else:
            return False
    if contador == (len(matriz)):
        return True


def matriz_identidade_criador(dimensão: int) -> list[list]:
    ''' 
    Recebe uma dimensão n x n (exemplo: 3x3) e retorna a matriz identidade de n x n.

    >>> matriz_identidade_criador(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    >>> matriz_identidade_criador(4)
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    >>> matriz_identidade_criador(1)
    [[1]]

    >>> matriz_identidade_criador(2)
    [[1, 0], [0, 1]]
    '''

    lista = []
    for i in range(dimensão):
        linha = []
        for j in range(dimensão):
            linha.append(0)
        lista.append(linha)

    for num in range(len(lista)):
        lista[num][num] = 1

    return lista

