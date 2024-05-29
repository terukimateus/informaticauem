texto = "Teste de string"
palavra = ''
lista = []
for i in range(len(texto)):
    if texto[i] == '' and len(palavra) == 0:
        lista.append(palavra)
        palavra = ''
    else:
        palavra = palavra + texto[i]
if len(palavra) != 0:
    lista.append(palavra)
    
print(lista)