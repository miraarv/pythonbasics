pessoas_presentes=['João','Lira', 'Alon', 'Diego', 'Sergio', 'Marcos']
#quero saber se uma pessoa específica está presente
chamada='Alon'

for pessoa in pessoas_presentes:
    if pessoa==chamada:
            print("{} está presente.".format(chamada))
            break
    else:
         print("Print para confirmar que passou pela pessoa."+str(pessoa))
