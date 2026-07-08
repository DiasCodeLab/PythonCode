#===================================================
#Utilizando args e *args com parametro de uma função
#===================================================


def soma(*args):
    return sum(args)
print(soma(1,2))
print(soma(1,2,3,4))
