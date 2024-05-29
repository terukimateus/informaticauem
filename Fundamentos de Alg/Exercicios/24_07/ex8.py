
from dataclasses import dataclass

@dataclass
class Monitor:
    COLUNA1: int
    LINHA1: int
    COLUNA2: int
    LINHA2: int

j1 = Monitor(1080,1290,1280,1500)

def click(janela: Monitor, cx: int, cy: int):
    ''''''
    if cx <= janela.LINHA2 and cy <= janela.COLUNA2:
        if cx >= janela.LINHA1 and cy >= janela.COLUNA1:
            print('dentro')
        else:
            print('fora')
    else:
        print('fora')


click(j1, 1300, 1100)


