#===================================
#       3 Exercicios
#===================================



# exercicio numero 1.

usuario_numero_inteiro = int(input('Digite apenas (um) numero inteiro: ').isdigit())
usuario_numero_inteiro_par = usuario_numero_inteiro % 2 == 0
if usuario_numero_inteiro:
    if usuario_numero_inteiro_par:
        print(F'{usuario_numero_inteiro} é par')
    else:
        print(f'{usuario_numero_inteiro} é impar')
else:
    print('Voce não digitou um digito...')
# exercicio numero 2.

pergunta_horas_ao_usuario = int(input('Digite um horario sem os minutos e letras Ex. 17 ou 16: '))

horario_dia = pergunta_horas_ao_usuario >= 0 and pergunta_horas_ao_usuario <=11
horario_tarde = pergunta_horas_ao_usuario >= 12 and pergunta_horas_ao_usuario <=17 
horario_noite = pergunta_horas_ao_usuario >= 18 and pergunta_horas_ao_usuario <=23

if pergunta_horas_ao_usuario:
    if horario_dia:
        print('Bom dia!')
    elif horario_tarde:
        print('Boa tarde !')
    elif horario_noite:
        print('Boa noite !')
else:
    print('Voce não digitou um numero, tente novamente...')

# exercicio numero 3.

nome_do_usuario = input('Digite seu nome: ')

contagem_de_letras = len(nome_do_usuario)
nome_grande = contagem_de_letras >= 5 and contagem_de_letras <= 6

nome_pequeno = contagem_de_letras <= 4
nome_normal = contagem_de_letras >= 5 and contagem_de_letras <= 6
nome_grande = contagem_de_letras > 6

if nome_pequeno:
    print('Seu nome é curto...')
elif nome_normal:
    print('Seu nome é normal...')
elif nome_grande:
    print('Seu nome é muito grande...')
