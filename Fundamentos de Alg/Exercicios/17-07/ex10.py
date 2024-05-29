def custos_viagem () -> str:
    '''
    Recebe o custo do combustível e baseado no consumo do carro e a quilometragem da viagem, retornando o custo da viagem.

    Consumo do carro 10km/l, 100km de viagem = 100km / 10 = 10 litros
    5,37R$ o litro.
    10 * 5,37
    53,7 R$

    Exemplo

    >>> custos_viagem()
    53,7 R$

    '''
    print('Insira somente os valores em numerais.')
    combustivel = input('Qual o valor do combustível?')
    consumo = input('Qual o consumo do carro na viagem?')
    quilometragem = input('Qual foi a quilometragem do trajeto?')

    c_gasto = float(quilometragem) / float(consumo)
    valor = float(c_gasto) * float(combustivel)
    valor = round(valor, 2)

    print(f'{valor}R$')

custos_viagem()