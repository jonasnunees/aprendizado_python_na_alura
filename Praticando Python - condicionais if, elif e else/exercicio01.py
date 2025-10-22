try:
    macas_vendidas = int(input('Digite a quantidade de maçãs vendidas: '))
    bananas_vendidas = int(input('Digite a quantidade de bananas vendidas: '))

except ValueError:

    print('Valor inválido! Por favor, digite apenas números inteiros.')
    
else:

    print(f'\nMaçãs vendidas: {macas_vendidas}')
    print(f'Bananas vendidas: {bananas_vendidas}')


    if macas_vendidas == bananas_vendidas:
        print('\nAmbos os produtos tiveram o mesmo número de unidades vendidas.')
    elif macas_vendidas > bananas_vendidas:
        print('\nAs maçãs tiveram mais vendas.')
    else:
        print('\nAs bananas tiveram mais vendas.')