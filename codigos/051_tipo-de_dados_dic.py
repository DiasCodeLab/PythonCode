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


def nomes():
    nome_encontrar = input(f'Digite o nome que deseja encontrar no diciionario: ')
    return nome_encontrar

def verificar_nome(nome_encontrar):
    if pessoa in nome_encontrar:
        return f'{nome_encontrar}'
    else:
        print('O nome não existe no diciionario')

while True:
    nome = nomes()
    verificar = verificar_nome()
    if nome == 'sair':
        break
    else:
        verificar_nome('mateus')
        continue