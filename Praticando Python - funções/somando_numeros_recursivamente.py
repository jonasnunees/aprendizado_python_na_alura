from typing import Tuple

def verificar_numero(mensagem: str) -> int:

    while True:

        try:

            numero: int = input(mensagem)

            if numero <= 0:
                print('O número deve ser maior que zero.')
            
            return numero
        
        except ValueError:
            print('Digite apenas números!')

def solicitar_numeros() -> Tuple[int, int]:

    n1: int = verificar_numero('Digite o primeiro número: ')
    n2: int = verificar_numero('Digite o segundo número: ')

    return n1, n2

def definir_maior_numero(n1, n2):

    if n1 > n2:
        maior = n1
    else:
        maior = n2

    return maior

def definir_menor_numero(n1, n2):

    if n1 < n2:
        menor = n1
    else:
        menor = n2
    
    return menor

def somar_recursivamente(menor, maior):

    if menor > maior:
        return 0
    return menor + somar_recursivamente(menor + 1, maior)

def main():

    n1, n2 = solicitar_numeros()
    menor = definir_menor_numero(n1, n2)
    maior = definir_maior_numero(n1, n2)
    soma = somar_recursivamente(menor, maior)
    print(f'A soma de {menor} até {maior} é: {soma}')

if __name__ == '__main__':
    main()