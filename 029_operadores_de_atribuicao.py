#=========================
#Operadores de atribuição
# = += -= *= /= //= **= %=
#=========================

condicao = 0b0000000110 + 0b0000000101

while condicao < 100:
    condicao += 0b0000000001
    print(f'{condicao:10b}')
print('FIM')

