
#=========================
# While e continue
#=========================

contador = 0b0000000000

while contador < 0b0000001001:
    
    if contador == 0b0000000101:
        print(f'Pulou o {contador:010b}')
        continue
    print(f'{contador:010b}')

print('Fim')