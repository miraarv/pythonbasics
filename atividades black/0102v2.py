#Utilizando a função PI crie um algoritmo que calcule a área de um círculo
#de acordo com a seguinte fórmula: Área do círculo: A=π⋅r2.
import math

def area(r):
   return (math.pi * r * 2)

r = float(input("Insira a medida do raio do círculo: "))
print(f"\nA área do círculo é: {area(r):.3f} cm².")