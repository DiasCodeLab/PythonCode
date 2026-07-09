

def pix(valor):
    return valor * 0.95

def boleto(valor):
    return valor * 0.90

def cartao(valor):
    return valor 

def desconto(function,valor):
    return function(valor)

print(desconto(pix,100))