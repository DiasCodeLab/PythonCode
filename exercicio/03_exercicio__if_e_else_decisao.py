#=================
#Uso do if e else
#=================


primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite um segundo valor: '))


if primeiro_valor > segundo_valor:
    print(
        f' primeiro valor é maior que o segundo valor'
     )
elif primeiro_valor < segundo_valor:
    print(
        f'O primeiro valor é menor que o segundo valor'
     )
else:
    print(
        f'O primeiro valor é igual ao segundo valor')