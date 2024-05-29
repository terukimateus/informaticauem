def dois_inteiros(lista: list[int], k: int) -> bool:
    ''''''
    for num in range(len(lista)-1):
        for i in range(num+1, len(lista)):
            if (lista[num] + lista[i]) == k:
                return True
   
    return False
            
print(dois_inteiros([1,3,7],6))