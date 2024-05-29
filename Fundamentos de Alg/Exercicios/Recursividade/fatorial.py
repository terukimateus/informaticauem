def fatorial(num: int) -> int:
    '''
    Calcula o fatorial de um número natural **num**.
    Exemplos:
    >>> fatorial(4) # 4! = 4*3*2*1 = 24
    24
    >>> fatorial(5) # 5! = 5*4*3*2*1 = 120
    120
    >>> fatorial(0) # 0! = 1 (definição)
    1
    '''
    if num == 0:
        return 1
    else:
        n = num * (num - 1)
        return n + (fatorial(n-1))
print(fatorial(1))