# TRABALHO ARQ. E ORG. DE COMPUTADORES Mateus Teruki RA136709 João Paulo da Silva Varjão RA128858
# Notas
# As instruções em IAS devem ser passadas seguindo a tabela de OPCODES abaixo

# O código a ser usado nesse compilador IAS é o programa da primeira prova da matéria.
#0: 30 // Guarda a temperatura em CELSIUS
#1: 9 // Constante usada nas conversoes
#2: 5 // Constante usada nas conversoes
#3: 32 // Constante usada nas conversoes
#4: 273 // Constante usada nas conversoes para Kelvin
#5: LOAD MQ, M(0) // Carrega MQ com o end. 0 que corresponde a 30
#6: MUL M(1) // Carrega M(0), que corresponde a 30, em MQ e logo apos multiplica por 9
#7: DIV M(2) // Divide o acumulador pelo registrador 2 que corresponde a 5
#8 :LOAD MQ // Divide o resultado de 30 * 9 por 5 e passa o resultado para AC com LOAD MQ
#9: ADD M(3) // Adiciona 32 no resultado da operacao anterior
#10: STOR M(18) // Guarda o resultado no acumulador no registrador 18
#11: LOAD M(0) // Carrega no acumulador o valor 30
#12: ADD M(4) // Adiciona o valor guardado no registrador 4 no valor do acumulador
#13: STOR M(19) // Armazena o resultado no acumulador no registrador 19

# Para executar, usar no terminal 'py [nome do arquivo]'


def int_para_binario(int: int):
    int = bin(int)[2:]
    return int

