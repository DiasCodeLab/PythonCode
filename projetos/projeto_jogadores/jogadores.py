jogadores = []
    
def cadastrar(nome,idade):
    jogador = {
        'nome':nome,
        'idade':idade
    }
    jogadores.append(jogador)

def ver_lista():
    print(jogadores)

if __name__=="__main__":
    print('executando')




