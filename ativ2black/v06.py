vet=[0]*12
pp=[]
for i in range(12):
    vet[i]=int(input("Insira um número: "))
    if (i%2==0):
        pp.append(vet[i])

print("Números em posições pares: ", pp)