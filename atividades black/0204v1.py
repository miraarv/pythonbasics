#Usando a estrutura repetição para, faça um algoritmo que calcule e
#imprima a soma dos números pares de 1 a 100.
soma= 0
def somp():
    for i in range(100):
        if i%2==0:
            soma=soma+i
            return soma

print("Soma pares:", somp())