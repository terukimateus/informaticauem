def conversor_data(data = str) ->str:
    '''
    Recebe a data em DIA / MÊS / ANO e retorna em ANO / MÊS / DIA

    Exemplos
    >>> conversor_data("05/11/2004")
    "2004/11/05"

    '''
    dia = data[:2]
    mes = data[3:5]
    ano = data[6:10]
    
    return(f"{ano}/{mes}/{dia}")
    
print(conversor_data("23/11/2004"))