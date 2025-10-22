contador = 10

while contador > 0:

    if contador % 2 == 0:
        print(f'Faltam apenas {contador} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {contador} segundos restantes.')
    
    contador -= 1

print('Aproveite a promoção agora!')