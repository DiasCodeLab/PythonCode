#==========================
# Uso de args não nomeados
#==========================



def soma(*argumentos):

    return sum(argumentos)

soma(1,2,3,4,5,6)

somas = soma()

print(somas)
