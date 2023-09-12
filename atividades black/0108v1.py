#Faça um programa que leia um número inteiro e exiba uma mensagem
#indicando se ele é positivo, negativo ou zero.

n = int(input("Insira um número: "))

if n>0:
    print("O número inserido é positivo.")
if n<0:
    print("O número inserido é negativo.")
else:
    print("O número inserido é zero.")