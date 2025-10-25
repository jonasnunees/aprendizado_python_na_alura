# Importa o tipo List do módulo typing para poder definir listas tipadas
from typing import List

# Função que recebe uma lista de strings (telefones) e retorna uma lista de inteiros
# List[str] significa "lista de strings"
# List[int] significa "lista de números inteiros"
def converter_para_inteiro(telefones: List[str]) -> List[int]:
    
    # List comprehension: cria uma nova lista aplicando int() em cada telefone
    # Para cada 'telefone' na lista 'telefones', converte para inteiro
    # É equivalente a um loop for que vai adicionando cada número convertido em uma nova lista
    return [int(telefone) for telefone in telefones]

# Função que verifica se a conversão dos números foi bem sucedida
# Recebe uma lista de inteiros e não retorna nada (None)
def conferir_conversao(numeros: List[int]) -> None:

    # if numeros verifica se a lista tem algum elemento
    # Se a lista estiver vazia, o if considera como False
    # Se tiver elementos, considera como True
    if numeros:  
        print('Todos os números foram convertidos corretamente!')
    else:
        print('Houve algum erro...')

# Função principal que organiza a execução do programa
def main() -> None:

    # Cria uma lista de strings com números de telefone
    # Cada número está entre aspas pois ainda é uma string (texto)
    telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
    
    # Chama a função que converte as strings para inteiros
    # Guarda o resultado na variável numeros_convertidos
    numeros_convertidos = converter_para_inteiro(telefones)
    
    # Chama a função que verifica se a conversão funcionou
    # Passa a lista de números convertidos como argumento
    conferir_conversao(numeros_convertidos)

# Verifica se este arquivo está sendo executado diretamente (não importado)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()