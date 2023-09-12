#Utilizando a estrutura de repetição enquanto, faça um algoritmo que
#solicite ao usuário que digite vários números e imprima quantos destes números
#são pares e quantos são ímpares. O programa deve parar de solicitar números
#quando o usuário digitar o número zero.
par=0
impar=0
n=int(input("Insira um número: "))
if n%2==0:
        par=par+1
else:
        impar=impar+1
while n!=0:
    n=int(input("Insira um número: "))
    if n%2==0:
        par=par+1
    else:
        impar=impar+1

print("\nQuantidade de números pares: ", par)#nao sei se era pra manter contando o zero como numero par
print("\nQuantidade de números ímpares: ", impar)