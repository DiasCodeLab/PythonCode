#========================
# Uso do insert e extend
#========================


lista = ['mateus','dias','leao']

print(lista[1])

#em listas de grande escala não é interesante o uso do insert 
#pois ele realoca os dados resultando em mais processamento.
lista.insert(1,'nome')

print(lista)

#os dados sao excluidos da memoria junto com a variavel
del lista[1]
print(lista)

#listas separadas
lista_a = ['a','b','c']
lista_b = ['d','e','f','g']

#requer mais processamento
for x in lista_b:
    lista_a.append(x)
print(lista_a, end =' \n')

#O trabalho ocorre diretamente em c baixo nivel sendo assim o mais rapido para junção de listas
lista_a.extend(lista_b)
print(lista_a)