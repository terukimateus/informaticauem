def pitagoras (num1: float, num2: float) -> float:
    '''Recebe dois números, dois catetos e retorna a hipotenusa.
    num1 ** 2 + num2 ** 2 = h2 ** 0.5

    Obs: sempre será limitado o resultado em 3 casas decimais.


    Exemplos 
    >>> pitagoras(5, 2)
    5.385
    '''
    hipotenusa = num1 ** 2 + num2 ** 2
    hip = hipotenusa ** 0.5
    hip = round(hip, 3)

    return hip

print(pitagoras(5,2))