#17/08/2023- mira
#soma ou multiplica (opção)

opcao = input("Deseja somar (S), multiplicar (M), subtrair (SB) ou dividir(D)?\n")

if (opcao == "s" or opcao == "S" or opcao == "m" or opcao == "M" or opcao == "sb" or opcao == "SB" or opcao == "d" or opcao == "D"):
        num1 = int(input("Digite o primeiro número:\n"))
        num2 = int(input("Digite o segundo número:\n"))

if (opcao == "s" or opcao == "S"):
        soma = num1+num2
        print("O resultado da soma é: \n", soma)
elif (opcao == "M" or opcao == "m"):
        prod = num1*num2
        print("O resultado da multiplicação é: \n", prod)
elif (opcao == "sb" or opcao == "SB"):
        sub = num1-num2
        print("O resultado da subtração é: \n", sub)
elif (opcao == "D" or opcao == "d"):
        div = num1/num2
        print("O resultado da divisão é: \n", div)
else:
        print("Opção inválida.\n")
