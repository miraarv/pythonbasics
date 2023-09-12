#Usando a estrutura enquanto, faça um algoritmo que solicite ao usuário
#que digite a idade de várias pessoas e calcule e imprima a média de idade dessas
#pessoas.
c=int(input("Quantas pessoas serão inseridas? "))
soma = 0
cont=0
while cont<c:
    idade=int(input("Insira a idade da pessoa:"))
    soma=soma+idade
    cont=cont+1

med=soma/c

print("Média das idades: ", med)