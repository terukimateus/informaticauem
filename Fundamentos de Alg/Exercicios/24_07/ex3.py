
def faz_bolo(T: int, O: int, L: int):
    '''
    >>> faz_bolo(0,10,5)
    0
    >>> faz_bolo(15,10,5)
    1
    >>> faz_bolo(4,6,10)
    2
    
    '''

    NT = T // 2
    NO = O // 3
    NL = L // 5


    if NT <= NO and NT <= NL:
        return NT
    elif NO <= NT and NO <= NL:
        return NO
    else:
        return NL
    
