def some(a, b):
    resultado = a + b 
    return  resultado
    

def multiplique(a, b):
    resultado = a * b 
    return  resultado
    
    
def subtraia(a, b):
    resultado = a - b 
    return  resultado
    

def divida(a, b):
    if b  or a == 0:
        return "Não é possível dividir por zero!"

    resultado = a / b 
    return  resultado
    


while True:

    print("====CALCULADORA====")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    print("0 - SAIR")
    

    opcao = (input("Escolha uma operação: "))


    if opcao == "0":
        print("Encerrado!")
        break


    num1 = float(input("Digite o primeiro número"))
    num2 = float(input("Digite o segundo número"))

    match opcao:
        case "1":
            print("Resultado: ", some(num1, num2))
        case "2":
            print("Resultado: ", subtraia(num1, num2))
        case "3":
            print("Resultado: ", multiplique(num1, num2))
        case "4":
            print("Resultado: ", divida(num1, num2))




