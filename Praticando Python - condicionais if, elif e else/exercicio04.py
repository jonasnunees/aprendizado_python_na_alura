# Função que solicita um número ao usuário e garante que ele seja válido
def obter_entrada_numerica(mensagem):

    # Cria um loop infinito que só para quando receber um valor válido
    while True:
        # Tenta executar o código abaixo, se der erro, vai para o "except"
        try:
            # Solicita ao usuário um valor e converte para número decimal (float)
            valor = float(input(mensagem))
            
            # Verifica se o valor é menor ou igual a zero
            if valor <= 0:

                # Exibe mensagem de erro para o usuário
                print('O valor deve ser maior que zero. Tente novamente.')
                
                # Volta para o início do loop (while) para pedir novamente
                continue
            
            # Se chegou aqui, o valor é válido, então retorna ele
            return valor
        
        # Captura o erro que acontece quando o usuário digita texto ao invés de número
        except ValueError:

            # Exibe mensagem explicando o erro
            print('Digite apenas valores numéricos!')
            # O loop continua automaticamente, pedindo novamente


# Função que calcula o IMC usando a fórmula: peso dividido pela altura ao quadrado
def calcular_imc(peso, altura):

    # Realiza o cálculo: peso / (altura * altura)
    return peso / (altura ** 2)


# Função que recebe o IMC e retorna uma mensagem com a classificação
def classificar_imc(imc):
    # Verifica em qual faixa o IMC se encaixa e retorna a mensagem correspondente
    
    # Se o IMC for menor que 18.5
    if imc < 18.5:
        return 'Você está abaixo do peso'
    
    # Se o IMC for entre 18.5 e menor que 25
    elif imc < 25:
        return 'Você está com o peso normal'
    
    # Se o IMC for entre 25 e menor que 30
    elif imc < 30:
        return 'Você está com sobrepeso'
    
    # Se o IMC for entre 30 e menor que 35
    elif imc < 35:
        return 'Obesidade grau I'
    
    # Se o IMC for entre 35 e menor que 40
    elif imc < 40:
        return 'Obesidade grau II'
    
    # Se não entrou em nenhuma condição acima, o IMC é 40 ou maior
    else:
        return 'Obesidade grau III'


# Função principal que executa todo o programa
def main():

    # Exibe um título para a calculadora
    print('=== Calculadora de IMC ===\n')
    
    # Chama a função para pedir a altura e armazena o valor na variável "altura"
    altura = obter_entrada_numerica('Informe sua altura (m): ')
    
    # Chama a função para pedir o peso e armazena o valor na variável "peso"
    peso = obter_entrada_numerica('Informe seu peso (kg): ')
    
    # Chama a função que calcula o IMC e armazena o resultado na variável "imc"
    imc = calcular_imc(peso, altura)
    
    # Chama a função que classifica o IMC e armazena a mensagem na variável "classificacao"
    classificacao = classificar_imc(imc)
    
    # Exibe uma linha em branco para separar visualmente
    # Exibe o valor do IMC formatado com 1 casa decimal (.1f)
    print(f'\nSeu IMC é {imc:.1f}')
    
    # Exibe a classificação do IMC
    print(classificacao)


# Verifica se este arquivo está sendo executado diretamente (não foi importado)
if __name__ == '__main__':
    # Executa a função principal
    main()