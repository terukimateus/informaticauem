from dataclasses import dataclass

@dataclass
class Data:
    dia: int
    mes: int
    ano: int

def prev_demanda(data: Data, consumo: int, estoque: int) -> int:
    '''
    Trata-se de utilizar dados históricos e tendências para estimar a demanda futura e ajustar os níveis de estoque de acordo.
    50% maior no do mês 1 a 3 e 10 a 12
    20% menor de 4 a 6

    igual = de 7 a 9
    
    Se a quantidade em estoque for suficiente devolver zero.

    >>> prev_demanda(Data(5,11,2004), 30, 40)
    5.0

    >>> prev_demanda(Data(10,5,2023), 30, 25)
    0

    >>> prev_demanda(Data(10,8,2023), 30, 25)
    5
    
    '''

    if data.mes <= 3 or data.mes >= 10 and data.mes <=12:
        consumo += consumo * 0.5
    elif data.mes >= 4 and data.mes <= 6:
        consumo -= consumo * 0.2
    elif data.mes >= 7 and data.mes <= 9:
        consumo = consumo
    else:
        return 'Mês inválido.'
    
    quant_necessaria = 0

    if consumo > estoque:
        quant_necessaria = consumo - estoque
    else:
        return 0

    return quant_necessaria