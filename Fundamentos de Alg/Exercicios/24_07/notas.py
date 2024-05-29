from dataclasses import dataclass

@dataclass

class Notas:
    nome: str
    nota1: float
    nota2: float
    nota3: float
    nota4: float

p1 = Notas('Mateus', 10.0, 9.7, 5.3, 2.1)
p2 = Notas('Beatriz', 6.0, 9.7, 7.3, 5.1)

def situacao(p1: Notas) -> str:
    ''''''

    media = (p1.nota1 + p1.nota2 + p1.nota3 + p1.nota4)/4

    if media >= 7.0:
        return 'aprovado'
    elif media < 4.0:
        return 'reprovado'
    else: 
        return 'exame'

print(situacao(p2))