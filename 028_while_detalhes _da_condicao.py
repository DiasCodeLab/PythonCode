#=========================
# While  com
#=========================

condicao = 0b000000000

while condicao < 0b0000001010:
    condicao = condicao + 0b000000001
    print(f'{condicao:010b}')
print(f'Saiu da condicao onde a condicao final é {condicao:010b}')

