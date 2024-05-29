aposta = [10,19,44,55,101,42]
sorteados = [13,44,99,10,82,45]

def checar(aposta: list[int], sorteados: list[int]):
    ''''''

    acertos = []

    if aposta in sorteados:
        acertos.append(aposta[0])
    if aposta[1] in sorteados:
       acertos.append(aposta[1])
    if aposta[2] in sorteados:
       acertos.append(aposta[2])
    if aposta[3] in sorteados:
       acertos.append(aposta[3])
    if aposta[4] in sorteados:
       acertos.append(aposta[4])
    if aposta[5] in sorteados:
       acertos.append(aposta[5])

    print(acertos)

checar(aposta, sorteados)


def indice(aposta: list[int], sorteados: list[int]):
    ''''''

    numeros = []

    for num in aposta:
        if num in sorteados:
            numeros.append(num)

    return numeros

print(indice([10,41,22,49,101,23], [14,10,99,22,932,111]))


def retur(aposta: list[int], sorteados: list[int]):
    ''''''

    return [num for num in aposta if num in sorteados]

print(retur([10,41,22,49,101,23], [14,10,99,22,932,111]))