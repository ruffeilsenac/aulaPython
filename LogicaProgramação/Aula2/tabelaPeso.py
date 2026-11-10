#tabela:
#abaixo de 18.5 and 24.9 ==> abaixo do peso
#entre 18.5 and 24.9 ==> peso normal
#entre 25.0 ==> 29,9 sobrespeso
#30.0 or > ==> obesidade
#formula: IMC = PESO / (ALTURA * ALTURA)

altura = float(input('digite a altura: '))
peso = float(input('digite o peso: '))

imc = peso / (altura**2)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('abaixo do peso')
elif imc >= 25.5 and imc >= 18.5:
    print('peso normal')
elif imc < 30.0 and imc >= 25.0:
    print('sobrepeso')
else:
    print('obesidade')
    