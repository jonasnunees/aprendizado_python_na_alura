nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
nota_3 = float(input('Terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 5:
    print(f'\nA média do aluno foi {media:.1f} e ele está reprovado.')
elif media < 7:
    print(f'\nA média do aluno foi {media:.1f} e ele está de recuperação.')
elif media <= 10:
    print(f'\nA média do aluno foi {media:.1f} e ele está aprovado.')