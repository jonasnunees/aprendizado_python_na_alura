def solicitar_valor_de_desconto():

    desconto = int(input('Digite a porcentagem de desconto: '))

    return desconto

def solicitar_valor_da_compra():

    valor_da_compra = float(input('Digite o valor da compra: '))

    return valor_da_compra

def preco_final(desconto, valor_da_compra):

    preco_final = valor_da_compra - (valor_da_compra * (desconto / 100))

    return preco_final

def main():

    desconto = solicitar_valor_de_desconto()
    valor_da_compra = solicitar_valor_da_compra()
    resultado = preco_final(desconto, valor_da_compra)
    print(f'Preço final com desconto R$ {resultado}')

if __name__ == '__main__':
    main()