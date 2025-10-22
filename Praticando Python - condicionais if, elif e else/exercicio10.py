renda_mensal = float(input('Digite sua renda mensal: '))
parcela_desejada = float(input('Digite o valor da parcela desejada: '))

parcela_permitida = renda_mensal * 0.30

if parcela_desejada > parcela_permitida:
    print(f'\nSua renda mensal é de R$ {renda_mensal}, a parcela desejada de R$ {parcela_desejada}. Porém a parcela máxima permitida para você é de R$ {parcela_permitida}. Portanto o empréstimo será NEGADO!')
else:
    print(f'\nSua renda mensal é de R$ {renda_mensal}, a parcela desejada de R$ {parcela_desejada}. Porém a parcela máxima permitida para você é de R$ {parcela_permitida}. Portanto o empréstimo será PERMITIDO!')