def soma(lista: list[int]) -> int:
    ''''''
    if len(lista) == 0:
        return 0
    return lista[-1] + soma(lista[:-1])

print(soma([1,10,20,100]))