#========================
# Argumentos nomeados
#========================

def soma (a,b,c,z):
    print(f'{a=} + {b=} + {c=}',a+b+c+z)
soma(1,2,4,z=10)


def somar(c=None):
    if c:
        print('É falso')
    else:
        print('é positivo')
somar()