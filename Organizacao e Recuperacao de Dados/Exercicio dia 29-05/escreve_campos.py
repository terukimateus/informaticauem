NOME_ARQ = input('Escreva o nome do arquivo: ')

def escreve_campos(NOME_ARQ: str):
    
    SAIDA = open(NOME_ARQ, 'w')

    SOBRENOME = input('Digite o Sobrenome: ')

    while SOBRENOME != '':
        NOME = input('Digite o nome: ')
        ENDERECO = input('Digite o endereço: ')
        CIDADE = input('Digite a cidade: ')
        ESTADO = input('Digite o estado: ')
        CEP = input('Digite o CEP: ')

        line = f'{SOBRENOME}|{ENDERECO}|{CIDADE}|{ESTADO}|{CEP}|'

        SAIDA.write(line)

        SOBRENOME = input('Digite o Sobrenome: ')

    SAIDA.close()


escreve_campos(NOME_ARQ)