
#============================
# Ainda esta sendo trabalhado
#============================

#banco de dados
lista_usuarios = ['mateus',] #lista de usuarios cadastrados
lista_senhas = ['123'] #lista de senhas cadastradas
lista_de_transacao = [' ',] #lista de transacoes feitas

#saudo bancario
saldo_bancario = 1000

#numero inicial de tentativas
tentativas = 3

#laço de repetição 
while tentativas > 0:

    #Menu para selecionar a opção de efetuar cadastro ou logar     
    menu = int(input('Voce possui cadastro digite [1]sim  ou  [2]não: ')) 

    #estrutura de decisão 1 para efetuar login
    if menu ==  1: 
        
        #Entrada de dados para o login com usuario e senha.
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        
        #Pega os indices para cada valor da lista permitindo atraves do indice controlar os dados da lista 
        for index_usuarios in range(len(lista_usuarios)):
            for index_senhas in range(len(lista_senhas)):     

                    # Condição para verificar se os dados estão nas listas.            
                if lista_usuarios[index_usuarios] == usuario and lista_senhas[index_senhas] == senha: 

                    #impreções visuais para o usuario visualisar as opções.               
                    print("="*10)
                    print('Deposito [1]')
                    print('Saque [2]')
                    print('Ver Saldo [3]')
                    print('Historico de Transações [3]')
                    print('='*10)
                    
                    #Estrutura de entrada de dados conforme o numero desejado do menu.
                    numero = int(input('Digite o numero desejado: '))
                    
                    #condicao para o deposito
                    if numero == 1:
                        deposito = float(input('digite um valor para depositar: '))

                        # Recebe o valor de deposito do usuario e adiciona a lista de transações
                        lista_de_transacao.append(deposito)
                        saldo_bancario = saldo_bancario + deposito

                    # condicao para o saque       
                    elif numero == 2:
                        #permite o usuario digitar um numero flutuante. 
                        saque = float(input('Digite um valor de saque: '))
                         
                        # Recebe o valor de saque do usuario e adiciona a lista de transações
                        lista_de_transacao.append(saque)
                        saldo_bancario = saldo_bancario - saque

                    # condicao onde mostra ao usuario seu saldo bancario 
                    elif numero == 3:
                        print(saldo_bancario)

                    # caso for igual a 4 imprime a lista de transações
                    elif numero == 4:
                        print(lista_de_transacao)

                    #caso nenhum numero do menu seja digitado    
                    else:
                        print('Voce não digitou um numero do menu...')
                
                else:
                    #caso o usuario erre a senha suas tentavivas diminuem 
                    print(f'Senha incorreta voce possui {tentativas}')
                    tentativas-=1
                    
                    #condição caso a tentativa esgote.
                    if tentativas == 1:
                        print('Espere 1h para tentar novamnete...')
                        break

    #estrutura de decisão 2 para cadastar usuario as listas de usuario e senha.
    elif menu == 2:
        #estrutura de entrada de dados para  cadastro.
        cadastro_usuario = input('Digite um usuario: ' )
        cadastro_senha = input('Digite uma senha: ')

        #dados do cadastro adicionando senha e usuario.
        lista_usuarios.append(cadastro_usuario)
        lista_senhas.append(cadastro_senha)

    else:
        #Caso o usuario não digite os numeros inteiros 1 ou 2 executa o else com a mensagem abaixo.
        print('Voce não digitou o numero [1]sim ou [2]não')


