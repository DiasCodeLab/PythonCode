import numpy as np

def formato_array():
    obj= np.array(
        [[1,2,3],
        [3,2,1]]
    )
    return obj.shape

formato = formato_array()
print(formato)

def tirar_tupla(obj):
    for inteiros in obj:
        print(inteiros)
resultado = tirar_tupla(formato)

def pegar_valor(obj):
    lista = []
    for i in obj:
        lista.append(i)
    return lista
valor = pegar_valor(formato)

print(type(valor),valor)
         