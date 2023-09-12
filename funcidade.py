idade = []
idade = [100,2,38,14,50]

print(idade)

idade.insert(2,25) #funcao que insere um valor numa posição do vetor
print(idade)

idade.remove(50)
print(idade)

maior = max(idade)
menor = min(idade)
pos_maior = idade.index(maior) #retorna a posiçao onde se encontra o maior
pos_menor = idade.index(menor)
#pesquisa valores no vetor


print("\nMaior valor no vetor: ", maior)
print("\n Posição do maior valor: ",pos_maior)
print("\nMenor valor no vetor: ", menor)
print("\nPosição do menor valor: ",pos_menor)

maior = max(idade)
menor = min(idade)
print("\nMaior valor no vetor:" , maior)
print("\nMenor valor no vetor: ",menor)

resultado = 45 in idade
if resultado == False:
                                        #funcao que verifica se um valor esta armazenado no vetor
    print("\nA idade 45 não está armazenada no vetor!")

idade.sort()
print(idade)
