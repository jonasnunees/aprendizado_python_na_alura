# Importa o tipo Tuple do módulo typing para poder definir o tipo de retorno de funções que devolvem múltiplos valores
from typing import Tuple

# Função que verifica se a nota digitada é válida (entre 0 e 10)
# Recebe uma mensagem (str) como parâmetro e retorna um número decimal (float)
def verificar_notas(mensagem: str) -> float:
    
    # Loop infinito que só será interrompido quando uma nota válida for digitada
    while True:
        try:
            # Tenta converter a entrada do usuário para número decimal
            valor = float(input(mensagem))

            # Verifica se o número está fora do intervalo válido (0 a 10)
            if valor < 0 or valor > 10:
                print('A nota não pode ser negativa e nem maior do que 10!')
                # continue faz o loop voltar ao início
                continue

            # Se chegou aqui, a nota é válida e pode ser retornada
            return valor
        
        # Se o usuário digitar algo que não é número (letra, símbolo etc.)
        except ValueError:
            print('Digite apenas valores numéricos!')

# Função que solicita as três notas do aluno
# Não recebe parâmetros e retorna uma tupla com três números decimais
def solicitar_notas() -> Tuple[float, float, float]:

    # Chama verificar_notas() três vezes, uma para cada nota
    nota_1 = verificar_notas('Primeira nota: ')
    nota_2 = verificar_notas('Segunda nota: ')
    nota_3 = verificar_notas('Terceira nota: ')

    # Retorna as três notas de uma vez
    return nota_1, nota_2, nota_3

# Função que calcula a média das três notas
# Recebe três números decimais e retorna um número decimal
def calcula_media_do_aluno(nota_1: float, nota_2: float, nota_3: float) -> float:

    # Soma as três notas e divide por 3 para obter a média
    media = (nota_1 + nota_2 + nota_3) / 3
    return media

# Função que mostra o resultado final com base na média
# Recebe um número decimal (média) e não retorna nada (None)
def exibir_media_do_aluno(media: float) -> None:

    # Se a média for menor que 5, aluno está reprovado
    if media < 5:
        print(f'\nA média do aluno foi {media:.1f} e ele está reprovado.')

    # Se a média for menor que 7 (e maior ou igual a 5), aluno está de recuperação
    elif media < 7:
        print(f'\nA média do aluno foi {media:.1f} e ele está de recuperação.')

    # Se a média for maior ou igual a 7 (e menor ou igual a 10), aluno está aprovado
    elif media <= 10:
        print(f'\nA média do aluno foi {media:.1f} e ele está aprovado.')

# Função principal que organiza a execução do programa
def main() -> None:

    # Primeiro solicita as três notas
    nota_1, nota_2, nota_3 = solicitar_notas()

    # Depois calcula a média
    media = calcula_media_do_aluno(nota_1, nota_2, nota_3)

    # Por fim, exibe o resultado
    exibir_media_do_aluno(media)

# Verifica se este arquivo está sendo executado diretamente
# Se sim, chama a função main()
if __name__ == "__main__":
    main()