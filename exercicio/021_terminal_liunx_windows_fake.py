
#========================
#Em desemvolvimento
#========================

arquivos = ['foto.png', 'senha.txt', 'python.py']
historico_de_comandos = [' ',]

login = {
    'mateus':'123'
}

usuario_status = False
              
while True:


    if usuario_status is False:

        usuario = input('Digite um usuario: ')
        senha = input('Digite uma senha: ') 

        if login[usuario] == usuario and login[senha] == senha:
            usuario_status = True
            print(f'{usuario} online')
            comando = input('Digite um comando: ')

            if comando == 'logout':
                print(f'{usuario} : Offline')
                historico_de_comandos.append('logout')
                usuario_status = False
                continue

            elif comando == 'help':
                print('='*40)
                print('Os comandos são\n' \
                    'cls : limpa tela\n'
                    'dir : mostras arquivos na pasta\n'
                    'create: cria arquivos\n'
                    'rename: renomeia a pasta'
                    'history: mostra historico de comandos digitados\n'
                    'exit: fecha o terimnal\n'
                    'history: historico de comandos')
                print('='*60)

                historico_de_comandos.append('help')
            
            elif comando == 'dir':

                print(arquivos)

            elif comando == 'create':

                nome_nova_pasta = input('Digite o nome da pasta')

                arquivos.append(nome_nova_pasta)

                historico_de_comandos.append('create')

            elif comando =='rename':

                print(f'A pasta possui {len(arquivos)} possições ')

                renomerar_pasta = input('Digite o novo nome para pasta: ')

                posicao = int(input(f'Digite a possição da lista que deseja alterar: '))

                arquivos[posicao] = renomerar_pasta

                print(f'A pasta da possição {posicao} foi renomeda para {renomerar_pasta}')

                historico_de_comandos.append('rename')

            elif comando == 'history':
                print(historico_de_comandos)

            elif comando == 'exit':
                print('Programa fechado')
                break
                
            else:
                print('Digite um comando valido...')
    else:
        print(f'Digite a senha correta')
        break
