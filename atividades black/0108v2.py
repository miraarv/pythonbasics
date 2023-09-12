#Faça um programa que leia um número inteiro e exiba uma mensagem
#indicando se ele é positivo, negativo ou zero.
def pos(n1):
    print("O número inserido é positivo.")
def neg(n1):
    print("O número inserido é negativo.")
def z(n1):
    print("O número inserido é zero.")
  
n1 = int(input("Insira um número: "))

if n1>0:
    pos(n1)
if n1<0:
    neg(n1)
else:
    (n1)