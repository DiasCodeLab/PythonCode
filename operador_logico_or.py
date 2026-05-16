#=====================
#Operador logico (or)
#=====================


senha = '4321'
nome = 'mateus'

if senha == '4321' or '0' and nome == 'zzzzz':
    print('Entrou...')
else:
    print('Senha incorreta')


#curto circuito

print(False or False or True)