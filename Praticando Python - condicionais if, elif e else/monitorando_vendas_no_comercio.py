# Função que obtém a quantidade vendida de um produto
def obter_quantidade(produto):
    
    # Inicia um loop infinito que só será interrompido quando obtivermos um valor válido
    while True:

        # O bloco 'try' tenta executar o código que pode gerar erros
        try:
            # Solicita ao usuário que digite a quantidade vendida
            # A função input() sempre retorna texto (string)
            # A função int() converte o texto em número inteiro
            # f'{produto}' insere o nome do produto na mensagem (interpolação de string)
            quantidade = int(input(f'Digite a quantidade de {produto} vendidas: '))
            
            # Verifica se o número digitado é negativo
            if quantidade < 0:
                # Exibe mensagem de erro se for negativo
                print('A quantidade não pode ser negativa. Tente novamente.')
                # 'continue' volta ao início do loop, pedindo o valor novamente
                continue
            
            # Se chegou aqui, o valor é válido (inteiro e não-negativo)
            # 'return' retorna o valor e encerra a função
            return quantidade
        
        # O bloco 'except' captura erros específicos que podem ocorrer no 'try'
        # ValueError acontece quando int() não consegue converter o texto em número
        # Exemplo: se o usuário digitar "abc" ou "12.5"
        except ValueError:

            # Exibe mensagem de erro amigável ao usuário
            print('Valor inválido! Por favor, digite apenas números inteiros.')
            # O loop continua automaticamente, pedindo o valor novamente


# Função que compara as vendas e exibe os resultados
def comparar_vendas(macas, bananas):

    # '\n' cria uma linha em branco antes do texto (quebra de linha)
    print(f'\nMaçãs vendidas: {macas}')

    # f'{bananas}' insere o valor da variável 'bananas' na string
    print(f'Bananas vendidas: {bananas}')
    
    # Verifica se as quantidades são iguais usando o operador '=='
    if macas == bananas:
        print('\nAmbos os produtos tiveram o mesmo número de unidades vendidas.')
    
    # 'elif' significa "senão, se..." - só é verificado se o 'if' anterior for falso
    # Verifica se maçãs teve mais vendas que bananas
    elif macas > bananas:

        # Calcula a diferença entre as vendas (subtração)
        diferenca = macas - bananas

        # Exibe a mensagem com a diferença calculada
        print(f'\nAs maçãs tiveram mais vendas ({diferenca} unidades a mais).')
    
    # 'else' significa "senão" - executado se nenhuma condição anterior foi verdadeira
    # Neste caso, significa que bananas teve mais vendas
    else:

        # Calcula quantas bananas a mais foram vendidas
        diferenca = bananas - macas

        # Exibe a mensagem com a diferença
        print(f'\nAs bananas tiveram mais vendas ({diferenca} unidades a mais).')


# Função principal que coordena todo o programa
def main():

    # Exibe um título para o programa usando '===' como decoração
    print('=== Sistema de Comparação de Vendas ===\n')
    
    # Chama a função obter_quantidade passando 'maçãs' como argumento
    # O resultado (número digitado pelo usuário) é armazenado na variável 'macas_vendidas'
    macas_vendidas = obter_quantidade('maçãs')
    
    # Faz o mesmo para bananas
    bananas_vendidas = obter_quantidade('bananas')
    
    # Chama a função que compara e exibe os resultados
    # Passa as duas quantidades como argumentos (parâmetros)
    comparar_vendas(macas_vendidas, bananas_vendidas)


# Esta linha especial verifica se o arquivo está sendo executado diretamente
# (não está sendo importado por outro arquivo)
if __name__ == '__main__':

    # Se for o programa principal, executa a função main()
    main()