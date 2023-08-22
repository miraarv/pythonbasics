# 15/08/2023 - mira
# calcula media e classifica aluno

cont = 0
while cont < 3:
    nome = input("Insira o nome do aluno:\n")
    n1 = float(input("Insira a nota do 1º bimestre:\n"))
    n2 = float(input("Insira a nota do 2º bimestre:\n"))
    media = (n1+n2)/2
    print(f'Média do aluno',nome,':\n', media)
    if media >= 7: 
        print("Aprovado!")
    if media<7:
        print("Reprovado.")
    cont =cont+1
