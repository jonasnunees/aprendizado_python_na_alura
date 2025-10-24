# Importa apenas a classe datetime do módulo datetime para trabalhar com data e hora
from datetime import datetime

# Importa Literal do módulo typing para definir quais textos exatos a função pode retornar
from typing import Literal

# Definimos o horário de início do expediente (8 horas da manhã)
# Usamos uma constante (valor que não muda) em letras maiúsculas
HORARIO_INICIO_EXPEDIENTE = 8

# Definimos o horário de fim do expediente (18 horas = 6 da tarde)
HORARIO_FIM_EXPEDIENTE = 18

# Define uma função que verifica se o horário atual permite acesso
# -> Literal[...] indica que a função só pode retornar um desses dois textos exatos
def verificar_horario_acesso() -> Literal['Está no seu horário, pode entrar.', 'Acesso negado!']:

    # Obtém apenas a hora atual do sistema (0-23)
    # datetime.now() pega data e hora atual
    # .hour extrai só a parte da hora
    hora_atual = datetime.now().hour
    
    # Verifica se a hora atual está entre o início e fim do expediente
    if HORARIO_INICIO_EXPEDIENTE <= hora_atual <= HORARIO_FIM_EXPEDIENTE:

        # Se estiver dentro do horário, permite o acesso
        return 'Está no seu horário, pode entrar.'
    
    # Se não estiver dentro do horário, nega o acesso
    return 'Acesso negado!'

# Função principal que organiza a execução do programa
def main():

    # Chama a função de verificação e guarda o resultado
    mensagem = verificar_horario_acesso()
    
    # Mostra a mensagem na tela
    print(mensagem)

# Verifica se este arquivo está sendo executado diretamente (não importado como módulo)
# Se sim, chama a função main()
if __name__ == "__main__":
    main()