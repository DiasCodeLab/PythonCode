from produtos_disponiveis import produtos,ver_preco,colocar_no_carrinho

        
lista_produtos = [
    {"nome": "maca", "preco": 10},
    {"nome": "pecego", "preco": 20},
    {"nome": "laranja", "preco": 30},
    {"nome": "abacaxi", "preco": 40}
]
carrinho = ['']

def main():
    ver_produtos = input('Deseja ver no carrinho [1]produto [2]Preço [3] codigo do produto ')

    if ver_produtos == '1':
        produtos(lista_produtos)
    elif ver_produtos == '2':
        ver_preco(lista_produtos)
    else:
        print('produto não encontrado')

    nome_produto = input(
        'Digite o nome do produto que deseja adicionar ao carrinho: '
    )
    for produtos in lista_produtos:
        if produtos in lista_produtos:
            colocar_no_carrinho(lista_produtos,nome_produto)
    else:
        print('Este produto não existe')
if __name__ == '__main__':
    main()