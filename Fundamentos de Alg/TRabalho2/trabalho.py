from dataclasses import dataclass

def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''

    alternativas = []
    alternativa = 1

    while s > 0:
        # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
        # divide todas as alternativas que compõe
        # o somatório s por 2
        s = s // 2
        # procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas

@dataclass
class Prova:
    codigo: int
    redacao: int
    respostas: list[int]

def compara_alternativa(resposta: list[int], gabarito: list[int]) -> int:
    ''''''
    if len(resposta) == 1:
        if resposta[0] in gabarito:
            return 1
        
    if len(resposta) == 0:
        return 0
    
    if resposta[0] not in gabarito:
        return 0 
    
    if compara_alternativa(resposta[1:], gabarito) == 0:
        return 0
    
    return 1 + compara_alternativa(resposta[1:], gabarito)

def ordem(resultado: list[list]):
    '''
    Recebe uma lista de resultados com dois valores, um código identificador e a nota.
    E retorna uma lista com os resultados em ordem de maior nota para menor
    '''

    if len(resultado) == 1:
        return resultado
    
    for i in range(len(resultado)):
        maior = i
   
        for j in range(i + 1, len(resultado)):
            if resultado[j][1] > resultado[maior][1]:
                maior = j
        resultado[i], resultado[maior] = resultado[maior], resultado[i]

    return resultado

def notas(provas: list[Prova], gabarito: list[int]) -> list:
    ''''''

    resultado = []

    for prova in range(len(provas)):
        if provas[prova].redacao != 0:
            candidato = []

            nota = provas[prova].redacao

            for alternativa in range(len(provas[prova].respostas)):
          
                alternativas = somatorio_alternativas(provas[prova].respostas[alternativa])
                corretas = somatorio_alternativas(gabarito[alternativa])
                certas = compara_alternativa(alternativas, corretas)

                if certas >= 1:
                    if len(corretas) == 5:
                        nota += certas * 1.2
                    elif len(corretas) == 4:
                        nota += certas * 1.5
                    elif len(corretas) == 3:
                        nota += certas * 2
                    elif len(corretas) == 2:
                         nota += certas * 3
                    elif len(corretas) == 1:
                        nota += 6

            candidato.append(provas[prova].codigo)
            candidato.append(nota)
            resultado.append(candidato)
    print(resultado)
    return ordem(resultado)


print(notas([Prova(3211, 80, [4, 10, 4, 16, 10]), Prova(7102, 0, [1, 2, 3 , 4, 5]), Prova(1234, 90, [21, 8, 8, 8, 14]), Prova(5812, 32, [20, 0, 8, 16, 1]), Prova(9123, 0, [5, 4, 3, 2, 1])], [21, 10, 8, 16, 15]))
