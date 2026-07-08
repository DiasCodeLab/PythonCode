pessoa = {}

chave = 'nome'

pessoa[chave] = "mateus"
pessoa['sobrenome'] = 'dias'

print(pessoa[chave])
print(pessoa)


del pessoa['sobrenome']

if pessoa.get('sobrenome')  is None:
    print('Não existe')
else:
    print('existe')
