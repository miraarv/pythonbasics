#Faça um programa que leia o nome e a idade de uma pessoa e exiba uma
#mensagem concatenando na resposta o nome, idade e indicando se ela é maior de
#idade (idade >= 18) ou menor de idade (idade < 18).


nome =str(input("Insira seu nome: ")) 
idade =int(input("\nInsira sua idade: "))

if (idade<18):
     maior = False
else :
     maior = True

if (maior == False):
    print(nome," tem ", idade, " anos e é menor de idade.")

if (maior == True) :
    print(nome," tem ", idade, " anos e é maior de idade.")



