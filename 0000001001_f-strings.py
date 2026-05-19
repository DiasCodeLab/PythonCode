
#===================
#f-strings
#===================

nome = 'MateusDias'
idade = 26
peso = 130
altura = 1.81
calculo = peso / (altura * altura)
print(nome, 'tem a idade de', idade, 'sua altura é de',altura ,'e seu IMC é', calculo)

print(f'{nome} tem a idade de {idade} sua altura é de {altura} seu IMC é {calculo:.2f}')
