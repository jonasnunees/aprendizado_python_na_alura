# Define uma função que pede e valida os dias de uma atividade
def obter_dias_atividade(nome_atividade):

    # Cria um loop infinito que só para quando o usuário digitar um valor válido
    while True:

        # O bloco 'try' tenta executar código que pode dar erro
        try:

            # Pede ao usuário para digitar os dias e converte para número inteiro
            # A letra 'f' antes das aspas permite inserir variáveis dentro do texto usando {}
            dias = int(input(f'Informe os dias para a atividade {nome_atividade}: '))
            
            # Verifica se o número digitado é negativo
            if dias < 0:

                # Mostra mensagem de erro e volta para o início do loop (continue)
                print('Erro: Os dias não podem ser negativos. Tente novamente.')
                continue  # Pula para a próxima iteração do loop (volta ao while)
            
            # Se chegou aqui, o valor é válido! Retorna o número e sai da função
            return dias
            
        # O bloco 'except' captura erros específicos
        # ValueError acontece quando o usuário digita texto ao invés de número
        except ValueError:

            # Mostra mensagem de erro e o loop recomeça automaticamente
            print('Valor inválido! Por favor, digite apenas números inteiros.')


# Define a função principal do programa (onde tudo começa)
def main():

    # Exibe o título do programa
    # O \n cria uma linha em branco
    print('=== Sistema de Registro de Atividades ===\n')
    
    # Cria um dicionário vazio para guardar as atividades
    # Dicionário é como uma lista, mas com nomes (chaves) ao invés de números
    atividades = {}
    
    # Loop que percorre cada letra da lista ['A', 'B', 'C']
    # A cada volta, 'nome' recebe uma letra diferente (primeiro A, depois B, depois C)
    for nome in ['A', 'B', 'C']:

        # Chama a função obter_dias_atividade e guarda o resultado no dicionário
        # atividades['A'] = dias da atividade A e assim por diante
        atividades[nome] = obter_dias_atividade(nome)
    
    # Exibe o cabeçalho do resumo com uma linha em branco antes (\n)
    print('\n=== Resumo das Atividades ===')
    
    # Percorre o dicionário pegando o nome e os dias de cada atividade
    # .items() retorna pares de (chave, valor) do dicionário
    for nome, dias in atividades.items():
        
        # Exibe os dias e o nome da atividade formatados
        print(f'{dias} dias para a atividade {nome}')
    
    # A função sum() soma todos os valores do dicionário
    # .values() retorna apenas os valores (números de dias), sem os nomes
    total = sum(atividades.values())
    
    # Exibe o total de dias de todas as atividades
    print(f'\nTotal: {total} dias')


# Esta linha especial verifica se o arquivo está sendo executado diretamente
# (não sendo importado por outro programa)
if __name__ == '__main__':

    # Se o arquivo foi executado diretamente, chama a função main()
    # Isso inicia todo o programa
    main()