#===========================
# exercicio sistema de login
#===========================

nome = 'mateus'
senha = '123456'
conta_ativa = True

usuario = input('Digite seu nome: ' )
senha_digitada = input('Digite uma senha: ' )

login = (
    senha == senha_digitada and 
    usuario == nome
)

captura_erro_de_usuario = (
    usuario != nome
)

captura_erro_de_senha= (
    senha != senha_digitada
)

if login and conta_ativa:
    print(f'Voce logou com sucesso, conta ativa.')

elif captura_erro_de_senha and captura_erro_de_usuario:
    print('Erro voce possui 3 tentativas') 

elif captura_erro_de_usuario:
    print('Erro de usuario tente novamente: ')

elif captura_erro_de_senha: 
    print('Erro de senha tente novamente: ')