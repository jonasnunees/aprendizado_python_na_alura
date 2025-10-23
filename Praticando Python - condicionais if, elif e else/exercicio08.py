# Função que verifica se a distância digitada é válida
# Recebe uma mensagem (texto) e retorna um número decimal
def verificar_distancia_percorrida(mensagem: str) -> float:

    # Loop infinito que só para quando uma distância válida for digitada
    while True:

        # O bloco try/except serve para tratar possíveis erros
        try:

            # Tenta converter a entrada do usuário para número decimal
            valor = float(input(mensagem))

            # Se a distância for zero, mostra mensagem e pede nova entrada
            if valor == 0:
                print('Você não saiu do lugar.')
                continue  # continue faz o loop voltar ao início
                
            # Se a distância for negativa, mostra mensagem e pede nova entrada
            if valor < 0:
                print('A distância não pode ser negativa. Tá andando de ré?')
                continue  # continue faz o loop voltar ao início
        
            # Se chegou aqui, a distância é válida e pode ser retornada
            return valor
        
        # Se o usuário digitar algo que não é número (letra, símbolo etc.)
        except ValueError:
            print('Digite apenas valores numéricos!')

# Função que solicita a distância percorrida ao usuário
# Não recebe parâmetros e retorna um número decimal
def solicitar_distancia_percorrida() -> float:

    # Chama a função de verificação e guarda o resultado
    distancia_percorrida = verificar_distancia_percorrida('Digite a distância percorrida (em km): ')

    # Retorna a distância válida digitada
    return distancia_percorrida

# Função que mostra quanto será cobrado de pedágio com base na distância
# Recebe um número decimal (distância) e não retorna nada (None)
def exibir_valor_de_pedagio(distancia_percorrida: float) -> None:

    # Se a distância for menor que 100km, cobra R$ 10,00
    if distancia_percorrida < 100:
        print('\nValor do pedágio: R$ 10.00')

    # Se a distância for menor que 200km (e maior ou igual a 100km), cobra R$ 20,00
    elif distancia_percorrida < 200:
        print('\nValor do pedágio: R$ 20.00')
        
    # Se a distância for maior ou igual a 200km, cobra R$ 30,00
    elif distancia_percorrida >= 200:
        print('\nValor do pedágio: R$ 30.00')

# Função principal que organiza a execução do programa
def main() -> None:

    # Primeiro solicita a distância percorrida
    distancia_percorrida = solicitar_distancia_percorrida()

    # Depois mostra o valor do pedágio
    exibir_valor_de_pedagio(distancia_percorrida)

# Verifica se este arquivo está sendo executado diretamente
# Se sim, chama a função main()
if __name__ == '__main__':
    main()
