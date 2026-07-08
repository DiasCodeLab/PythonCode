pessoa = {
    'nome':'mateus',
    'sobrenome':'dias'
}


chave = pessoa.keys()
print(chave)

for chave in pessoa.keys():
    print(chave)

valor = pessoa.values()
print(valor)

for sobrenome in pessoa.values():
    print(sobrenome)

chave_valor = pessoa.items()
print(chave_valor)

for chave, valor in pessoa.items():
    print(chave,valor)

defaut = pessoa.setdefault('idade','não existe')
print(defaut)