def salario () -> str:
    '''
    Recebe o valor ganho por hora e o número de horas trabalhadas no mês e calcula o seu salário com impostos.

    Exemplo:
    >>> salario(6,176)
    '+ Salário Bruto : 1056 R$
    - IR (11%) : 116.16 R$
    - INSS (8%) : 84.48 R$
    - Sindicato (5%) : 52.80 R$
    = Salário Liquido : 802.56 R$'

    '''

    salario = input("Quantos reais você recebe por hora trabalhada? Digite somente números.")
    horas = input('Quantas horas você trabalhou no mês? Somente números.')
    
    sal_bruto = int(salario) * int(horas)

    ir = sal_bruto * 0.11

    inss = sal_bruto * 0.08
    sind = sal_bruto * 0.05

    descontos = ir + inss + sind

    sal_liquido = sal_bruto - descontos
    print(f'+ Salário Bruto : {sal_bruto} R$' )
    print(f'- IR (11%) : {ir} R$')
    print(f'- INSS (8%) : {inss} R$')
    print(f'- Sindicato (5%) : {sind:.2f} R$')
    print(f'= Salário Líquido : {sal_liquido} R$')

salario()