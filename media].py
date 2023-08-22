#10/08/2023
#autor: mira
cont = 0
while cont < 3:
    n1= float(input('Nota 1:   \n'))
    n2= float(input('Nota 2:   \n'))

    media= (n1+n2)/2

    print('A média das notas inseridas é :  \n', media)

    if media > 6:
        print('Aprovado.\n')
    else :
        print('Reprovado.\n')
    cont = cont+1
