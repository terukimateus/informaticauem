def busca_e_atualiza():
    NOME_ARQ = input('Digite o nome do arquivo: ')
    
    try:
        ARQ = open(NOME_ARQ, 'rb+')
    except:
        ARQ = open(NOME_ARQ, 'wb+')
        TOTAL_REG = 0
        TOTAL_REG = TOTAL_REG.to_bytes(4)
        ARQ.write(TOTAL_REG)
    
    TOTAL_REG = ARQ.read(4)
    TOTAL_REG = int.from_bytes(TOTAL_REG)

    print('Suas opções são: ')
    print('          1. Inserir um novo registro')
    print('          2. Buscar um registro por RRN para alterações')
    print('          3. Terminar o programa')

    OPCAO = int(input('Digite o numero da sua escolha: '))

    while (OPCAO < 3):
        if OPCAO == 1:
            SOBRENOME = input('Sobrenome: ')
            NOME = input('Nome: ')
            RUA = input('Rua: ')
            CIDADE = input('Cidade: ')
            ESTADO = input('Estado: ')
            CEP = input('CEP: ')
            
            REG = f'{SOBRENOME}|{NOME}|{RUA}|{CIDADE}|{ESTADO}|{CEP}|'
            REG = REG.encode()
            REG = REG.ljust(64, b'\0')

            if TOTAL_REG > 1: 
                TOTAL_REG = 1
            OFFSET = TOTAL_REG * 64 + 4
            ARQ.seek(OFFSET)
            ARQ.write(REG)
            TOTAL_REG += 1
        elif OPCAO == 2:
            RRN = int(input('Digite o RRN: '))
            if RRN > TOTAL_REG:
                print('Erro!')
            else:
                OFFSET = RRN * 64 + 4
                ARQ.seek(OFFSET)
                REG = ARQ.read(64)
                REG = REG.decode()
                REG = REG.replace('\0', '')
                for campo in REG.split(sep='|')[:-1]:
                    print(campo)
                ALTERAR = input('Deseja alterar o registro?(ENTER = Não)')
                if ALTERAR:
                    SOBRENOME = input('Sobrenome: ')
                    NOME = input('Nome: ')
                    RUA = input('Rua: ')
                    CIDADE = input('Cidade: ')
                    ESTADO = input('Estado: ')
                    CEP = input('CEP: ')
                    
                    REG = f'{SOBRENOME}|{NOME}|{CIDADE}|{ESTADO}|{CEP}|'
                    REG = REG.encode()
                    REG = REG.ljust(64, b'\0')

                    OFFSET = TOTAL_REG * 64 + 4
                    ARQ.seek(OFFSET)
                    ARQ.write(REG)
        print('Suas opções são: ')
        print('          1. Inserir um novo registro')
        print('          2. Buscar um registro por RRN para alterações')
        print('          3. Terminar o programa')

        OPCAO = int(input('Digite o numero da sua escolha: '))
    ARQ.seek(0)
    TOTAL_REG = TOTAL_REG.to_bytes(4)
    ARQ.write(TOTAL_REG)
    ARQ.close()


if __name__ == '__main__':
    busca_e_atualiza()