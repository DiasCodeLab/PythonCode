condicao = True
passou_no_if = None

if condicao:
    passou_no_if = None
    print('Faça algo')
else:
    print('Não faça algo ')


print(passou_no_if is None)
print(passou_no_if is not None)