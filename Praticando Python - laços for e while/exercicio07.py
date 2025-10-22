estoque = 5

while estoque > 0:
    estoque -= 1
    if estoque >= 1:
        print(f'Venda realizada! Estoque restante: {estoque}')
    else:
        print('Última venda realizada... estoque esgotado!')