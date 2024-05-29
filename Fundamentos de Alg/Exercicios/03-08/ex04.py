arranjo = [-1,5,10,-10,15]


def positivo_negativo(arranjo: list):
    ''''''
    positivo = 0
    negativo = 0
    for num in arranjo:
        if num < 0:
            negativo = negativo + 1
        else: 
            positivo = positivo + 1


    if positivo > negativo:
        print('Positivo')
    else:
        print('Negativo')
    
positivo_negativo(arranjo)