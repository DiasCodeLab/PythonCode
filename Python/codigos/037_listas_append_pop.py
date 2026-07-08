#===========================
# Utilização de append e pop
#===========================

lista = ['mateus', 'Dias', 'leao']

acresentar = lista.append('onça')
print(lista)

#retirar = lista.pop()
#print(lista)

#quando o pop faz o uso do index ele atribui o valor a uma variavel permitindo assim o uso do objeto,
# ja o valor continua na memoria onde não é preciso a memoria realocar mais espaço para o mesmo valor,
#isso é conhecido como cache, ajudando assim na otmização do codigo.

retirar_com_index = lista.pop(0)
print(lista)

print(retirar_com_index)