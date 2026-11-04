# < 12 criança
# < 18 adolescente
# < 60 adulto

idade = int(input('digite a idade: '))

if idade  < 12:
    print(f'criança {idade}')
elif idade < 18:
    print(f'adulto {idade}')
elif idade < 60:
    print(f'adulto')
else:
    print(f'idoso {idade}')