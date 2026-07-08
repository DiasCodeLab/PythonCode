#==============================
#Listas e modificando listas
#==============================


#para termos listas independentes utilizamos assim.


listas = ['a','b','c','d']



#agora são listas independentes ou seja se alterar a segunda_lista não altera a lista.
lista_secundaria = listas[:]

#lista_secundaria[3:] = 'd'
lista_secundaria[1:3] = [1,4]
print(listas)
print(lista_secundaria)


lista_dentro_de_lista = [
[0,1,2,3,4],
['a','b','c','d']
]

lista_dentro_de_lista_dois = lista_dentro_de_lista[:]

lista_dentro_de_lista_dois[0][1:3] = ['f','f']
print(lista_dentro_de_lista_dois)
print(lista_dentro_de_lista)

texto = 'Python'

texto_dois = texto[:]


print(texto_dois)