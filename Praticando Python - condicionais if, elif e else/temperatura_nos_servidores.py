# Definindo uma constante (valor que não muda) para a temperatura máxima permitida
# Por convenção, constantes em Python são escritas em MAIÚSCULAS
TEMPERATURA_MAXIMA = 25

# Esta função é responsável por pedir a temperatura ao usuário e validar se é um número válido
def obter_temperatura():
    # Esta função é responsável por pedir a temperatura ao usuário e validar se é um número válido
    
    # Loop infinito que só para quando conseguimos uma entrada válida
    # while True significa "repita para sempre até encontrar um break ou return"
    while True:

        # O bloco try/except serve para capturar erros que podem acontecer
        try:
            # input() mostra uma mensagem e espera o usuário digitar algo
            # float() tenta converter o texto digitado em um número decimal
            # Se o usuário digitar algo que não é número (como "abc"), vai dar erro
            temperatura = float(input('Digite a temperatura atual (°C): '))
            
            # Se chegou aqui, significa que a conversão funcionou!
            # Retorna o valor da temperatura para quem chamou a função
            # O return também interrompe o loop while
            return temperatura
            
        # except captura o erro caso o usuário digite algo inválido
        except ValueError:
            
            # Mostra mensagem de erro amigável
            print('\nValor inválido! Por favor, digite apenas números.')
            # O loop continua (volta para o início) e pede a temperatura novamente
            print('Tente novamente.\n')

# Esta função compara a temperatura digitada com o limite permitido
# O parâmetro "limite" tem um valor padrão (TEMPERATURA_MAXIMA)
# Isso significa que se não passarmos um valor, ele usa 25 automaticamente
def verificar_temperatura(temperatura, limite=TEMPERATURA_MAXIMA):
       
    # if verifica se a condição é verdadeira (temperatura maior que o limite)
    if temperatura > limite:

        # Se for maior, mostra um alerta
        print(f'\nALERTA! A temperatura de {temperatura}°C excede o limite de {limite}°C')
        
        # Calcula e mostra quanto a temperatura ultrapassou o limite
        # O :.1f formata o número para mostrar apenas 1 casa decimal
        print(f'Diferença: +{temperatura - limite:.1f}°C')
        
    # else executa quando a condição do if é falsa (temperatura <= limite)
    else:
        # Mostra mensagem de que está tudo ok
        print(f'\nTemperatura de {temperatura}°C está dentro do limite permitido.')


def main():
    # Esta é a função principal que coordena todo o programa
    
    # Imprime o título do programa
    print('=== Sistema de Monitoramento de Temperatura ===\n')
    
    # Chama a função obter_temperatura() e guarda o resultado na variável temperatura
    # O resultado pode ser um número (se deu certo) ou None (se deu erro)
    temperatura = obter_temperatura()
    
    # Verifica se a temperatura não é None (ou seja, se foi digitada corretamente)
    # "is not None" é a forma correta de verificar se algo não é None em Python
    if temperatura is not None:

        # Se temos uma temperatura válida, chama a função para verificar se está ok
        verificar_temperatura(temperatura)


# Este bloco só executa se o arquivo for rodado diretamente
# Se alguém importar este arquivo em outro código, este bloco não executa
# É uma boa prática em Python para separar código executável de código reutilizável
if __name__ == '__main__':
    # Chama a função principal para iniciar o programa
    main()