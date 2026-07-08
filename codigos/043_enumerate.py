#=======================================
# Uso do enumerate() e iter() com (next)
#=======================================


lista = ['mateus','dias','usuario']
lista_dois = ['mateus','dias','usuario']

lista_enumerada = enumerate(lista)


print(next(lista_enumerada))

for listas in lista_enumerada:
    print(listas)

segunda_lista = iter(lista_dois)

while True:
    try:
        print(next(segunda_lista))
    except:
        break