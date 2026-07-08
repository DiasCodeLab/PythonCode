#===========================
#Exercicio desempacotamento
#===========================


pessoa = ["Mateus", 25, "Brasil"]

nome,idade,pais = pessoa

contador  = 1

while contador < 10:
    print(f'{nome} tem {idade + contador} anos e mora no {pais}')
    contador += 1
