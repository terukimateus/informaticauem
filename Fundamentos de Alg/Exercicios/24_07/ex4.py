
def salario(salario: float):
    '''
    Recebe o salário do funcionário e repasse com reajuste de acordo com a seguinte tabela:
    Salário Percentual de Reajuste
    0 - 400.00 15%
    400.01 - 800.00 12%
    800.01 - 1200.00 10%
    1200.01 - 2000.00 7%
    Acima de 2000.00 4%

    Exemplos:

    >>> salario(400)
    460.0
    >>> salario(1200)
    1320.0

    >>> salario(2000)
    2080.0
    '''

    if salario <= 400:
        calcular_reajuste(salario,0.15)
    elif salario <= 800:
        calcular_reajuste(salario,0.12)
    elif salario <= 1200:
        calcular_reajuste(salario,0.1)
    elif salario <= 2000:
        calcular_reajuste(salario,0.07)
    else:
        calcular_reajuste(salario,0.04)

def calcular_reajuste(salario: float, reajuste: float):
    ''''''
    aumento = salario * reajuste
    salario = salario + aumento

    print(f'Seu novo salário é {salario}R$, seu  valor de reajuste foi {aumento}R$')

salario(450)

salario(1000)

salario(3000)