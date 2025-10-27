# Importa o módulo math, que fornece funções matemáticas, como verificar se um número é finito.
import math

# Função para verificar e obter o nome do produto do usuário
def verificar_nome_do_produto(mensagem: str) -> str:

    
    """
    Solicita ao usuário o nome de um produto e valida a entrada.

    Args:
        mensagem (str): Mensagem exibida ao solicitar o nome do produto.

    Returns:
        str: Nome válido do produto informado pelo usuário.
    """


    while True:
        try:
            # Solicita ao usuário o nome do produto e remove espaços extras
            nome: str = input(mensagem).strip() 

            # Verifica se o usuário não digitou nada
            if not nome:  
                print('Digitar o nome do produto é obrigatório!')
                # Volta ao início do loop para pedir novamente
                continue
            
            # Verifica se o nome tem menos de 4 caracteres
            if len(nome) < 4:  
                print('Esse não é um nome válido!')
                continue  
            
            # Retorna o nome válido, sem espaços extras
            return nome.strip()  
        
        except ValueError as e:  # Captura erros inesperados (raro nesse caso)
            print(f'Erro: {e}')  # Mostra a mensagem de erro

# Função para verificar e obter o valor do produto do usuário
def verificar_valor_do_produto(mensagem: str) -> float:
    
    """
    Solicita ao usuário o valor de um produto e valida a entrada.

    Args:
        mensagem (str): Mensagem exibida ao solicitar o valor do produto.

    Returns:
        float: Valor válido do produto informado pelo usuário.
    """

    while True:
        try:
            # Solicita o valor e troca vírgula por ponto
            raw: str = input(mensagem).strip().replace(',', '.')  

            # Converte o valor digitado para float (número decimal)
            valor: float = float(raw)  

            # Verifica se o valor é um número válido (não infinito ou NaN)
            if not math.isfinite(valor):  
                print('Valor inválido!')
                continue

            if valor <= 0:  
                print('O valor do produto deve ser maior que zero!')
                continue 

            return valor
        
        except ValueError:  # Captura erro se o usuário digitar algo que não seja número
            print('Digite apenas números! (use . ou , como separador decimal)')

# Função para cadastrar vários produtos
def cadastrar_produtos() -> list[dict[str, float | str]]:
    
    """
    Permite ao usuário cadastrar múltiplos produtos, solicitando nome e valor.

    Returns:
        list[dict[str, float | str]]: Lista de dicionários, cada um contendo nome e valor de um produto.
    """

    # Cria uma lista vazia para armazenar os produtos
    produtos: list[dict[str, float | str]] = []  

    while True: 
        produto: str = verificar_nome_do_produto('Digite o nome do produto: ') 
        valor: float = verificar_valor_do_produto('Digite o valor do produto: ')
    
        # Cria um dicionário com os dados
        dados_do_produto: dict[str, float | str] = {'nome': produto, 'valor': valor}

        # Adiciona o produto à lista  
        produtos.append(dados_do_produto)  

        # Pergunta se quer cadastrar mais
        cadastrar: str = input('Deseja cadastrar mais produtos? [S/N] ').strip().upper()  

        # Se a resposta não for 'S', encerra o cadastro
        if cadastrar != 'S':  
            break

    return produtos

# Função para listar os produtos cadastrados
def listar_produtos(produtos: list[dict[str, float | str]]) -> None:

    """
    Exibe a lista de produtos cadastrados com seus respectivos valores.

    Args:
        produtos (list[dict[str, float | str]]): Lista de produtos para exibição.
    """

    for produto in produtos:

        nome_do_produto: str = produto.get('nome')  # Obtém o nome do produto do dicionário
        valor_do_produto: float = produto.get('valor')  # Obtém o valor do produto do dicionário
        print(f'- {nome_do_produto}\n R$ {valor_do_produto:.2f}')  # Exibe o nome e valor formatado

# Função principal do programa
def main() -> None:

    """
    Função principal que executa o fluxo de cadastro e exibição dos produtos.
    """

    produtos: list[dict[str, float | str]] = cadastrar_produtos()  # Chama a função para cadastrar produtos
    listar_produtos(produtos)  # Chama a função para listar os produtos cadastrados

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    try:
        main()  # Executa a função principal
    except KeyboardInterrupt:  # Captura se o usuário pressionar Ctrl+C para interromper
        print('\nOperação cancelada pelo usuário. Saindo...')  # Mensagem de saída amigável