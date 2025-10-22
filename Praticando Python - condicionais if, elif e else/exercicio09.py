try:

    n = int(input('Digite um número: '))

    if n % 2 == 0:
        print(f'\n{n} é par.')
    else:
        print(f'\n{n} é ímpar.')

except ValueError:
    print('\nDigite apenas um número inteiro.')