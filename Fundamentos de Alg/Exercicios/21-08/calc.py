from enum import Enum


def soma(n1: float, n2: float) -> float:
    return n1 + n2

def subtracao(n1: float, n2: float) -> float:
    return n1 - n2

def mult(n1: float, n2: float) -> float:
    return n1 * n2

def divisao(n1: float, n2: float) -> float:
    return n1 / n2

class Opcao(Enum):
    SOMA = 1
    SUBTRAIR = 2
    MULTIPLICAR = 3
    DIVIDIR = 4
    SAIR = 0

def exibe_menu() -> int:
    while True:
        print('Selecione uma das opções: ')
        print(Opcao.SAIR.value, '- Sair')
        print(Opcao.SOMA.value, '- Somar')
        print(Opcao.SUBTRAIR.value, '- Subtrair')
        print(Opcao.MULTIPLICAR.value, '- Multiplicar')
        print(Opcao.DIVIDIR.value, '- Dividir')
        opcao = int(input('Opção: '))
        
        if opcao == Opcao.SAIR.value:
            return Opcao.SAIR
        elif opcao == Opcao.SOMA.value:
            return Opcao.SOMA
        elif opcao == Opcao.SUBTRAIR.value:
            return Opcao.SUBTRAIR
        elif opcao == Opcao.MULTIPLICAR.value:
            return Opcao.MULTIPLICAR
        elif opcao == Opcao.DIVIDIR.value:
            return Opcao.DIVIDIR
        else:
            print('Erro: Opção inválida')

opcao = exibe_menu()

while opcao.value != Opcao.SAIR.value:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if opcao.value == Opcao.SOMA.value:
        print('Resultado: ', soma(n1, n2))
    elif opcao.value == Opcao.SUBTRAIR.value:
        print('Resultado: ', subtracao(n1, n2))
    elif opcao.value == Opcao.MULTIPLICAR.value:
        print('Resultado: ', mult(n1, n2))
    elif opcao.value == Opcao.DIVIDIR.value:
        print('Resultado: ',divisao(n1,n2))

    opcao = exibe_menu()