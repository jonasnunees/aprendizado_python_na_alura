# Importa apenas a classe datetime do módulo datetime para trabalhar com data e hora
from datetime import datetime

# Importa Literal do módulo typing para definir quais textos exatos a função pode retornar
from typing import Literal

# Definimos constantes (valores que não mudam) para tornar o código mais legível
# Meio-dia marca o início da tarde
HORA_INICIO_TARDE = 12

# 18 horas (6 da tarde) marca o início da noite
HORA_INICIO_NOITE = 18

# Define uma função que retorna uma saudação baseada na hora do dia
# -> Literal[...] indica que a função só pode retornar um desses três textos exatos
def obter_saudacao() -> Literal['Bom dia!', 'Boa tarde!', 'Boa noite!']:

    # Pega a hora atual do sistema
    # datetime.now() obtém data e hora atual
    # .hour extrai apenas a parte da hora (0-23)
    hora_atual = datetime.now().hour

    # Se a hora for antes do meio-dia (menor que 12)
    if hora_atual < HORA_INICIO_TARDE:
        return 'Bom dia!'
    
    # Se a hora for entre meio-dia e 18h
    # Esta condição verifica se hora_atual está entre 12 e 17
    elif HORA_INICIO_TARDE <= hora_atual < HORA_INICIO_NOITE:
        return 'Boa tarde!'
    
    # Se não for nenhuma das condições acima (ou seja, 18h ou mais)
    else:
        return 'Boa noite!'

# Função principal que organiza a execução do programa
def main():

    # Chama a função obter_saudacao() e guarda o resultado
    saudacao = obter_saudacao()
    # Mostra a saudação na tela
    print(saudacao)

# Verifica se este arquivo está sendo executado diretamente (não importado como módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()