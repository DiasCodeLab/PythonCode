from livros import listar_livros

from usuarios import listar_usuario

from menu import mostrar_menu

def main():

    lista_usuarios =[1,2,3,4]
    
    opcao_livros = [3,2,1,0]
   
    while True:

        mostrar_menu()

        lista_usuario = input('Deseja ver a lista de livros: [s]sim [n]não:  ').lower()

        if lista_usuario == 's':
            livro = listar_livros(opcao_livros)
            print(livro)
        else:
            print('Digite apenas s ou n')

        biblioteca = input('Deseja ver a lista de usuarios: [s]sim [n]não:  ').lower()

        if biblioteca == 's':
            usuario = listar_usuario(lista_usuarios)
            print(usuario)
        else:
            print('Digite apenas s ou n')
        
        if biblioteca not in ['s', 'n']:
            print('Erro')

        if lista_usuario not in ['s', 'n']:
            print('Erro')
        
if __name__ == '__main__':
    main()
