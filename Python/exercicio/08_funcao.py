#=======================================
# Sistema de Funçao
#=======================================

condicional = 0b0000000000
condicao = 0b000000100
# laço de repeticao com condicional
while condicional < condicao:

    #Entrada de dados
    print('Bem Vindo a conta de algebra, digite os parametros abaixo para a  seguinte conta: primeiro_parametro(segundo_parametro*terceiro_parametro)\n')
    print("===========================================================================================================================")
    primeiro_parametro = int(input('Digite o primeiro parametro, numero inteiro '))
    segundo_parametro = int(input('Digite o primeiro parametro, numero inteiro '))
    terceiro_parametro = int(input('Digite o primeiro parametro, numero inteiro '))
    print("===========================================================================================================================")

    # condicional verifica se todo os parametros foram preenchidos

    parametro = "{a} {b} {c}"
    parametro.format(
        a =primeiro_parametro,
        b = segundo_parametro, 
        c =terceiro_parametro
    )
    algebra__de_multiplicacao = primeiro_parametro * (
    segundo_parametro * terceiro_parametro
)
    
    print(f'O resultado é {algebra__de_multiplicacao:010b}')
    condicional += 0b0000000001

print('fim')       