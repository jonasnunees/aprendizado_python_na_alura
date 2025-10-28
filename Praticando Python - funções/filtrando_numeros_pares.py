"""
Módulo para coleta, filtragem e exibição de números pares.

Este módulo implementa um programa interativo que solicita números inteiros
positivos ao usuário, filtra apenas os números pares e os exibe na tela.

Exemplo de uso:
    $ python filtrando_numeros_pares.py
    
    Digite 10 números inteiros positivos:
    
    Número 1/10: 5
    Número 2/10: 8
    ...
    
    8 12 20
"""

# Importa o tipo List do módulo typing para fazer anotações de tipo
# Isso ajuda a indicar que uma função trabalha com listas
from typing import List 

# Define uma função que recebe uma mensagem (texto) e retorna um número inteiro
# Esta função é responsável por validar se o usuário digitou um número válido
def verificar_numero_fornecido(mensagem:str) -> int:
    """
    Solicita e valida um número inteiro positivo do usuário.
    
    A função continua solicitando entrada até que o usuário forneça um número
    inteiro válido, positivo e diferente de zero. Exibe mensagens de erro
    apropriadas para entradas inválidas.
    
    Args:
        mensagem (str): Mensagem a ser exibida ao solicitar o número do usuário.
    
    Returns:
        int: Número inteiro positivo válido fornecido pelo usuário.
    
    Raises:
        Nenhuma exceção é propagada. Erros são tratados internamente.
    
    Note:
        - Números negativos não são aceitos
        - Zero não é aceito
        - Apenas números inteiros são válidos (não aceita decimais)
    """

    # Cria um loop infinito que só para quando o usuário digitar um número válido
    while True:
    
        # Bloco try-except: tenta executar um código que pode dar erro
        try:

            # Solicita ao usuário que digite algo e tenta converter para número inteiro
            # Se o usuário digitar "abc", isso vai gerar um erro (ValueError)
            numero = int(input(mensagem))

            # Verifica se o número digitado é negativo (menor que zero)
            if numero < 0:
                print('Digite apenas números positivos!')
            # Verifica se o número é exatamente zero
            elif numero == 0:
                print('O número não pode ser igual a zero!')
            # Se passou pelas verificações, o número é válido (positivo e diferente de zero)
            else:
                # Retorna o número válido e sai da função (e do loop while)
                return numero
        
        # Captura o erro que acontece quando o usuário não digita um número
        # Por exemplo: se digitar "abc", "!@#", ou qualquer texto
        except ValueError:
            print('Digite apenas números!')

# Define uma função que coleta vários números do usuário
# Recebe quantos números quer coletar (padrão é 10) e retorna uma lista de números
def solicitar_numero(maximo_de_numeros: int = 10) -> List[int]:
    """
    Coleta múltiplos números inteiros positivos do usuário.
    
    Solicita ao usuário uma quantidade específica de números inteiros positivos,
    validando cada entrada através da função verificar_numero_fornecido().
    Exibe um contador de progresso durante a coleta.
    
    Args:
        maximo_de_numeros (int, optional): Quantidade de números a serem coletados.
            Valor padrão é 10.
    
    Returns:
        List[int]: Lista contendo todos os números válidos fornecidos pelo usuário,
            na ordem em que foram digitados.
    
    Note:
        - A função não retorna até que todos os números sejam coletados
        - Cada número passa pela validação da função verificar_numero_fornecido()
        - O progresso é exibido no formato "Número X/Y"
    """

    # Cria uma lista vazia onde os números digitados serão armazenados
    numeros = []

    # Exibe uma mensagem informando quantos números o usuário precisa digitar
    # O \n cria uma linha em branco antes e depois da mensagem
    print(f'\nDigite {maximo_de_numeros} números inteiros positivos:\n')

    # Loop que vai de 1 até maximo_de_numeros (inclusive)
    # range(1, 11) gera: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    for i in range(1, maximo_de_numeros + 1):   

        # Chama a função de validação pedindo um número
        # Mostra ao usuário qual número está digitando (ex: "Número 1/10")
        numero = verificar_numero_fornecido(f'Número {i}/{maximo_de_numeros}: ')

        # Adiciona o número válido no final da lista
        numeros.append(numero)

    # Retorna a lista completa com todos os números digitados
    return numeros

