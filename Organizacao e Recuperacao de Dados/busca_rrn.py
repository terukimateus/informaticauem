def busca_rrn():
    NOME_ARQ = input('Digite o nome do arquivo a ser aberto: ')

    try:
        ENTRADA = open(NOME_ARQ, 'rb')
    except:
        print('Erro ao abrir arquivo!')
        exit()

    CAB = ENTRADA.read(4)
    TOTAL_REG = int.from_bytes(CAB)

    RRN = int(input('Digite o RRN: '))

    if RRN >= TOTAL_REG:
        print('RRN maior que o total.')
        exit()
    OFFSET = RRN * 64 + 4
    
    ENTRADA.seek(OFFSET)
    REG = ENTRADA.read(64)
    REG = REG.decode()
    REG = REG.split(sep='|')

    contador = 1

    for CAMPO in REG[:-1]:
        print(F'Campo {contador}: {CAMPO}')
        contador +=1
    ENTRADA.close()


if __name__ == '__main__':
    busca_rrn()