import math
from typing import Callable, Tuple

def verificar_numero(mensagem: str) -> float:

    """Solicita e valida a entrada de um número pelo usuário.

    Exibe uma mensagem personalizada e aguarda a entrada do usuário. A função
    realiza validações para garantir que o valor digitado seja um número válido,
    aceitando tanto vírgula quanto ponto como separador decimal. Caso o usuário
    digite um valor inválido, a função solicita novamente até receber um número
    válido e finito.

    Args:
        mensagem: Texto que será exibido ao solicitar o número ao usuário.

    Returns:
        Um número decimal válido e finito digitado pelo usuário.

    Note:
        A função aceita tanto vírgula quanto ponto como separador decimal.
        Valores infinitos ou NaN (Not a Number) são rejeitados.
    """

    while True:

        try:

            # Recebe o texto do usuário, remove espaços e troca vírgula por ponto
            raw: str = input(mensagem).strip().replace(',', '.')

            # Tenta converter o texto em número decimal
            valor: float = float(raw)

            # Verifica se o número é válido (não é infinito ou NaN)
            if not math.isfinite(valor):  
                print('Valor inválido!')
                continue

            return valor

        except ValueError:
            print('Digite apenas números!')    

def solicitar_numeros() -> Tuple[float, float]:

    """Solicita ao usuário os dois números necessários para a operação matemática.

    Utiliza a função verificar_numero para garantir que ambos os valores
    digitados sejam números válidos. Os números são solicitados sequencialmente,
    primeiro o operando esquerdo e depois o operando direito.

    Returns:
        Uma tupla contendo os dois números válidos digitados pelo usuário,
        na ordem (primeiro_número, segundo_número).
    """

    n1: float = verificar_numero('Digite o primeiro número: ')
    n2: float = verificar_numero('Digite o segundo número: ')

    return n1, n2

def solicitar_operacao_matematica() -> str:

    """Solicita ao usuário a escolha da operação matemática a ser realizada.

    Exibe um menu com as operações disponíveis e aguarda a entrada do usuário.
    A função não realiza validação da operação, apenas coleta e retorna o
    símbolo digitado após remover espaços em branco.

    Returns:
        Uma string contendo o símbolo da operação escolhida pelo usuário,
        sem espaços em branco no início ou fim.
    """

    print('=== Selecione uma operação matemática ===')

    operacao: str = input('Escolha a operação (| + | - | * | / |): ')

    # Remove espaços extras e retorna
    return operacao.strip()

def verificar_operacao_matematica(operacao: str) -> Callable[[float, float], float]:

    """Valida a operação matemática e retorna a função correspondente.

    Verifica se o símbolo da operação fornecido é válido (soma, subtração,
    multiplicação ou divisão). Se for válido, retorna uma função lambda que
    executa a operação correspondente. Caso contrário, solicita uma nova
    operação até que o usuário digite uma opção válida.

    Args:
        operacao: String contendo o símbolo da operação matemática
                  (+, -, *, /).

    Returns:
        Uma função lambda que recebe dois números decimais como parâmetros
        e retorna o resultado da operação matemática escolhida.

    Note:
        A função permanece em loop até receber uma operação válida.
        As operações suportadas são: + (soma), - (subtração), 
        * (multiplicação) e / (divisão).
    """

    while True:

        # Verifica qual operação foi escolhida
        match operacao:

            case '+':
                return lambda n1, n2: n1 + n2
            case '-':
                return lambda n1, n2: n1 - n2
            case '*':
                return lambda n1, n2: n1 * n2
            case '/':
                return lambda n1, n2: n1 / n2
            case _:
                print('Operação inválida! Tente novamente...')
                operacao = solicitar_operacao_matematica()

def main() -> None:

    """Função principal que orquestra a execução da calculadora.

    Coordena o fluxo completo da aplicação: solicita os dois números ao usuário,
    pede a operação matemática desejada, obtém a função correspondente à operação,
    executa o cálculo e exibe o resultado na tela.

    Note:
        Esta função não retorna valores, apenas exibe o resultado no console.
    """
    
    n1, n2 = solicitar_numeros()
    operacao = solicitar_operacao_matematica()
    funcao = verificar_operacao_matematica(operacao)
    resultado = funcao(n1, n2)
    print(f'Resultado: {resultado}')

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    try:
        # Tenta executar a calculadora
        main()
    except KeyboardInterrupt:
        # Se o usuário apertar Ctrl+C, mostra mensagem e encerra
        print('\nOperação cancelada pelo usuário. Saindo...')