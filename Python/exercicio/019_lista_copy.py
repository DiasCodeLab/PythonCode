#=====================
# Copia rasa e profunda
#=====================

from copy import deepcopy

lista = ['',1,True,'false']

biblioteca = [
    [123,'dias'],
    'mateus'
]

# copia rasa onde aponta pro mesmo lugar da memoria não permitindo assim a copia de listas dentro de listas
lista2 = lista.copy()

# copia profunda onde aponta pra outro lugar da memoria permirindo a copia de listas dentro de listas
lista3 = deepcopy(biblioteca)

print(lista)
print(lista2)

print(biblioteca)
print(lista3)

lista3[0][1] = 'oliveira'

print()
print('original:')
print(biblioteca)

print()
print('Deepcopy alterada:')
print(lista3)


lista5 = biblioteca.copy()
print(lista5)