#variável composta homogênea 24/08/2023

qtd = 5
n = []
soma = 0
media = 0
cont = 0
for i in range(qtd):
    n.append(float(input("Informe o número: ")))
    print(n)
    soma = soma + n[i]
    media = soma/qtd
    if n[i]>media:
        cont = cont + 1 

print("\n")
print("Média:", media)
print("Vetor resultante:\n",n)
print("Quantidade de vetores maiores que a média: ", cont)