import random

lista = ['mateus', 'dias']
palavra = random.choice(lista)
tentativas = 5

designer = ['_']*len(palavra)

while tentativas > 0:
    designer_tela = ' '.join(designer)
    print(designer_tela)

    digito = input('digite uma letra: ')

    for i in range(len(palavra)):
        if palavra[i] == digito:
            designer[i] = digito

    if digito not in palavra:
        tentativas-=1
        print(f'Você possui {tentativas} tentativas')
        if tentativas == 0:
            print(f'Voce perdeu a palavra era "{palavra}" ')
    
    if '_' not in designer:
        print('voce ganhou')
        break