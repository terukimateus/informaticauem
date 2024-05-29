arranjo = [1,5,3,9,4]
resultado = []

for num in arranjo:
    resultado.append(num)
    i = len(resultado) - 1
    chave = resultado[i]
    while i > 0 and resultado[i - 1] > chave:
        resultado[i] = resultado[i - 1]
        i = i -1 
    resultado[i] = chave

print(resultado)