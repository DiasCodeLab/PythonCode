#=========================
# Tipos de dados
#=========================

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

lista = ['nome','mateus']

idade  = pessoa['idade']

dados_lista = lista[1]

print(dados_lista)
print(idade)

for valores in lista:
    print(valores)

for chave in pessoa:
    print(chave, pessoa[chave])
          

novo_dicionario = dict(nome = 'leao',
                       sobrenome = 'elefante')

print(novo_dicionario)
