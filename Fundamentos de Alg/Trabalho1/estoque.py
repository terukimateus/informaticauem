from dataclasses import dataclass
from enum import Enum,auto

class Vendedor:
    id: int
    nome: str

class Produto(Enum):
    PAPEL = auto()
    PAPELAO = auto()
    PAINEIS = auto()

@dataclass
class Nota:
    vendedor: Vendedor
    produto: Produto
    quant: int
    valor: float


def receita(vendas: list[Nota]) -> int:
    '''
    Baseado nas vendas irá relatar a receita mensal e lucro líquido obtidos no mês.

    Produto Quantidade Preço de custo Preço de venda
    Papel   100.000    50,00          60,00
    Papelão 50.000     40,00          48,00
    Painéis 30.000     75,00          90,00
    '''

    lucro = 0
    receita = 0

    for venda in vendas:
        receita += venda.valor
        if venda.produto == Produto.PAPEL:
            lucro += venda.valor - ( 50 * venda.quant)
        elif venda.produto == Produto.PAPELAO:
            lucro += venda.valor - (40*venda.quant)
        elif venda.produto == Produto.PAINEIS:
            lucro += venda.valor - (75*venda.quant)

    return (f'Receita: {receita} R$ e Lucro: {lucro} R$')


print(receita([Nota('Pedro', Produto.PAPEL, 3, 180), Nota('Joao', Produto.PAPELAO, 2, 80)]))



