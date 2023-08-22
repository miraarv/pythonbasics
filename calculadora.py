
print("==========CALCULADORA===========\n \n")
print("Insira a opção desejada:\n")
opcao = int(input(" 1:Soma\n 2:Subtração\n 3:Multiplicação\n 4:Divisão\n \nOpção escolhida: "))
print("================================")
def soma(n1,n2):
    soma = n1+n2
    return soma
def mult(n1,n2):
    mult = n1*n2
    return mult
def sub(n1,n2):
    sub = n1-n2
    return sub
def div(n1,n2):
    div = n1/n2
    return div

if (opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4):
        num1 = int(input("\nDigite o primeiro número:\n"))
        num2 = int(input("\nDigite o segundo número:\n"))

if (opcao == 1):
        print("\nO resultado da soma é: \n",soma(num1,num2))
elif (opcao == 3):
        print("\nO resultado da multiplicação é: \n",  mult(num1,num2))
elif (opcao == 2):
        print("\nO resultado da subtração é: \n", sub(num1,num2))
elif (opcao == 4):
        print("\nO resultado da divisão é: \n",  div(num1,num2))
else:
        print("\n Opção inválida.\n")
