#Faça um programa que calcule a base X elevado ao expoente Y utilizando
#a função exponencial.
def exp(x,y):
    return x**y

x = int(input("Insira a base desejada : "))
y = int(input("\nInsira o expoente desejado: "))

print("\n Resultado: ", exp(x,y))
