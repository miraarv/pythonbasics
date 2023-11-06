vetor=[0]*10
digitos = []
strings = []

for i in range(10):
    item=input("Insira um elemento: ")
    vetor.append(item)
for item in vetor:
    if str(item).isnumeric():
        digitos.append(item)
    else:
        strings.append(item)

print("Dígitos:", digitos)
print("Strings:", strings)

