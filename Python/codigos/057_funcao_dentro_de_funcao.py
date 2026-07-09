

def numeros(a,b):
    return a+b

def somar(function):
    somar = function(10,10)
    return somar

conta = somar(numeros)
print(conta)


def pessoa(saudacao):

    return saudacao

def saudar(function):
    return function

saldado = saudar(pessoa('Olá'))

print(saldado)


def dano_espada():
    return 50


def dano_arco():
    return 30

def dano_de_flexa():
    return 40

def aplicar_ataque(arma):
    dano = arma()
    print(f'A arma causou {dano} de dano')



aplicar_ataque(dano_espada)
aplicar_ataque(dano_arco)