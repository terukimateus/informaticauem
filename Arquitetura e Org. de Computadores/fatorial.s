.data
    label: .long, 5
    
.text
.globl main
main :
/ * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * /
/* mantenha este trecho aqui - prologo !!! */
    pushq % rbp
    movq % rsp , % rbp
    subq $16 , % rsp
    movq % rbx , -8(% rbp )
    movq % r12 , -16(% rbp )
/  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * /

    MOV label, %rdi
    MOV $1, %rax

calcular:
    CMP $1, %rdi
    JLE end
    
    IMUL %rax, %rdi
    INC %rax
    JMP calcular

end:
    mov $1, %rax
    mov $1, %rdi
    mov $saida, %rsi
    mov %rdi, %rdx
    
saida: .asciz "O fatorial é %ld\n"

/* mantenha este trecho aqui - finalizacao !!!! */
    movq $0 , % rax
    movq -8(% rbp ) , % rbx
    movq -16(% rbp ) , % r12
    leave
    ret
/ * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
