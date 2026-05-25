#===================================================
# Exericio Funcionamento de artmazenamentode memoria
#===================================================

reg_a = []
reg_b = []
reg_c = []


while True:

# Uso do try except para registrar erros.
    try:
          # Menu de seleção numerica. 
        print('='*10)
        print('1 - armazenar\n'
              '2 - calcular\n'
              '3 - ver memória\n'
              '0 - sair'            )
        print('='*10)
        
            # Entrada de dados do 1 menu de seleção.
        dados = int(input('Digite a opção que deseja Ex.. (1) para armazenar, lembrando é permitido apenas 1 numero : '))

                                #======================
                                #Estruturas de decisao
                                #======================

        # Armazenar dados nos registradores.
        if dados == 1:
            # Menu de registradores.
            print('='*10)
            print(
            '1 - registrador a \n'
            '2 - registrador b\n'
            '3 - registrador c\n'        
                )
            #entradas de dados dos registradores.
            registrador = int(input('Qual registrador (1 - para a,\n2 - para b,\n3 -c): '))
            valor = float(input('Digite um Valor: '))

            # Uso do metodo append para armazenar dados na memoria.
            if registrador == 1: 
                reg_a.append(valor)
            elif registrador == 2:
                reg_b.append(valor)
            elif registrador == 3:
                reg_c.append(valor)
        # Soma
        if dados == 2:

            print('='*10)
            # informações
            print('A operação é  (a*b)+c\n')
            # Entrada de valores
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            c = int(input('Digite o valor de c: '))
            #saida de informação
            print(f'O resultado é: {(a*b)+c}' ) 

        # Verificação de dados armazenados nos registradores.            
        if dados == 3:
            print(f"{reg_a=}\n{reg_b=}\n{reg_c=}")
         
        #Uso do metodo break para fechar o programa.
        if dados == 0:
            print('Agradecemos pela escolha, te espero novamente...')
            break
    # Uso do except para tratar erros.         
    except:
        print('='*10)
        print(f'Ouve um erro de informações tente novamente...')
        print('='*10)
        # Uso do continue para retornar ao inicio do programa para nova tentativa
        continue
        