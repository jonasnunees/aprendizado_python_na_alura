# Função que verifica se o número digitado é válido (inteiro positivo)
# Recebe uma mensagem (texto) como parâmetro e retorna um número inteiro
def verificar_numero(mensagem: str) -> int:

    # Loop infinito que só será interrompido quando um número válido for digitado
    while True:

        # O bloco try/except serve para tratar possíveis erros na entrada do usuário
        try:
            # Solicita um número ao usuário e converte para inteiro
            # int() converte o texto digitado para número inteiro
            valor = int(input(mensagem))

            # Verifica se o número é negativo
            if valor < 0:
                print('Digite apenas valores positivos!')
                continue  # continue faz o loop voltar ao início

            # Verifica se o número é zero
            if valor == 0:
                print(f'O número {valor} não é par nem ímpar!')
                continue  # continue faz o loop voltar ao início

            # Se chegou aqui, o número é válido e pode ser retornado
            return valor
        
        # Se o usuário digitar algo que não pode ser convertido para inteiro
        except ValueError:
            print('Digite apenas números inteiros!')

# Função que solicita um número ao usuário
# Não recebe parâmetros e retorna um número inteiro
def solicitar_numero() -> int:

    # Chama a função de verificação e guarda o resultado
    numero = verificar_numero('Digite um número: ')

    # Retorna o número válido digitado
    return numero

# Função que verifica se um número é par ou ímpar
# Recebe um número inteiro e não retorna nada (None)
def par_ou_impar(numero: int) -> None:

    # % é o operador de resto da divisão
    # Se o resto da divisão por 2 for 0, o número é par
    if numero % 2 == 0:
        print(f'\n{numero} é par.')

    # Se não for par, é ímpar
    else:
        print(f'\n{numero} é ímpar.')

# Função principal que organiza a execução do programa
def main() -> None:

    # Primeiro solicita o número
    numero = solicitar_numero()
    
    # Depois verifica se é par ou ímpar
    par_ou_impar(numero)

# Verifica se este arquivo está sendo executado diretamente
# Se sim, chama a função main()
if __name__ == '__main__':
    main()