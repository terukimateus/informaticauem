from soma import soma

def perfeito(numero: int) -> bool:
    '''
    Retorna verdadeiro se ** numero ** é perfeito, isto é, se a soma de seus divisores (exceto ele mesmo) é igual a **numero**

    >>> perfeito(28)
    True
    >>> perfeito(6)
    True
    >>> perfeito(7)
    False
    '''
    lista = []

    for i in range(1, (numero//2) + 1):
        if numero % i == 0:
            lista.append(i)

    return soma(lista) == numero
