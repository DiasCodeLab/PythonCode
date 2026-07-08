#===============
#biblioteca copy
#===============
from copy import deepcopy

lista = ['mateus','dias','usuario']
listas = ['mateus',
    ['dias'], [123]    
]
#faz um copy profunda ao contrario do copy que é uma copia rasa
#o deepcopy é excelente para listas dentro de listas onde ocorre a copia pra outro local da memoria ao contrario do copy.

listas2 = deepcopy(listas)
#desempacota e mostra os obejetos da lista
for  nome in lista:
    print(nome)

#verifica quantos obejetos dentro de uma lista
print(f'{len(lista)}')

#pega o index das listas e altera o nome do objeto.
listas[1][0] = "MUNDO"
print(listas2)
print(listas)
