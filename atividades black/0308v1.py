#Faça um programa que leia um vetor com 20 números inteiros e exiba a
#quantidade de números que são maiores do que a média dos valores.

v=[]
for i in range(20):
    n=int(input("Insira um número: "))
    v.append(n)
soma=sum(v)
med=soma/20
maior=[]
cont=0
for i in range(20):
    if v[i]>med:
        maior.append(v[i])
        cont=cont+1
print("V=",v)
print("Média: ", med)
print("Números maiores que a média: ",maior)
print("Quantidade números maiores que a média: ",cont)
