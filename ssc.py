
print("==========CALCULADORA===========\n \n")
print("Insira a opção desejada:\n")
opcao = int(input(" 1:Soma\n 2:Subtração\n 3:Multiplicação\n 4:Divisão\n \nOpção escolhida:"))
print("================================")
if (opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4):
        num1 = int(input("\nDigite o primeiro número:\n"))
        num2 = int(input("\nDigite o segundo número:\n"))

if (opcao == 1):
        soma = num1+num2
        print("\nO resultado da soma é: \n", soma)
elif (opcao == 3):
        prod = num1*num2
        print("\nO resultado da multiplicação é: \n", prod)
elif (opcao == 2):
        sub = num1-num2
        print("\nO resultado da subtração é: \n", sub)
elif (opcao == 4):
        div = num1/num2
        print("\nO resultado da divisão é: \n", div)
else:
        print("\n Opção inválida.\n")
