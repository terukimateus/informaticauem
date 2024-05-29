def velho (idade: int) ->bool:
    '''
    Recebe a **idade** de uma pessoa e devolve True 
    se ela é super centenária ou False caso contrário

    Exemplos:
    >>> velho(112)
    True
    >>> velho(78)
    False
    '''  
   
    return idade >= 110

print(velho(112))