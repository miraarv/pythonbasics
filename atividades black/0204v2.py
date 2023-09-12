#Usando a estrutura repetição para, faça um algoritmo que calcule e
#imprima a soma dos números pares de 1 a 100.
soma= 0
def somp(soma):
       if i%2==0:
        print(i," + ",(i+2)," = ", soma)
for i in range(100):
    if i%2==0:
        soma=soma+i
        somp(soma)

print("Soma pares:", soma)