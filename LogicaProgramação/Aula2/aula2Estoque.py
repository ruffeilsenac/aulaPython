# print / tipy / inpu
#1 nome do produto (texto)
#Quantidade em estoque (inteiro)
#Preço unitário ( Decimal)

#Requisito: Ao final, exiba as informações capturadas e utilize a função Type() para auditar e provar que 
#os tipos corretos foram aplicados

produto = str(input('Digite nome do produto: '))
estoque = int(input(' Qual é a q2uantidade e estoque: '))
preco_unit = float(input('digite preço unitário: '))

print(produto, estoque, preco_unit)
print(f'produto {produto}, estoque {estoque}, preço unitário {preco_unit}')
print(type(produto))
