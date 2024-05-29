def notas(n1: int, n2: int, n3: int, n4: int):
    '''
    Recebe a nota de 4 avaliações e gera sua média, se o aluno tiver média maior ou igual a 7 é aprovado, reprovado alunos com nota menor que 4 e exame alunos com nota menor que 7 e maior igual a 4.

    Exemplo
    >>> notas(6,7,8,7)
    Aprovado
    >>> notas(5,6,5,7)
    Exame
    >>> notas(4,3,3,2)
    Reprovado
    '''

    média = (n1+n2+n3+n4) / 4

    if média >= 7:
        print('Aprovado')
    elif média < 4:
        print('Reprovado')
    else:
        print('Exame')