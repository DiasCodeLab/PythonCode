def cadastro():
    usuarios = []
    return usuarios

def cadastrar_usuario(usuarios):
    nome = input('Digite um nome: ')
    usuarios.append(nome)
    return  usuarios

lista = cadastro()
cadastrar_usuarios = cadastrar_usuario(lista)
print(cadastrar_usuarios)