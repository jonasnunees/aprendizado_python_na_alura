temperatura_maxima = 25

try:

    temperatura = float(input('Digite a temperatura atual: '))

except ValueError:

    print('\nValor inválido! Por favor, digite apenas números.')

else:

    if temperatura > 25:
        print(f'\nAlerta! A temperatura máxima permitida é de {temperatura_maxima}°C')
    else:
        print(f'\nA temperatura de {temperatura}°C está dentro do limite permitido.')