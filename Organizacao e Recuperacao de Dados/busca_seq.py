from le_registros import leia_reg

def busca_sequencial():
    NOME_ARQ = input('Digite o nome do arquivo a ser pesquisado: ')

    try:
        ENTRADA = open(NOME_ARQ, 'rb')
    except:
        print('Registro não encontrado')
        exit()

    CHAVE = input('Digite o SOBRENOME a ser buscado: ')
    ACHOU = False

    REG = leia_reg(ENTRADA)

    while REG != '' and ACHOU == False:
        SOBRENOME = REG.split(sep='|')[0]

        if SOBRENOME == CHAVE:
            ACHOU = True
        else:
            REG = leia_reg(ENTRADA)

    if ACHOU == True:
        REG = REG.split(sep='|')[:-1]

        contagem = 1

        for CAMPO in REG:
            print(f'CAMPO {contagem}: {CAMPO}')
            contagem += 1
    else:
        print('Sobrenome não encontrado')
    
    ENTRADA.close()

if __name__ == '__main__':
    busca_sequencial()