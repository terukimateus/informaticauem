from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa('Beatriz', 19)
p2 = Pessoa('Mateus', 18)

def compara_idade(p1: Pessoa, p2: Pessoa):
    ''''''

    if p1.idade > p2.idade:
        return p1
    else:
        return p2

p3 = compara_idade(p1,p2)

p3.nome