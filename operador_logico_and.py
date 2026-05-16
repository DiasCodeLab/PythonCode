
#=================+++++++
# Uso operador logico and 
#=================+++++++

entrada_saida = input('Digite [E]Eentrar ou [S]Sair: ')
senha = '1234'
if entrada_saida == 'e' and senha == '1234':
    print('Entrou...')
else:
    print('Erro ao entrar tente novamente')


#curto circuito

print(True and True and False)
print(True and 0 and True)
print(1 and 1 and True)


if input('Digite sua senha: ') and ' ': 
    print('senha digitada')
else:
     print('Senha não digitada')