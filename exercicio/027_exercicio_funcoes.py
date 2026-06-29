#================================
# Verificar Saldo
#================================

def saldo ():
    return 1000

def usuario():
    try:
        usuarios = input('Deseja ver seu saldo saldo [S]sim [N]não: ' ).lower()
        return usuarios
        
    except:
        print('Erro')

def somar_numeros():
    numero = int(input('digite um numero: '))
    return numero * 5
            
def consutar_saldo(usuarios,saldo):
    if usuarios == 's':
        return saldo
    
usuarios= usuario()

variavel_saldo = saldo()

somar = somar_numeros()

variavel_consultar_saldo = consutar_saldo(
    usuarios,
    variavel_saldo
    )

print(variavel_consultar_saldo)
print(somar)
    
        
