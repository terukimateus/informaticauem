def lista_rep(lista: list[int]) -> list:
    ''''''

    listas = []

    for num in lista:
        if num not in listas:
            listas.append(num)
            
    return listas

print(lista_rep([1,1,2,3,4,4]))