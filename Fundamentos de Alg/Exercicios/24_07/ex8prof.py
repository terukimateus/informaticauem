from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int

@dataclass
class Janela:
    ponto_superior_esquerdo: Ponto
    ponto_inferior_direito: Ponto

def determina_clique(clique: Ponto, janela: Janela) -> bool:
    '''
    Devolve verdadeiro se o **clique** está dentro da **janela** e false caso contrário.

    >>> determina_clique(Ponto(20,20),Janela(Ponto(5,5), Ponto(30,30)))
    True

    '''
    if janela.ponto_superior_esquerdo.x <= clique.x <= janela.ponto_inferior_direito.x and janela.ponto_superior_esquerdo.y <= clique.y <= janela.ponto_inferior_direito.y:
        return True
    else:
        return False


def janela_sobrepor(janela1: Janela, Janela2: Janela):
    '''
    exemplos

    >>> janela_sobrepor(Janela(Ponto(5,5), Ponto(30,30)), Janela(Ponto(20,20), Ponto(40,40)))
    True

    >>> janela_sobrepor(Janela(Ponto(10,10), Ponto(15,15)), Janela(Ponto(20,20), Ponto(40,40)))
    False

    >>> janela_sobrepor(Janela(Ponto(30,15), Ponto(60,30)), Janela(Ponto(30,25), Ponto(60,80)))
    True

    >>> janela_sobrepor(Janela(Ponto(30,25), Ponto(60,80)), Janela(Ponto(30,15), Ponto(60,30)))
    True
    '''
    if janela1.ponto_superior_esquerdo.x <= Janela2.ponto_superior_esquerdo.x and janela1.ponto_superior_esquerdo.y <= Janela2.ponto_superior_esquerdo.y and janela1.ponto_inferior_direito.x >= Janela2.ponto_superior_esquerdo.x and janela1.ponto_inferior_direito.y >= Janela2.ponto_superior_esquerdo.y:
        return True
    elif Janela2.ponto_superior_esquerdo.x <= janela1.ponto_superior_esquerdo.x and Janela2.ponto_superior_esquerdo.y <= janela1.ponto_superior_esquerdo.y and Janela2.ponto_inferior_direito.x >= janela1.ponto_superior_esquerdo.x and Janela2.ponto_inferior_direito.y >= janela1.ponto_superior_esquerdo.y:
        return True
    else:
        return False