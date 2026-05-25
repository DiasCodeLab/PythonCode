#=====================
# For in exercicio 11
#=====================


# 1 - Aparecer 1234 na horizontal

numero = '1234'

for numeros in numero:
    print(numeros, end = '-')
print()


#2 - Exercicio 
 
nome = 'mateus'
index = 1
for nomes in nome:
    print(f'{nomes * index}')
    index+=1
print()

# 3 exercicio
nome = 'mateus' 
acomulador = 'm'
index = 1

for digitos in nome:
    local =  acomulador[0]
    print(f'{local*index}')
    index+=1


# 4  - Criando um for com while.
index = 0 
texto = 'mateus'
while index < len(texto):
    print(texto[index])
    index+=1