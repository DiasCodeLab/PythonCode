#===============================
# Cadastro com listas
#===============================

lista_usuario = ['',]
lista_senha = ['',]


for _ in range(3):
    usuario = input('Digite seu usuario: ')
    lista_usuario.append(usuario)

    senha = input('Digite sua senha: ')
    lista_senha.append(senha)

print(lista_usuario, end = ' \n')

print('*'*10)

print(lista_senha,end =' \n')


listas = ['','dias',' mateus', 'usuario', 'senha']

listas.insert(1,'mateus')
listas.pop(2)
print(listas, end = ' ')

del listas

lista_usuario.extend(lista_senha)

for x in lista_usuario:
    lista_senha.append(x)
