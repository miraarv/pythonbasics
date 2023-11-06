vet=[0]*8
par=[]


for i in range(8):
    vet[i]=int(input("Insira um número: "))
    if (vet[i]%2)==0:
            par.append(vet[i])

print("Números pares: ", par)