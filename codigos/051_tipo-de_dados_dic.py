pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}


pessoas = dict(nome='mateus', sobrenome = 'dias')

nome = pessoa['nome']
print(nome)

for chave in pessoa:
    print(chave,pessoa[chave])




