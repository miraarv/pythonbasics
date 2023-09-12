#Utilizando a função PI crie um algoritmo que calcule a área de um círculo
#de acordo com a seguinte fórmula: Área do círculo: A=π⋅r2.
import math
r = float(input("Insira a medida do raio do círculo: "))

a = (math.pi * r * 2)
print(f"A área do círculo é: {a:.3f} cm²")