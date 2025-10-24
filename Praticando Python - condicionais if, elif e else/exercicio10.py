# Importa o tipo Tuple do módulo typing para anotar funções que retornam múltiplos valores
from typing import Tuple

# Função que pede ao usuário um número e valida que seja um float positivo e não zero
# Recebe uma mensagem (str) para mostrar ao usuário e retorna um float válido
def verificar_valor(mensagem: str) -> float:

    # Loop que repete a solicitação até o usuário fornecer um valor válido
    while True:

        # Tenta executar o bloco de conversão/validação — se der erro, cai no except
        try:

            # Pede a entrada do usuário e tenta converter para número decimal (float)
            valor = float(input(mensagem))

            # Se o valor for negativo, avisa e reinicia o loop para pedir novamente
            if valor < 0:
                print('Digite apenas valores positivos')
                continue  # volta ao início do while

            # Se o valor for zero, avisa que não faz sentido pedir e reinicia o loop
            if valor == 0:
                print('Você não está precisando de dinheiro')
                continue  # volta ao início do while

            # Se chegou até aqui, o valor é válido — retorna o float para quem chamou
            return valor
        
        # Se a conversão para float falhar (ex.: usuário digitou letras), trata o erro aqui
        except ValueError:
            print('Digite apenas números!')

# Função que solicita a renda mensal e a parcela desejada ao usuário
# Não recebe parâmetros e retorna uma tupla com dois floats (renda_mensal, parcela_desejada)
def solicitar_valor() -> Tuple[float, float]:

    # Solicita e valida a renda mensal usando verificar_valor
    renda_mensal = verificar_valor('Digite sua renda mensal: ')

    # Solicita e valida o valor da parcela desejada usando verificar_valor
    parcela_desejada = verificar_valor('Digite o valor da parcela desejada: ')

    # Retorna os dois valores em uma tupla
    return renda_mensal, parcela_desejada

# Função pura que decide se o empréstimo é permitido com base na regra de negócio
# Recebe renda_mensal e parcela_desejada e retorna True se permitido, False caso contrário
def avaliar_emprestimo(renda_mensal: float, parcela_desejada: float) -> bool:

    # Calcula a parcela máxima permitida como 30% da renda e arredonda para 2 casas
    parcela_permitida = round(renda_mensal * 0.30, 2)

    # Retorna True se a parcela desejada for menor ou igual à permitida
    return parcela_desejada <= parcela_permitida

# Função que calcula a parcela máxima permitida (30% da renda) e retorna como float
def verificar_parcela(renda_mensal: float) -> float:

    # Retorna o valor arredondado para 2 casas decimais
    return round(renda_mensal * 0.30, 2)

# Função que exibe uma mensagem final para o usuário com os valores formatados
# Recebe parcela_desejada, parcela_permitida e renda_mensal e não retorna nada (None)
def exibir_mensagem(parcela_desejada: float, parcela_permitida: float, renda_mensal: float) -> None:

    # Converte os números em strings formatadas com duas casas decimais para exibição
    # OBS: estas variáveis passam a ser strings — não use-as para comparações numéricas
    renda_mensal = f'{renda_mensal:.2f}'
    parcela_desejada = f'{parcela_desejada:.2f}'
    parcela_permitida = f'{parcela_permitida:.2f}'

    # Aqui o código compara parcela_desejada e parcela_permitida — cuidado:
    # após as linhas acima estas variáveis são strings, então a comparação será lexicográfica.
    # Em geral é melhor comparar os valores numéricos antes de convertê‑los para string.
    if parcela_desejada > parcela_permitida:
        
        # Se a parcela desejada for maior que a permitida (segundo a comparação feita), mostra NEGADO
        print(f'\nSua renda mensal é de R$ {renda_mensal}, a parcela desejada de R$ {parcela_desejada}. '
              f'A parcela máxima permitida para você é de R$ {parcela_permitida}. Empréstimo NEGADO!')
    else:
        # Caso contrário, permite o empréstimo
        print(f'\nSua renda mensal é de R$ {renda_mensal}, a parcela desejada de R$ {parcela_desejada}. '
              f'A parcela máxima permitida para você é de R$ {parcela_permitida}. Empréstimo PERMITIDO!')
        
# Função principal que orquestra a execução do programa
def main() -> None:
    
    # Chama a função que solicita os dois valores e recebe a tupla descompactada em duas variáveis
    renda_mensal, parcela_desejada = solicitar_valor()

    # Calcula a parcela máxima permitida a partir da renda informada
    parcela_permitida = verificar_parcela(renda_mensal)

    # Avalia se o empréstimo é permitido (útil para testes ou lógica separada)
    permitido = avaliar_emprestimo(renda_mensal, parcela_desejada)

    # Exibe a mensagem final para o usuário (usa os valores calculados acima)
    exibir_mensagem(parcela_desejada, parcela_permitida, renda_mensal)

# Verifica se este arquivo está sendo executado diretamente (não importado)
# Se for o caso, executa a função main()
if __name__ == '__main__':
    main()