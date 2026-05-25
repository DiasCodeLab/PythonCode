
#============================
# Ainda esta sendo trabalhado
#============================


senhas = ['123',]
usuarios = ['mateus',]
saldo = 1000
historico_de_transacao = [' ',]

tentativas = 3
while tentativas > 0:

    print(saldo)
    
    menu = int(input('Voce possui cadastro digite [1]sim  ou  [2]não: '))
    
    if menu ==  1:
        usuario = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        for index_usuarios in range(len(usuarios)):
                        if usuarios[index_usuarios] == usuario:
                            for index_senhas in range(len(senhas)):
                                if senhas[index_senhas] == senha:
                                    print("="*10)
                                    print('Deposito [1]')
                                    print('Saque [2]')
                                    print('Historico de transções [3]')
                                    print('='*10)

                                    numero = int(input('Digite o numero desejado: '))

                                    if numero == 1:

                                        deposito = float(input('digite um valor para depositar: '))
                                        historico_de_transacao.append(deposito)
                                        saldo = saldo + deposito
                       
                                    elif numero == 2:
                                        saque = float(input('Digite um valor de saque: '))
                                        historico_de_transacao.append(saque)
                                        saldo = saldo - saque

                                    elif numero == 3:
                                        print(f'{historico_de_transacao}')
                                    
                        else:
                            print(f'Senha ou usuario incorreto voce possui {tentativas}...')
                            tentativas-=1
    elif menu == 2:
            
            cadastro = input('Digite um usuario: ' )
            cadastro_senha = input('Digite uma senha: ')
            usuarios.append(cadastro)
            senhas.append(cadastro_senha)                                                                    
    else:
        print('Voce não digitou um numero')

