#Faça um programa que leia um número inteiro entre 1 e 12 e exiba o
#nome do mês correspondente. Use a função escolha para exibir o nome do mês (1:
#Janeiro, 2: Fevereiro, etc).

noM = [" ","Janeiro", "Fevereiro", "Março","Abril","Maio","Junho", "Julho", "Agosto","Setembro","Outubro", "Novembro","Dezembro"]

n1 =int(input("Insira um número de 1 à 12: "))
if (n1>12):
    print("Erro: Valor Inválido.")
else:   
    print(noM[(n1)])
