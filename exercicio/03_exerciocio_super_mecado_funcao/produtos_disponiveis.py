
def produtos(lista_produtos):
    for index,produco in enumerate(lista_produtos):
        print(index,produco['nome'])

def ver_preco(lista_produtos):
    for index ,produto in enumerate(lista_produtos):
        print(index,produto['nome'] , produto['preco'])

def colocar_no_carrinho(carrinho,nome_produto):
    carrinho.append(nome_produto)