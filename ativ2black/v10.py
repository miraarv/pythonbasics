relatorio=()
nome=[]
peso=[]
altura=[]
imc=[]

for i in range (1):
    nome=str(input("Insira o nome: "))
    peso=(int(input("Insira o peso(kg): ")))
    altura=(int(input("Insira a altura(cm): ")))
    imc=(peso/(altura**2))
for i in range (1):
    relatorio=[(nome[i],peso[i], altura[i],imc[i]),]

for pessoa in relatorio:
    nome, peso, altura, imc = pessoa

