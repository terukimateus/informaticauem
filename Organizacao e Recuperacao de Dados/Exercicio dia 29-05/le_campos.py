NOME_ARQ = input('Digite o nome do arquivo: ')

def le_campos(NOME_ARQ: str):

    try:
        ENTRADA = open(NOME_ARQ, 'r')
    except:
        print('Erro na abertura!')
        exit()
    
    CAMPO = leia_campo(ENTRADA)

    n_campo = 1

    while CAMPO != '':
        print(f'Campo #{n_campo}: {CAMPO}')
        n_campo += 1

        CAMPO = leia_campo(ENTRADA)

    ENTRADA.close()

def leia_campo(ENTRADA):
    CAMPO = ''

    C = ENTRADA.read(1)

    while C != '' and C != '|':
        CAMPO = f'{CAMPO}{C}'
        C = ENTRADA.read(1)

    return CAMPO

le_campos(NOME_ARQ)


