

def saudacao(saudar):
    def nome(nome):
        return f'{saudar}, {nome}'
    return nome

bom_dia = saudacao('Bom dia')
boa_noite = saudacao('Boa noite')


lista =['mateus','dias','luiz','maria']

print(bom_dia(lista))
print(boa_noite('maria'))


for nomes in lista:
    print(bom_dia(nomes))


def calcular(valor):
    def soma(soma):
        return valor + soma
    return soma

a = calcular(1)

b = a(2)

print(b)