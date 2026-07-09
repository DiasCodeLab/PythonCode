import jogadores

while True:

    print('1 - adicionar jogador 2 - ver jogadores cadastrado')

    try:
        opcao = int(input('Selecione a opção desejada: '))
    except ValueError:
        print(f'voce digitou digite apenas numero sendo 1 ou 2')
        continue
    if opcao == 1:
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade')
        
        jogadores.cadastrar(nome,idade)
        
    elif opcao == 2:
       jogadores.ver_lista()
