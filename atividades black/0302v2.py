#Faça um programa que leia um vetor com 10 números inteiros e exiba a
#média dos valores.

v=[]
for i in range(0,10):
    n=int(input("insira um número: "))
    v.append(n)
soma=sum(v)
print("Média dos valores: ",(soma/10))
