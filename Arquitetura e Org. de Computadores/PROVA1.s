    global main
    extern printf
    extern atoi
    section .data
    celsius dq 0
    fahrenheit dq 0
    format db "Temperatura em Fahrenheit: %d", 10, 0
    format_kelvin db "Temperatura em Kelvin: %d", 10, 0
    formato_quente db "Cuidado, está muito quente!", 10, 0
    section .text
main:
    push rbx
    push rsi

    ; Nesta parte do código, definimos rax como o segundo argumento da linha de chamada

    dec rdi
    mov rdi, [rsi+rdi*8]
    mov [celsius], rdi

    call atoi ; usamos o atoi para converter uma string em um número inteiro 64bits.

    pop rdi
    mov [celsius], rax ; movemos rax, para [celsius] para deixar armazenado

    ; Convertemos Celsius para Fahrenheit (Celsius * 9;5) + 32

    imul rax, 9 ; multiplicamos por 9
    mov rbx, 5 ; movemos o valor 5 para rbx
    xor rdx, rdx
    idiv rbx ; dividimos rax por rbx
    add rax, 32 ; adicionamos 32 a rax
    mov [fahrenheit], rax

    ; Salvamos o resultado de rax em RDI, para imprimir Fahrenheit

    mov rdi, rax
    mov rdi, format ; colocamos o primeiro parametro como o format, que é a mensagem ja
    definida em data.
    mov rsi, rax ; colocamos como segundo a temperatura convertida
    xor rax, rax
    call printf ; printf(format, temperatura convertida)
    ; Checar se está muito muito_quente
    cmp qword [fahrenheit], 100 ; Compara fahrenheit > 100 se for jumpa para execução de
    alerta
    jg muito_quente

celsius_kelvin:
    mov rax, [celsius]
    add rax, 273 ; adicionamos 273 a RAX
    mov rdi, rax
    mov rdi, format_kelvin ; colocamos o primeiro parametro como o format_kelvin, que é a
    mensagem ja definida em data.
    mov rsi, rax ; colocamos como segundo a temperatura convertida
    xor rax, rax
    call printf ; printf(format, temperatura convertida)
    jmp final ; Pula para o fim do programa

; Usado para exibir a mensagem de muito quente

muito_quente:
    mov rdi, formato_quente
    xor rsi, rsi
    xor rax, rax
    call printf
    jmp celsius_kelvin ; Jump para o calculo de Kelvin

final:
    pop rbx
    ret