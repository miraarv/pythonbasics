#Faça um programa que leia um número inteiro entre 1 e 12 e exiba o
#nome do mês correspondente. Use a função escolha para exibir o nome do mês (1:
#Janeiro, 2: Fevereiro, etc).

n1 =int(input("Insira um número de 1 à 12: "))

if (n1==1):
    print("Janeiro")
if (n1==2):
    print("Fevereiro")
if (n1==3):
    print("Março")
if (n1==4):
    print("Abril")
if (n1==5):
    print("Maio")
if (n1==6):
    print("Junho")
if (n1==7):
    print("Julho")
if (n1==8):
    print("Agosto")
if (n1==9):
    print("Setembro")
if (n1==10):
    print("Outubro")
if (n1==11):
    print("Novembro")
if (n1==12):
    print("Dezembro")
if n1>12 :
    print("Erro: Valor Inválido.")
