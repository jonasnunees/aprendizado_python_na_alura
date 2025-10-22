from datetime import datetime

data_e_hora = datetime.now()

hora_atual = data_e_hora.time()

if hora_atual.hour >= 8 and hora_atual.hour <= 18:
    print('Está no seu horário, pode entrar.')
else:
    print('Acesso negado!')