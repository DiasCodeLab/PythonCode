#==================================================
#Usuraio e senha com uso do Try except e biblioteca
#==================================================

entativas = 3
usuario_senha = {

    'mateus':'1233'

}


historico_de_tentativas = [

]


while True:

    try:
        usuario= input('Digite seu usuario: ')
        senha = input('Digite sua senha a mesma deve conter no maximo 10 caracteres: ')

    except:

        print('Senha ou usuario incorreto digite apenas letras.')
        continue

    historico_de_tentativas.append((usuario,senha))

    if usuario in usuario_senha and usuario_senha[usuario] == senha:
        print('Voce logou')
        break

    elif len(senha) < 4:
        print('Voce deve digitar uma senha maior que 4 caracteres...')
        tentativas-=1

    else:
        print(f'Voce possui {tentativas}')
        tentativas-=1

    if tentativas == 0:
        print(f'Seu historico de tentatiovas é {historico_de_tentativas}')
        break

 
            
    