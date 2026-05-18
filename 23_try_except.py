#=======================
#Uso do try except
#=======================


numero = input('Digite um numero:' )

try:
    numero_convertido_para_inteiro = float(numero)
    print(f'STR : {numero}')
    print(f'O numero Inteiro é {numero_convertido_para_intero}')
    print(f'INT: {numero_convertido_para_inteiro}')
except:
    print(f'Voce não digitou um numero' )