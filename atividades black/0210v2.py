#Utilizando a estrutura de repetição enquanto, faça um algoritmo que
#solicite ao usuário que digite vários números e imprima quantos destes números
#são pares e quantos são ímpares. O programa deve parar de solicitar números
#quando o usuário digitar o número zero.
par=[]
impar=[]
n=int(input("Insira um número: "))
if n%2==0:
    par.append(n)
if n%2==1:
    impar.append(n)

while n!=0:
    n=int(input("Insira um número: "))
    if n%2==0:
        par.append(n)
    if n%2==1:
        impar.append(n)

np=len(par)
ni=len(impar)

print("\nQuantidade de números pares: ", np)#nao sei se era pra manter contando o zero como numero par
print("\nQuantidade de números ímpares: ", ni)