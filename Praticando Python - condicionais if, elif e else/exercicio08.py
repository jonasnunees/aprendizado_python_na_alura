distancia_percorrida = int(input('Digite a distância percorrida (em km): '))

if distancia_percorrida < 100:
    print('\nValor do pedágio: R$ 10.00')
elif distancia_percorrida < 200:
    print('\nValor do pedágio: R$ 20.00')
elif distancia_percorrida >= 200:
    print('\nValor do pedágio: R$ 30.00')