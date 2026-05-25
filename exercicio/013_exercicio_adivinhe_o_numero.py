import random

chance = 5
while  0 < chance:
    numero_digitado = int(input('Digite um nuemro numero: de 0 á 10: '))

    numero_escolhido = random.randint(1,10)

    conferir = numero_digitado > 0 and numero_digitado < 10
    conferencia = numero_digitado == numero_escolhido

    if conferir:
        if conferencia:       
            print(f'Você acertou o numero escolhido era {numero_escolhido}')
        else:
            print(numero_escolhido)
            print(f'Voce possui {chance} chances')
            chance-=1
        if chance == 0:
            print(f'Chances esgotadas o numero era {numero_escolhido}')
    else:
        print('Escolha apenas numeros de (0 a 1)')