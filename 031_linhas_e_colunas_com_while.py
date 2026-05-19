#============================
# Linhas e Colunas e binarios
#============================


qtd_linhas = 0b0000000101
qtd_coluna = 0b0000000101
qtd_segunda_coluna = 0b0000000101

linhas = 0b0000000000
while linhas <= qtd_linhas:
    colunas = 0b0000000000
    while colunas <= qtd_segunda_coluna:
        segunda_coluna = 0b0000000000
        while segunda_coluna < qtd_coluna:
                print(f'{linhas=} {colunas=} {qtd_coluna=}')
                segunda_coluna+=0b0000000001
                colunas+=0b0000000001
                linhas+=0b0000000001
print('fim')