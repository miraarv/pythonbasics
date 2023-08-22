import os
def menu():
    print("================================================\n")
    print("FacInpro\n")
    print("\n 1 - Cadastro\n 2 - Consultar\n 3 - Excluir\n 4 - Sair\n")
    print("================================================\n")
menu()
opcao = int(input("Insira a opção desejada:"))

while opcao <= 3 :
    qntAlunos = 3 
    if opcao == 1 :
        arquivo = open("alunos.txt", "a")
        print("Cadastro de Aliunos: ")
        for i in range(qntAlunos):
            nomeA = input("Aluno:  ")
            arquivo.write(str(nomeA))
            arquivo.write("\n")
        arquivo.close()
    if opcao == 2 :
        arquivo = open("alunos.txt")
        print(arquivo.read())
        arquivo.close 
    if opcao == 3 :
        arquivo = open ("alunos.txt", "w")
        arquivo.write('  ')
        arquivo.close
    menu()
    opcao = int(input("Digite a opção desejada: "))
print ("FIM DO PROGRAMA")
