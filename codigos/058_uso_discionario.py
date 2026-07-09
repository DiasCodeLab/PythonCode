pessoa = {
    'nome': 'Mateus',
    'sobrenome': 'Dias',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

contagem = pessoa.__len__()

segunda_contagem = len(pessoa)


print(segunda_contagem)
print(contagem,)

for chave in pessoa:
    print(chave, pessoa[chave])


print(pessoa['nome'])
print(pessoa['sobrenome'])


if pessoa.get('nome') is None:
    print('Não existe')
else:
    print(pessoa['nome'])

valor = list(pessoa.values())

print(valor)

chave = list(pessoa.keys())

print(chave)

items = list(pessoa.items())

print(items)

pessoa.setdefault('vivi', 0)

