from dataclasses import dataclass
from enum import Enum, auto


class Tipo(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

@dataclass
class Produto:
    nome: Tipo
    quant: int

def vendas_mes(pedidos: list[Produto]) -> list[Produto]:
    ''''
    Os pedidos serão processados e formarão uma nova lista
    com a quantidade de vendas de cada produto.

    >>> vendas_mes([Produto(Tipo.BOBINA, 100), Produto(Tipo.CHAPA, 40), Produto(Tipo.BOBINA, 50)])
    [Produto(nome=<Tipo.BOBINA: 1>, quant=150), Produto(nome=<Tipo.CHAPA: 2>, quant=40), Produto(nome=<Tipo.PAINEL: 3>, quant=0)]

    '''
    
    quant_bobina = 0
    quant_chapa = 0
    quant_painel = 0

    for pedido in pedidos:
        if pedido.nome == Tipo.BOBINA:
            quant_bobina += pedido.quant
        elif pedido.nome == Tipo.CHAPA:
            quant_chapa += pedido.quant
        elif pedido.nome == Tipo.PAINEL:
            quant_painel += pedido.quant
    
    list = [Produto(Tipo.BOBINA, quant_bobina), Produto(Tipo.CHAPA, quant_chapa), Produto(Tipo.PAINEL, quant_painel)]
    return list


def ha_ruptura(estoque: list[Produto], demanda: list[Produto]) -> bool:

    '''
    Devolve verdadeiro se o estoque de um produto é
    insuficiente para cobrir sua demanda; devolve falso caso
    contrário.

    >>> ha_ruptura([Produto(Tipo.BOBINA, 150), Produto(Tipo.CHAPA, 50), Produto(Tipo.PAINEL, 100)], [Produto(Tipo.BOBINA, 100), Produto(Tipo.BOBINA, 49)])
    False
    '''
    pedido = vendas_mes(demanda)
    
    for pedido in demanda:
       for estoqu in estoque:
           if pedido.nome == Tipo.BOBINA and estoqu.nome == Tipo.BOBINA:
               if pedido.quant > estoqu.quant:
                   return True
           elif pedido.nome == Tipo.CHAPA and estoqu.nome == Tipo.CHAPA:
               if pedido.quant > estoqu.quant:
                   return True
           elif pedido.nome == Tipo.PAINEL and estoqu.nome == Tipo.PAINEL:
               if pedido.quant > estoqu.quant:
                   return True 
    return False 