# Define uma função que filtra apenas os números pares de uma lista
# Recebe uma lista de números e retorna outra lista só com os pares
def filtrar_numeros_pares(numeros: List[int]) -> List[int]:
    """
    Filtra e retorna apenas os números pares de uma lista.
    
    Utiliza a função filter() com uma expressão lambda para identificar
    números pares (divisíveis por 2 sem resto).
    
    Args:
        numeros (List[int]): Lista de números inteiros a serem filtrados.
    
    Returns:
        List[int]: Nova lista contendo apenas os números pares da lista original,
            mantendo a ordem original. Lista vazia se não houver números pares.
    
    Note:
        - Um número é considerado par se o resto da divisão por 2 é zero (n % 2 == 0)
        - A lista original não é modificada
        - A ordem dos elementos é preservada
    """

    # Usa a função filter() para filtrar números pares
    # lambda x: x % 2 == 0 é uma função anônima que verifica se x é par
    # O operador % (módulo) retorna o resto da divisão
    # Se o resto da divisão por 2 é zero, o número é par
    # list() converte o resultado do filter em uma lista
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    # Retorna a lista contendo apenas os números pares
    return pares

# Define uma função que exibe os números pares na tela
# Recebe uma lista de números pares e não retorna nada (deveria ser -> None)
def exibir_numeros_pares(pares: List[int]) -> int:
    """
    Exibe os números pares na tela em uma única linha.
    
    Imprime todos os números da lista fornecida separados por espaços.
    Se a lista estiver vazia, exibe uma mensagem informativa.
    
    Args:
        pares (List[int]): Lista de números pares a serem exibidos.
    
    Returns:
        int: Tipo de retorno incorreto na assinatura (deveria ser None).
            A função não retorna nenhum valor efetivamente.
    
    Note:
        - Os números são impressos na mesma linha, separados por espaços
        - Se a lista estiver vazia, exibe mensagem apropriada
        - Não adiciona quebra de linha ao final da impressão
    """

    # Verifica se a lista está vazia (not pares retorna True se lista vazia)
    if not pares:
        # Se não houver números pares, exibe esta mensagem
        print('Nenhum número par foi encontrado.')

    # Loop que percorre cada número par da lista
    for par in pares:

        # Exibe o número par na tela
        # end=' ' faz os números aparecerem na mesma linha, separados por espaço
        # Sem o end=' ', cada número apareceria em uma linha diferente
        print(f'{par}', end=' ')

# Função principal que coordena a execução do programa
# É como o "maestro" que chama as outras funções na ordem correta
def main() -> None:
    """
    Função principal que orquestra o fluxo do programa.
    
    Coordena a execução sequencial das etapas do programa:
    1. Coleta números do usuário
    2. Filtra os números pares
    3. Exibe os resultados na tela
    
    Returns:
        None: Esta função não retorna nenhum valor.
    
    Note:
        - Utiliza o valor padrão de 10 números para coleta
        - Imprime uma linha em branco antes de exibir os resultados
    """

    # Chama a função que coleta os números do usuário
    # Armazena a lista de números na variável lista_de_numeros
    lista_de_numeros = solicitar_numero()

    # Chama a função que filtra apenas os números pares
    # Armazena os números pares na variável numeros_pares
    numeros_pares = filtrar_numeros_pares(lista_de_numeros)

    # Imprime uma linha em branco para melhorar a visualização
    print()

    # Chama a função que exibe os números pares na tela
    exibir_numeros_pares(numeros_pares)

# Verifica se este arquivo está sendo executado diretamente
# Se sim, chama a função main() para iniciar o programa
# Isso evita que o código rode automaticamente se for importado em outro arquivo
if __name__ == '__main__':
    main()