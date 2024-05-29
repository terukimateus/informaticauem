from enum import Enum, auto
from dataclasses import dataclass

@dataclass
class Situacao(Enum):
    APROVADO = auto()
    REPROVADO = auto()
    EXAME = auto()

def situacao_aluno(n1: float, n2: float, n3: float, n4: float):
    '''
    Exemplos

    >>> situacao_aluno(5.0,6.0,6.0,7.0).name
    'EXAME'

    >>> situacao_aluno(8.0,9.0,7.0,10.0).name
    'APROVADO'

    >>> situacao_aluno(4.0,3.0,2.0,2.5).name
    'REPROVADO'

    >>>
    '''

    media = (n1+n2+n3+n4) / 4

    if 0.0 <= media < 4.0:
        return Situacao.REPROVADO
    elif 4.0 <= media < 7.0:
        return Situacao.EXAME
    else:
        return Situacao.APROVADO
    
def main():
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    n4 = float(input('Digite a nota 4: '))

    status = situacao_aluno(n1, n2, n3, n4).name

    print(status)


if __name__ == '__main__':
    main()