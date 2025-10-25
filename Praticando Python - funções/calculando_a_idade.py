# Importa a classe 'date' do módulo datetime para trabalhar com datas
from datetime import date

# Define uma função chamada 'calcular_idade' que não recebe parâmetros
def calcular_idade():

    # Obtém o ano atual usando date.today().year
    # date.today() retorna a data de hoje, e .year pega apenas o ano
    ano_atual = date.today().year
    
    # Inicia um loop infinito que só para quando conseguimos um valor válido
    while True:

        # Bloco try: tenta executar o código que pode gerar erro
        try:

            # Solicita ao usuário que digite o ano de nascimento
            ano_nascimento = int(input('Em que ano você nasceu? '))
            
            # Verifica se o ano é menor ou igual a zero OU maior que o ano atual
            # Isso evita anos negativos, zero ou anos no futuro
            if ano_nascimento <= 0 or ano_nascimento > ano_atual:
                # Mostra mensagem de erro informando o intervalo válido
                print(f'Informe um ano entre 1 e {ano_atual}')
                # 'continue' volta ao início do loop while, pedindo nova entrada
                continue
            
            # Se chegou aqui, o ano é válido!
            # Calcula a idade (ano atual menos ano de nascimento) e retorna o resultado
            # O 'return' também encerra a função e o loop
            return ano_atual - ano_nascimento
            
        # Bloco except: captura o erro ValueError (quando não consegue converter para int)
        # Isso acontece se o usuário digitar letras ou símbolos
        except ValueError:

            # Mostra mensagem explicando o erro e dando exemplo
            print('Entrada inválida. Digite apenas um número inteiro (ex: 1990)')
            # O loop continua automaticamente, pedindo nova entrada


# Define a função principal do programa
def main():

    # Chama a função calcular_idade e guarda o resultado na variável 'idade'
    idade = calcular_idade()
    
    # Imprime a idade formatada em uma frase
    # O 'f' antes das aspas permite inserir variáveis usando {idade}
    print(f'Você tem {idade} anos de idade.')


# Verifica se este arquivo está sendo executado diretamente (não importado)
if __name__ == '__main__':
    
    # Executa a função main, iniciando o programa
    main()