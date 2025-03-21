num1 = int(input("Digite o número 1"))
num2 = int(input("Digite o número 2"))

operacao = input("Escolha sua operação matemática (+, -, * ou /):")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print (num1 / num2)
else:
    print("Op inválida!")