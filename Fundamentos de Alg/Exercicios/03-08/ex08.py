def valores (valores: list[int]) -> list:
    '''
    Recebe uma lista com valores e remove os valores incorretos(negativos) da lista.

    >>> valores([2,-1,10,-15,20])
    [2, 10, 20]

    >>> valores([-100,120,-1000,0,50])
    [120, 0, 50]
    '''

    for num in valores:
        if num < 0:
            valores.remove(num)
        
    return valores