#Crie um vetor com 5 posições, solicite que o usuário possa preenche-lo
#na ordem que ele desejar e ao final pergunte qual é o valor que deseja procurar
#neste vetor e informar qual é a posição que se encontra no vetor.

v=[]
for i in range(5):
    n=int(input("Insira um número: "))
    v.append(n)

x=int(input("Qual valor deseja procurar? "))
pos=v.index(x,0,4)
print("Sua posição no vetor é: ", pos)



