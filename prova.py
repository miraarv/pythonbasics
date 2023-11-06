def buscarMenor(vet):
    menor = vet[0]
    for i in vet:
         if i < menor:
             menor = i
    return menor

def menu ():
    print("--------------Menu--------------\n") 
    print("\n1=impressão do vetor.\n")  
    print("\n2= exibe maior e menor elemento do vetor.\n")  
    print("\n3= exibe soma e média dos elementos.\n")  
    print("\n4= exibe vetor em ordem crescente e decrescente.\n")  
    print("\n5= pesquisa existência e posição do elemento no vetor. \n")  
    print("\n6= exibe tamanho do vetor \n")
  
vet=[]

menor=0
n=int(input("Quantos números serão inseridos?"))
for i in range(n):
    x=int(input("Insira um número: "))
    vet.append(x)
menu()
c=int(input("Escolha uma opção: \n"))
soma=sum(vet)

if c==1:
    print(vet)
if c==2:
    print("Maior: ",max(vet))   
    print("Menor: ",buscarMenor(vet))
if c==3:
    print("soma:",soma)
    print("média:",soma/n)
if c==4:
    print("ordem crescente: ",sorted(vet))
    vet.sort(reverse=True)
    print("ordem decrescente: ",vet)
if c==5:
    em=int(input("Qual elemento deseja buscar? "))
    if em in vet:
        pos=vet.index(em)
        print("O elemento {} está na posição {}".format(em,pos))
    else:
        print("{} não existe no vetor.".format(em))
if c==6:
    print("O tamanho do vetor é: ", len(vet))





