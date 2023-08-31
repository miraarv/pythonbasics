
def calcula_media(v): #def sinaliza uma função, (v) é vetor
    soma = 0
    for i in range(2): #range e len aqui servem para repetir a soma até o vetor acabar
        soma = soma + v[i]
        media = soma/2

vet = []
 float(input("nota 1:"))
vet[2] = float(input("nota 2:"))

print("media:", calcula_media(vet))