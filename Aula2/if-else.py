

nota1 = float(input('rimeira avaliação:'))
nota2 = float(input('Segunda avaliação: '))
nota3 = float(input('Terceira avaliação: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Aluno aprovado média {media:.2}')

elif media >= 6.0:
    print(f'Recuperação média {media:.2}')

else:
    print(f'Aluno reprovado média {media:.2}')
    