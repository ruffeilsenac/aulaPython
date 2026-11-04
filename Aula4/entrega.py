compra = float(input("Valor da compra R$: "))
regiao = input("Região Central / periferica): ")

if compra <=0:
    print("Valor de compra inválido: ")

elif regiao != "central" and regiao != "periferica":
    print("Região inválida.: ")

elif compra >= 200:
    frete = 0
    print("Você ganhou frete grátis!")
    print(f"Frete: R$ {frete:.2}")
    print(f"Total: R$ {compra + frete:.2f}")
    