#===========================
# Em progreção
#===========================

lista_jogadores = []


def menu():

    print('1. Cadastrar\
    \n2. Mostrar jogadores\
    \n3. Categoria jogador\
    \n4. Sair')

    opcao_menu = int(input('Digite a opção numerica: '))

    return opcao_menu

def cadastro():

    nome_jogador = input('Digite o nome do jogador: ')
    lista_jogadores.append(nome_jogador)

    idade_jogador = input('Digite a idade do jogador: ' )
    lista_jogadores.append(idade_jogador)

def dados_jogador(idade_jogador,nome_jogador):
    
    if idade_jogador < 18:
        
        print()
        
    
    elif idade_jogador >= 18 <= 35:
        lista_jogadores.append(nome_jogador)
        lista_jogadores.append(idade_jogador)
        return f'Profissional'
    
    else:
        lista_jogadores.append(nome_jogador)
        lista_jogadores.append(idade_jogador)
        return 'Veterano'

def buscar_jogador(nome_jogador,idade_jogador):
    
    buscar_nome = input('Digite o nome do jogador que deseja buscar: ')
    buscar_idade = input('Digite a idade do ojgador que deseja buscar: ')

    if buscar_nome in lista_jogadores:
        print(buscar_nome,'se encontra na lista')
    else: 
        print('nome não encontrado...')
    
while True:
    opcao = menu()
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        print(lista_jogadores)
    elif opcao == 3:
        dados_jogador()
    elif opcao == 4:
        break


