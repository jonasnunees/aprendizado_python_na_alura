import sys

def exibir_imc(imc):
    print(f'Seu IMC é {imc:.1f}')

def verificar_peso_e_altura(peso, altura):
    if peso <= 0 or altura <= 0:
        print('Não é possível informar um valor negativo ou igual a zero.')
        sys.exit()

try:

    altura = float(input('Informe sua altura (m): '))
    peso = float(input('Informe seu peso (kg): '))

    verificar_peso_e_altura(peso, altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        exibir_imc(imc)
        print('Você está abaixo do peso')
    elif imc >= 18.5 and imc <= 25:
        exibir_imc(imc)
        print('Você está com o peso normal')
    else:
        exibir_imc(imc)
        print('Você está acima do peso')

except ValueError:
    print('Digite apenas valores numéricos!')