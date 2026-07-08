#====================================
# String Iteraveis e uso in /  not in 
#====================================

# 0 1 2 3 4 5
# M A T E U S
# 6 5 4 3 2 1

nome = "Mateus"
print(nome[-6])
print(nome[0])

print('============')

print('a' in nome)
print('z'in nome)

print('============')

print('z' not in nome)
print('Mat' not in nome)


print('============')

nome = input('Digite um nome: ')
encontrar = input('Digite o nome que deseja encontrar: ')


if encontrar in nome:
    print(f'{encontrar} esta em {nome}...')
else:
    print(f'{encontrar} não esta em {nome}...')