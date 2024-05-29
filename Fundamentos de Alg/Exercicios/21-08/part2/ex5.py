def intercala(A: list[int], B: list[int]) -> list[int]:
    '''
    Recebe as listas **A** e **B** de números inteiros em ordem crescente e produz a
    intercalação de todos os elementos das duas listas mantendo-se a ordem.

    Exemplos:
    >>> intercala([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> intercala([2, 4, 6], [1, 3, 5])
    [1, 2, 3, 4, 5, 6]
    >>> intercala([1, 5, 6], [2, 3, 4, 7])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    i = 0 
    j = 0
    resultado = []

    for __ in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] > B[j]:
                resultado.append(B[j])
                j += 1
            else:
                resultado.append(A[i])
                i += 1
        elif i < len(A):
            resultado.append(A[i])
        else:
            resultado.append(B[j])
    return resultado

print(intercala([2, 4, 6], [1, 3, 5]))