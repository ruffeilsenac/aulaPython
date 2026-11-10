nome  = "Maria"

def saudacao():
    mensagem = f"Olá {nome}!"
    return mensagem

def somar(a, b):
    resultado = a + b
    return resultado

print(saudacao())

total = somar(5, 3)
print("Resultado da soma:", total)

