 # importa o módulo 'os' que permite executar comandos do sistema operacional
import os  

 # importa o módulo 'time' que fornece funções relacionadas ao tempo (como pausar a execução)
import time              

# cria a variável 'contador' e inicializa com 0; será usada para controlar quantas vezes o loop roda
contador = 0              

 # inicia um loop 'while' que repete enquanto 'contador' for menor que 10
while contador < 10: 

    # executa o comando do sistema 'cls' (no Windows) para limpar a tela/terminal a cada iteração   
    # e mostra qual iteração está sendo executada (contador+1 para começar em 1) 
    os.system('cls')     

    # imprime uma mensagem no terminal mostrando que está "processando" 
    print('Processando dados... (iteração', contador+1, 'de 10)')  
                           
    # pausa a execução por 0.5 segundos (meio segundo) para que você consiga ver cada iteração                      
    time.sleep(0.5)  

    # incrementa 'contador' em 1; quando atingir 10 a condição do while será falsa e o loop termina     
    contador += 1         