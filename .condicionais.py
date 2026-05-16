
#=====================
#Uso do if elif else
#=====================

disjuntor = input('digite (ligar) para ligar desligar a luz ou digite (desligar) para desligar a luz a luz: ')

if disjuntor == 'ligar':
    print('A luz ligou')
elif  disjuntor == 'desligar':
    print('A luz apagou')
else:
    print('Voce não digitou corretamente')
print('fora do if ') # fora do bloco de codigos