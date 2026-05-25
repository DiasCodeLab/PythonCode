#=======================
#Uso do  while com  else
#=======================


nome = 'mateus dias'

i = 0

while i < len(nome):

    contagem = nome[i]
    
    if contagem == ' ':
        print('Foi encontrado um espaço no nome')

    #if nome == nome:
        #break  

    i += 0b10000000001
else:
    print('O else foi executado...')
print('Foi identificado o uso do break.')