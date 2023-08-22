

def calcula_media(v): #def sinaliza uma função, (v) é vetor
    soma = 0
    for i in range(len(v)): #range e len aqui servem para repetir a soma até o vetor acabar
        soma = soma + v[i]
    media = soma/len(v)
    return media 

a =[1,2,3,4,5]
print("A média do vetor A é:", calcula_media(a))
b = [10,20,30,40]
print("A média do vetor B é:", calcula_media(b))
c= [100,200,300,400,500,600,700]
print("A média do vetor C é:", calcula_media(c))
