#Desconto na loja 
#Uma loja oferece descontos conforme o valor da compra: 
# • Compras de R$ 200,00 ou mais recebem 15% de desconto. 
# • Compras de R$ 100,00 ou mais recebem 10% de desconto. 
# • As demais compras não recebem desconto. 
#Clientes cadastrados no programa de fidelidade recebem mais 5 pontos percentuais de desconto, independentemente do valor da compra.
#Solicite o valor da compra e se o cliente participa do programa (sim ou não). 
# Calcule o #desconto total e o valor final.


compra = input("Digite o total da compra: ")
fidelidade = input("Tem fidelidade? ")


if compra >= 200:
    desconto = 10

elif compra >= 100:
    desconto = 10
else:
    desconto = 0
if fidelidade == "sim":
    desconto = desconto + 5

valor_desconto = compra * desconto / 100
total = compra - valor_desconto

print(f"Desconto: {desconto}%")
print(f"Valor descontado: R$ {valor_desconto:.2}")
print(f"Total a pagar: R$ {total:.2}")

