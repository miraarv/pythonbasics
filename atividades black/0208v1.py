#Utilizando a estrutura de repetição repita, faça um algoritmo que solicite
#ao usuário que digite vários números e imprima a média desses números. O
#programa deve parar de solicitar números quando o usuário digitar um número
#negativo.
n=int(input("Insira um número:"))
soma=0
cont=0
while n>0: 
    n=int(input("Insira um número:"))
    soma=soma+n
    cont=cont+1
print(f"Média:{(soma/cont):.3f}")