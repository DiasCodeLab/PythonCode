#======================
# Uso do while e break
#======================

condicao = True

while condicao:
  nome =  input('Digite seu nome: ')
  print(f'Seu nome é {nome}')

  if nome == 'sair':
    break

print('Laço de repetição finalizado...')

