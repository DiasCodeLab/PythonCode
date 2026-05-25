
while True:
    try:
        #entrada de dados.
        decisao = input('Deja continuar [S]sim ou [N]não: ').lower()

        #estrura de decisao para continuar ou não.
        if decisao != 's':
            print('Digite o valor correto apenas "s" para continuar ou "n" para parar...')
            break
        
        if decisao == 'n':
            break

        numero = int(input('Digite um numero: '))
    
    # tratamento de erros.
    except ValueError as error:
        print('Erro voce digitou algo errado, tente novamente...')
        print(type(error).__name__)
        continue
    
    #calculo do impar e par
    if numero == 0:
        print('O numero é 0.')

    elif numero % 2 == 0:
        print('O numero é par.')

    else:
        print('O numero é impar.')
    
