#Aluno José Fernando

#programa para informar o consumo médio de combustivel gasto por km rodado

# variaveis: 'km' para distancia percorrida / 
# 'consumo' para a quantidade consumida rm litros / '
# conMedio' para consuno médio
#

km = float(input('Digite a distancia percorrida em km: '))
consumo = float(input('Digite o consumo médio em litros:'))


conMedio = (km / consumo) 

print(f'A média consumida foi de:{conMedio:.2f}')
print(type(conMedio))

if conMedio >= 12:
    print('consumo alto')
elif conMedio <= 15:
    print('consumo normal')
elif conMedio > 15:
    print('consumo baixo')


