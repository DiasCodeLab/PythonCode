#=========================================================
# desempacotamneto em chamada das funções com uso do sep()
#=========================================================


lista = [

    ['mateus','dias'],
    ['leao'],
    ['gato', (1,2,3,4,True)],

]



for listas in lista:
    for lista_final in listas:
        print(lista_final)

print(*lista, end = ' ')
print(*lista, sep = '\n')