# Importa o tipo List do módulo typing para fazer anotações de tipo
# Isso ajuda a indicar que uma função trabalha com listas
from typing import List 

# Define uma função que recebe uma mensagem (texto) e retorna um número inteiro
# Esta função é responsável por validar se o usuário digitou um número válido
def verificar_numero_fornecido(mensagem:str) -> int:

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

    # Verifica se a lista está vazia (not pares retorna True se lista vazia)
    if not pares:
        # Se não houver números pares, exibe esta mensagem
        print('Nenhum nÃºmero par foi encontrado.')

    # Loop que percorre cada número par da lista
    for par in pares:

        # Exibe o número par na tela
        # end=' ' faz os números aparecerem na mesma linha, separados por espaço
        # Sem o end=' ', cada número apareceria em uma linha diferente
        print(f'{par}', end=' ')

# Função principal que coordena a execução do programa
# É como o "maestro" que chama as outras funções na ordem correta
def main() -> None:

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