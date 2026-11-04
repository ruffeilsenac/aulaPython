# Uma loja cobra R$ 15,00 de frete para compras inferiores a R$ 100,00. 
# Para compras de R$ 100,00 ou mais, o frete é gratuito. 
# Solicite o valor da compra, calcule o total com o frete e apresente o resultado. 

valor_compra = input('Digite o valor da compra: ')
frete = 15


if valor_compra < 100:
    frete = 15
else:
    frete = 0
total = valor_compra + frete

print(f'frete: R$ {frete:.2f}')
print(f'frete: R$ {total:.2f}')