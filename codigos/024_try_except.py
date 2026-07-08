#=======================
#Uso do try except
#=======================


numero = input('Digite um numero:' ).isdigit()

try:
    numero_convertido_para_inteiro = float(numero)
    print(f'INT : {numero}')
    print(f'INT: {numero_convertido_para_inteiro}')
except:
    print(f'Voce não digitou um numero' )