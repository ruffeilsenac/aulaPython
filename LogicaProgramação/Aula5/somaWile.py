numero = int(input("Digite um númeor: "))
soma = 0
contador = 1

while numero != 0:
    soma = soma + numero 
    contador = contador + 1

    numero = int(input("Digite outro número: "))


media = soma / contador

print(f"Soma total: {soma}")
print(f"Soma total: {contador}")
print(f"A média dos valores é igual a: {media}")