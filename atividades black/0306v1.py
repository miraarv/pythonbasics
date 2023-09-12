#Faça um programa que leia um vetor com 7 números inteiros e exiba o
#vetor em ordem crescente.
v=[]
for i in range(7):
    n=int(input("Insira um número: "))
    v.append(n)
v.sort()
print(v)