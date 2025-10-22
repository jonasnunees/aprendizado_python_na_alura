# Função que vai verificar se a palavra digitada pelo usuário é válida
def obter_palavra():

    # Loop infinito que só será interrompido quando uma palavra válida for digitada
    while True:

        # Solicita que o usuário digite uma palavra
        # strip() remove espaços em branco no início e fim da palavra
        palavra_digitada = input("Digite uma palavra (apenas letras): ").strip()
        
        # Verifica se o usuário digitou algo
        # Se palavra_digitada estiver vazia, mostra erro e continua o loop
        if not palavra_digitada:
            print("Erro: Você não digitou nada!\n")
            continue
        
        # Verifica se existe espaço na palavra digitada
        # Se existir espaço, significa que foi digitada mais de uma palavra
        if ' ' in palavra_digitada:
            print("Erro: Digite apenas UMA palavra, sem espaços!\n")
            continue
        
        # isalpha() verifica se todos os caracteres são letras do alfabeto
        if palavra_digitada.isalpha():

            # len() conta quantos caracteres tem na palavra
            tamanho = len(palavra_digitada)

            # Mostra a palavra e seu tamanho
            # Se tamanho for diferente de 1, adiciona 's' na palavra 'letra'
            print(f"A palavra '{palavra_digitada}' possui {tamanho} letra{'s' if tamanho != 1 else ''}!")

            # Retorna a palavra válida e sai da função
            return palavra_digitada
        
        # Se chegou aqui, significa que a palavra tem números ou caracteres especiais
        else:
            print("Erro: A palavra deve conter apenas letras do alfabeto!\n")

# Função principal do programa
def main():

    # Chama a função e exibe o resultado
    obter_palavra()

# Verifica se este arquivo está sendo executado diretamente
# Se sim, chama a função main()
if __name__ == "__main__":
    main()