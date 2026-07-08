#=======================
#Aprendisagem de Lista
#=======================

lista = [123, 'mateus', True, 1, 1.1]

lista[1] = 'dias'

#=================================================
segunda_lista = list(['segunda lista',False,1.1,1])

segunda_lista[0] = 'Mateus'
#=================================================
print(lista)
print(segunda_lista)
print(list('mateus'))
#=================================================

#exemplo do funcionamento de uma (list) parecida com for.

lista_iteravel = ['Leão',123,True]

listas = iter(lista_iteravel)

while True:
    try:
        print(next(listas))        
    except StopIteration:
        break   