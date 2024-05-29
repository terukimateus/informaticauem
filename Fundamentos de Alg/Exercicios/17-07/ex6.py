def unity_checker (number: int) ->int:
    '''
    Recebe um número e retorna a unidade dele.

    Exemplo
    >>> unity_checker(152)
    2
    '''
    print(number % 10)

unity_checker(152)

def dezena_checker (number: int) ->int:
    '''
    Recebe um número e retorna a dezena dele.

    Exemplo
    >>> unity_checker(152)
    5
    '''
    unidade = number % 10
    numero = (number - unidade) / 10
    numero_int = round(numero)
    print(numero_int % 10)

dezena_checker(152)

def centena_chck (number: int) ->int:
    '''
    Recebe um número e retorna a dezena dele.

    Exemplo
    >>> unity_checker(152)
    5
    '''
    dezena = number % 10
    numero = (number - dezena)/10
    centena = numero/10
    centena = int(centena)
    print(centena)


centena_chck(152)