class IAS:
    def __init__(self):
        self.memoria = ['0' * 40] * 20  # Inicializa a memória com 20 espacos, de 40 bytes cada.
        self.AC = '0' * 40  # Inicializa o acumulador 
        self.MQ = '0' * 40 # Inicializa o registrador multiplicador/quociente 
        self.PC = 0  # Inicializa o contador de programa
        self.opcodes = { # Define o Opcode de cada operação
            'ADD': '00000101',
            'STOR': '00100001',
            'LOAD': '00000001',
            'LOAD-': '00000010',
            'LOAD|': '00000011',
            'LOAD-|': '00000100',
            'LOADMQ': '00001010',
            'LOADMQMX': '00001001',
            'ADD|': '00000111',
            'SUB': '00000110',
            'SUB|': '00001000',
            'DIV': '00001100',
            'LSH': '00010100',
            'RSH': '00010101',
            'JUMP': '00001101',
            'JUMP+': '00001110',
            'MUL': '00001011',
            'STOR8-19': '00010010',
            'STOR28-39': '00010011',
        }

    def compilar_instrucao(self, instrucao):
            # Compila as intruções retornando o código de operação e o endereço caso haja um
            if ' ' in instrucao:
                opcode, endereco = instrucao.split(' ')
                codigo_op = self.opcodes[opcode]
                # Extrai o número do endereço entre parênteses
                endereco_numero = int(endereco.split('(')[1].rstrip(')'))
                return codigo_op + f' {endereco_numero}'
            return f'{int_para_binario(int(instrucao))}'

    def carregar_programa(self, programa):
        # Carrega as memórias com suas instruções
        for indice, instrucao in enumerate(programa):
            self.memoria[indice] = '0' * (40 - len(self.compilar_instrucao(instrucao))) + self.compilar_instrucao(instrucao)

    def executar(self):
        # Executa cada linha das instruções em programa.
        for i in range(len(programa)):
            instrucao = self.memoria[self.PC] # Usa o PC(Program counter) para executar as instruções em sua respectiva ordem.
            if ' ' in instrucao: # Se houver espaço na instrução que indica que há um opcode.
                split = instrucao.split(' ')
                opcode = split[0][-8:]
                operando = split[1]
            else: # se não tiver espaço, não há opcode, no nosso programa. Então ele retorna apenas o operando
                operando = instrucao
                opcode = ''

            if opcode == '00000001':  # LOAD Transfer M(X) to the accumulator
                endereco = int(operando)
                self.AC = self.memoria[endereco] # Passa o valor da memória especifica para AC

            elif opcode == '00100001':  # STOR Transfer contents of accumulator to memory location X
                endereco = int(operando)
                self.memoria[endereco] = self.AC # Transfere o valor de AC para um registrador de memória

            elif opcode == '00001010':  # LOADMQ  Transfer contents of register MQ to the accumulator AC
                self.AC = self.MQ 

            elif opcode == '00001001':  # LOADMQMX Transfer contents of memory location X to MQ
                endereco = int(operando)
                self.MQ = self.memoria[endereco] 

            elif opcode == '00001101':  # JUMP
                endereco = int(operando)
                self.PC = endereco - 1  # Subtrai 1 para compensar o incremento no próximo ciclo

            elif opcode == '00001110':  # JUMP+ 
                if self.AC[0] == '0':  # Se o número no acumulador for não negativo
                    endereco = int(operando)
                    self.PC = endereco - 1

            elif opcode == '00000101': # ADD M(X) Add M(X) to AC; put the result in AC
                endereco = int(operando)
                AC = int(self.AC, 2) # Transforma o valor de AC para inteiro.
                
                resultado = f'{int_para_binario(AC + int(self.memoria[endereco], 2))}' # Soma o valor inteiro de AC pelo inteiro da memória escolhida e depois transforma o resultado em Binário
                self.AC = '0' * (40 - len(resultado)) + resultado # Pega o resultado e coloca no final de AC

            elif opcode == '00000111': # ADD |M(X)| Add |M(X)| to AC; put the result in AC
                endereco = int(operando)
                AC = int(self.AC, 2) # Transforma o valor de AC para inteiro.
                
                resultado = f'{int_para_binario(AC + int(self.memoria[endereco], 2))}' # Soma o valor inteiro de AC pelo inteiro da memória escolhida e depois transforma o resultado em Binário
                self.AC = '0' * (40 - len(resultado)) + resultado # Pega o resultado e coloca no final de AC

            elif opcode == '00000110': # SUB M(X) Subtract M(X) from AC; put the result in AC
                endereco = int(operando)
                AC = int(self.AC, 2) # Transforma o valor de AC para inteiro.
             
                resultado = f'{int_para_binario(AC - int(self.memoria[endereco], 2))}' # Diminui o valor inteiro de AC pelo inteiro da memória escolhida e depois transforma o resultado em Binário
                self.AC = '0' * (40 - len(resultado)) + resultado # Pega o resultado e coloca no final de AC

            elif opcode == '00001000': # SUB |M(X)| Subtract |M(X)| from AC; put the remainder in AC
                endereco = int(operando)
                AC = int(self.AC, 2)
     
                resultado = f'{int_para_binario(AC - int(self.memoria[endereco], 2))}' # Diminui o valor inteiro de AC pelo inteiro da memória escolhida e depois transforma o resultado em Binário
                self.AC = '0' * (40 - len(resultado)) + resultado # Pega o resultado e coloca no final de AC

            elif opcode == '00001011': # MUL M(X) Multiply M(X) by MQ; put most significant bits of result in AC, put least significant bits in MQ
                endereco = int(operando)
                MQ = int(self.MQ, 2) # Transforma o valor de MQ para inteiro.

                resultado = f'{int_para_binario(MQ * int(self.memoria[endereco], 2))}'  # Multiplica o valor inteiro  de MQ pelo inteiro do endereço de memória escolhido e converte o resultado em binário.
                self.AC = '0' * (40 - len(resultado)) + resultado # Coloca o resultado no final de AC
            
            elif opcode == '00001100': # DIV M(X) Divide AC by M(X); put the quotient in MQ and the remainder in AC
                endereco = int(operando)
                AC = int(self.AC, 2)
                
                divisao = f'{int_para_binario(int(AC / int(self.memoria[endereco], 2)))}' # Faz a divisão de AC pelo endereço de memória, deixando o quociente salvo.
                resto = f'{int_para_binario(int(AC % int(self.memoria[endereco], 2)))}' # Faz a divisão, porém pegando o resto.

                self.MQ = '0' * (40 - len(divisao)) + divisao # Armazena o quociente em MQ
                self.AC = '0' * (40 - len(resto)) + resto # Armazena o resto em AC

            elif opcode == '00010100': # LSH Multiply accumulator by 2; that is, shift left one bit position
                endereco = int(operando)
                self.AC = self.AC[1:] + '0' # Remove o primeiro número de AC e adiciona um 0 no ultimo, ja que estamos deslocando para esquerda.

            elif opcode == '00010101': # RSH Divide accumulator by 2; that is, shift right one position
                endereco = int(operando)
                self.AC = '0' + self.AC[:-1]  # Remove o ultimo numero de AC e adiciona um 0 no começo, ja que estamos deslocando a direita.

            elif opcode == '00010010': # STOR8-19 Replace left address field at M(X) by 12 rightmost bits of AC
                endereco = int(operando)
                AC = self.AC[-12:]
                self.memoria[endereco] = AC + self.memoria[endereco][12:] # Adiciona AC nos primeiros bytes da memória e remove os 12 primeiros da memória, substituindo

            elif opcode == '00010011': # STOR28-39 Replace right address field at M(X) by 12 rightmost bits of AC
                endereco = int(operando)
                AC = self.AC[-12:]
                self.memoria[endereco] = self.memoria[endereco][:-12] +  AC  # Remove os ultimos 12 bytes do registrador e coloca AC no lugar.

            self.PC += 1    


    def imprimir_memoria(self):
        # Imprime a memória do IAS, AC e MQ.
        for indice, valor in enumerate(self.memoria):
            if valor is not None:
                if ' ' in valor:
                    print(f'{indice}: {valor}')
                else:
                    print(f'{indice}: {valor} Int: {int(valor, 2)}')
        print(f'AC em Binario: {self.AC} // Int: {(int(self.AC, 2))}' )
        print(f'MQ em Binario: {self.MQ} // Int: {(int(self.MQ, 2))}')

# Programa
programa = [
    '30',
    '9',
    '5',
    '32',
    '273',
    'LOADMQMX M(0)',
    'MUL M(1)',
    'DIV M(2)',
    'LOADMQ M(1)',
    'ADD M(3)',
    'STOR M(18)',
    'LOAD M(0)',
    'ADD M(4)',
    'STOR M(19)'
]

ias = IAS()
ias.carregar_programa(programa)
ias.executar()
ias.imprimir_memoria()
