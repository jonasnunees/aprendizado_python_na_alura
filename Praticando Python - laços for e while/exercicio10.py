def verificar_usuario():
    usuario = input('Digite seu nome de usuário: ')

    while len(usuario) < 5:
        print('\nNome de usuário muito curto... mínimo de 5 caracteres')
        usuario = input('Digite seu nome de usuário: ')


def verificar_senha():
    senha = input('Digite sua senha: ')

    while len(senha) < 8:
        print('\nSenha muito curta... mínimo de 8 caracteres')
        senha = input('Digite sua senha: ')

verificar_usuario()
verificar_senha()

print('\nCadastro realizado com sucesso!')