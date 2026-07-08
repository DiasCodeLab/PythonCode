#===================
#Exercicio enumerate
#===================

nomes = ["mateus", "joao", "ana", "carlos"]

nomes[2] = 'Maria'

for index,nome in enumerate(nomes):
    print(f'Usuário {index} : {nome.upper()}')

print(nomes)

        