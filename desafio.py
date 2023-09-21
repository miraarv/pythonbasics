n=int(input("Quantos números serão inseridos?"))
num=[]
maior=0
x=0
menor=0

def buscarMenor(num):
    menor = num[0]
    for i in num:
         if i < menor:
             menor = i
    return menor

for i in range(n):
    x=int(input("Insira um número: "))
    num.append(x)
    if x>maior:
        maior=x
    else: 
        maior=maior
        
soma=sum(num)
print("soma:",soma)
print("média:",soma/n)
print("maior:" ,maior)
print("menor:",buscarMenor(num))
print("ordem crescente: ",sorted(num))
print(num)
em=int(input("Qual elemento deseja buscar? "))
if em in num:
    pos=num.index(em)
    print("O elemento {} está na posição {}".format(em,pos))
else:
    print("{} não existe no vetor.".format(em))




