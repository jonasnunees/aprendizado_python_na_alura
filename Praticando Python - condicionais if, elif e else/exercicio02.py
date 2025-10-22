try:

    a = int(input('Informe os dias para a atividade A: '))
    b = int(input('Informe os dias para a atividade B: '))
    c = int(input('Informe os dias para a atividade C: '))

except ValueError:

    print('\nValor inválido! Por favor, digite apenas números inteiros.')

else:

    print(f'\n{a} dias para a atividade A')
    print(f'{b} dias para a atividade B')
    print(f'{c} dias para a atividade C')

    if any(x < 0 for x in (a, b, c)):
        print('\nErro: Os dias não podem ser negativos.')