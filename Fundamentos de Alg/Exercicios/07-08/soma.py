
def soma(lista: list[int]) -> int:
    '''
    Calcula a soma de todos os inteiros em **lista**

    >>> soma([1,2,3,4,5,6,7])
    28

    >>> soma([-10,20,5,-15,-20,20,7])
    7
    '''
    soma = 0
    

    for num in lista:
        soma += num
    return soma


def main():
    lista = []
    for i in range(7):
        numero = int(input('Digite o {}* número: '.format(i+1)))
        lista.append(numero)
    print('A soma dos números é: ', soma(lista))

if __name__ == '__main__':
    main()
