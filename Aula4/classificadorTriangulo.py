a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if a <= 0 or b <= 0:
    print("As medidas devem ser positivas.")
elif a >=  b + c or b >= a + c or c >= a + b:
    print("Essas madidas não formam um triangulo")
elif a == b and b == c:
    print("Triângulo equiláterio.")
elif a == b or a == c or b == c:
    print("Triângulo isóceles.")
else:
    print("Triângulo escaleno")