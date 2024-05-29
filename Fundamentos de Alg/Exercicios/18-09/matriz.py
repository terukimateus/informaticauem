M = [[1,2,3], [4,5,6], [7,8,9]]

print(M[0][1])

lista = [[0]*4]*3
print(lista)

lista[1][0] = 8
print(lista)

m = []

for i in range(3):
    linha = []
    for j in range(4):
        linha.append(0)
    m.append(linha)

print(m)

m[1][0] = 8

print(m)