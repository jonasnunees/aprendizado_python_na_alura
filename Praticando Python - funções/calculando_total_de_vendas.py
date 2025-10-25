# Importa a funcionalidade List do módulo typing para definir tipos de dados em listas
from typing import List 

def verificar_valor_fornecido(mensagem: str) -> float:
    """
    Função que solicita um valor ao usuário e valida se é um número positivo válido.
    
    Parâmetros:
        mensagem (str): Texto que será exibido ao usuário ao pedir o valor
    
    Retorna:
        float: O valor numérico válido fornecido pelo usuário
    """
    
    # Inicia um loop infinito que só será interrompido quando o usuário digitar um valor válido
    while True:

        # Bloco try: tenta executar o código que pode gerar erros
        try:

            # Solicita um valor ao usuário, exibe a mensagem e converte a entrada para número decimal (float)
            valor = float(input(mensagem))

            # Verifica se o valor digitado é negativo (menor que zero)
            if valor < 0:
                
                # Se for negativo, exibe mensagem de erro e volta ao início do loop
                print('\nDigite apenas valores positivos!')
            
            # Verifica se o valor digitado é exatamente zero
            elif valor == 0:

                # Se for zero, exibe uma mensagem questionando (vendeu de graça?) e volta ao início do loop
                print('\nVendeu de graça?')
            
            # Se o valor não é negativo nem zero, então é um valor válido
            else:

                # Retorna o valor válido e encerra a função (sai do loop)
                return valor
            
        # Bloco except: captura erros quando o usuário digita algo que não pode ser convertido para número
        except ValueError:

            # Exibe mensagem de erro se o usuário digitou letras ou caracteres inválidos
            print('\nDigite apenas números!')


def solicitar_valor_da_venda() -> float:
    """
    Função que permite registrar múltiplas vendas e retorna a lista com todos os valores.
    
    Retorna:
        List[float]: Lista contendo todos os valores das vendas registradas
    """

    # Cria uma lista vazia que armazenará todos os valores das vendas
    vendas = []

    # Inicia um loop infinito que continuará até o usuário decidir parar
    while True:
        
        # Chama a função que valida e retorna um valor de venda válido
        valor = verificar_valor_fornecido('\nDigite o valor da venda: R$ ')

        # Adiciona o valor da venda no final da lista de vendas
        vendas.append(valor)

        # Pergunta ao usuário se deseja continuar registrando vendas e converte a resposta para maiúscula
        continuar = input('\nDeseja registrar mais uma venda? (S/N): ').upper()

        # Se a resposta for diferente de 'S' (qualquer tecla exceto S)
        if continuar != 'S':

            # Interrompe o loop (para de pedir vendas)
            break
        
    # Retorna a lista completa com todas as vendas registradas
    return vendas


def somar_vendas(vendas: List[float]) -> float:
    """
    Função que recebe uma lista de valores e calcula o total somando todos os elementos.
    
    Parâmetros:
        vendas (List[float]): Lista contendo os valores das vendas
    
    Retorna:
        float: Soma total de todas as vendas
    """

    # Inicializa uma variável com valor zero para acumular o total das vendas
    total_vendas = 0

    # Loop que percorre cada elemento (venda) dentro da lista de vendas
    for venda in vendas:
        
        # Adiciona o valor da venda atual ao total acumulado
        # É equivalente a: total_vendas = total_vendas + venda
        total_vendas += venda

    # Retorna o valor total acumulado de todas as vendas
    return total_vendas


def main():
    """
    Função principal que coordena a execução do programa.
    Chama as outras funções na ordem correta e exibe o resultado final.
    """

    # Chama a função que solicita as vendas e armazena a lista retornada na variável
    lista_vendas = solicitar_valor_da_venda()

    # Chama a função que soma todas as vendas e armazena o resultado total
    total_vendas = somar_vendas(lista_vendas)

    # Exibe o resultado formatado na tela
    # O :.2f formata o número para exibir 2 casas decimais (centavos)
    print(f'\nO total do faturamento foi de R$ {total_vendas:.2f}')


# Verifica se este arquivo está sendo executado diretamente (não foi importado)
if __name__ == '__main__':

    # Se sim, executa a função principal main() para iniciar o programa
    main()