#==================================
# Exercicio Saldo de Banco com Menu
#==================================


linhas_menu = 15 * '#'
titulo_menu = ' ' * 3 + 'MENU'


print(linhas_menu)
print(titulo_menu)
print(linhas_menu)
print('1. Ver saldo')
print('2. Depositar')
print('3. Sacar')
print(linhas_menu)

saldo = 1000

numero_da_escolha = int(input('Digite o numero da opção: '))

primeiro_numero= (
    numero_da_escolha == 1
)

segundo_numero= (
    numero_da_escolha == 2
)

terceiro_numero= (
    numero_da_escolha == 3
)

if primeiro_numero:
    print(f'Seu saldo é {saldo} reais')

elif segundo_numero:
    banco = int(input('Digite um valor de deposito: '))
    print(f'Seu sacou {saldo} reais')
    print(f'Seu saldo é  {saldo + banco} reais')

elif terceiro_numero:

    banco = int(input('Digite um valor de deposito: '))
    print(f'Seu sacou {saldo} reais')
    print(f'Seu saldo é  {saldo - banco} reais')



