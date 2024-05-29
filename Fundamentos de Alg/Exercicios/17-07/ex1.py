def atualiza (salario_atual: float) -> float:

    ''' 
    Recebe o salário atual e devolve o salário atualizado, isto é
    salario_atual *1.05 
    Exemplos: 

    >>> atualiza(100.0)
    105.0
    >>> atualiza(50.0)
    52.5

    '''
    print(__name__)
    return salario_atual * 1.05


    def main():
        print(atualiza(10.0))



    if __name__ == '__main__':
        main()
