#=======================
# listas dentro de lista
#=======================

lista = [

    ['mateus','dias'],
    ['leao'],
    ['gato', (1,2,3,4,True)]

]

print(lista[0][1])
print(lista[2][0])
print(lista[2][1][2])

for nome in lista:
    print(nome)
    for objeto in nome:
        print(objeto)
