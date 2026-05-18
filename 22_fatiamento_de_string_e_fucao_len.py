#=================================
#Fatiamento de string e função len
#=================================


nome = 'Mateus'
print(nome[::1])
print(nome[0:3:1])
convercao = len(nome[:3:1])
if  convercao == len(nome[:3:1]):
    print(f'Possue o mesmo')
else:
    print(f'O nome {nome} não contem nehum caracter')    