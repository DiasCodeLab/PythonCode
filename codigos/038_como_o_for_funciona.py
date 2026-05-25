#====================
#Como o for funciona
#====================

dados = 'ABC'

interador = iter(dados)


while True:
    try:
        print(next(interador))
    except StopIteration:
        break