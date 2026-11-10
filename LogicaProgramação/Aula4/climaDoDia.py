#Crie um programa que solicite a temperatura atual em graus Celsius e informe a condição do clima: 

#• Menor que 18 °C: está frio. 
#• De 18 °C até 29 °C: temperatura agradável. 
#• 30 °C ou mais: está muito quente. 


temp = float(input('Digite a temperatura: '))
if temp < 18:
    print(f'está fio: {temp}')
elif temp >= 18 and  temp <= 29:
    print(f'temperatura agradável: {temp}')
else:
    print(f'está muito quente: {temp}')