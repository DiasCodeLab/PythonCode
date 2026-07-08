#==================================
# Uso do decimal, round e :.numerof 
#==================================

import decimal 

primeiro_numero = decimal.DecimaL('l0.4')
segundo_numero = decimal.Desimal('0.5')

soma = primeiro_numero + segundo_numero

print(f'O resultado da soma é {soma:.2f}')

print(round(soma,1))

