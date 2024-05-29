def conversor_centimetros(medida: float) ->float:
    '''
    Recebe a **medida** em polegadas e retorna em centimetros, isto é medida * 2.54

    Exemplos:
    >>> conversor_centimetros(10.0)
    25.4
    >>> conversor_centimetros(20.0)
    50.8

    '''

    return medida * 2.54

def conversor_polegadas(medida: float) ->float:
    '''
    Recebe a **medida** em centimetros e retorna em polegadas, isto é medida / 2.54

    Exemplos:
    >>> conversor_centimetros(25.4)
    10.0
    >>> conversor_centimetros(50.8)
    20.0

    '''

    return medida / 2.54

print(conversor_centimetros(10.0))

print(conversor_polegadas(25.4))