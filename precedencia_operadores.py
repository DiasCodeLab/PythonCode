#====================
#Ordem de precedencia 
#====================

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -



conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

nome = 'MateusDias'
idade = 26
peso = 130
altura = 1.81
calculo = peso / (altura * altura)
print(nome, 'tem', altura, 'de altura', 'seu imc é: ', calculo )
