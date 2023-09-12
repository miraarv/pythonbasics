#Utilizando a estrutura de repetição para, faça um algoritmo que calcule a
#média de 10 números digitados pelo usuário.
soma=0
def med(soma):
    media=soma/10 
    return media 
 
for i in range(10):
    n= int(input("Insira um número:"))
    soma=soma+n

print("Média: ", med(soma))
