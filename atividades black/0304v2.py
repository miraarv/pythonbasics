#Faça um programa para ler dois vetores A e B, contendo N elementos
#cada. Em seguida, gere um terceiro vetor C onde cada elemento de C é a
#multiplicação dos elementos correspondentes de A e B. Imprima o vetor C
#gerado.
A=[]
B=[]
C=[]
n=int(input("Quantos elementos terão os vetores?"))

def prodvet(A,B,C):
    C = [x*y for x,y in zip(A,B)]
    return C

for i in range(n):
    x=(int(input("Insira um valor para o vetor A: ")))
    A.append(x)
print(A)
for i in range(n):
    y=(int(input("Insira um valor para o vetor B: ")))
    B.append(y)
print(B)

print("vetor resultante: ", prodvet(A,B,C))
