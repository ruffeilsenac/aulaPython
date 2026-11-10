# tabuada:

#entrada do número:
N = int(input("Digite um número inteiro: "))

# Estrutura for para gerar a tabuada
for i in range(1, 11, 2):
    resultado = N * i
    print(f"{N} x {i} = {resultado}")