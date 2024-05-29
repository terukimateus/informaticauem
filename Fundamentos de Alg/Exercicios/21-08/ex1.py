def divisores(num1: int, num2: int) -> list[int]:
    '''
    Identifica todos os inteiros no intervalo aberto definido por **num1** e **num2**, tal que
    esse inteiro dividido por 5 possui resto 2 ou resto 3. Os números **num1** e **num2** são
    inteiros positivos, mas não necessariamente **num1** < **num2**.

    Exemplos:
    >>> divisores(10, 18)
    [12, 13, 17]
    >>> divisores(9, 7)
    [8]
    >>> divisores(25, 26)
    []
    '''

    lista = []
    numeros = 0
    lista_divisores = []

    if num1 > num2:
        numeros = num1 - num2
        for num in range(numeros):
            if num != 0:
                num += num2
                lista.append(num)
    else:
        numeros = num2 - num1
        for num in range(numeros):
            if num != 0:
                num += num1
                lista.append(num)

    for i in lista:
        if (i % 5) == 2 or (i % 5) == 3:
            lista_divisores.append(i)
        
    return lista_divisores
