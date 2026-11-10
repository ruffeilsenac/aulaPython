#fazer uma calculadora 

while True:

    print("\n=====CALCULADORA=====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir ")
    print("5 - Sair ")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Programa encerrado!")
        break
    
    elif opcao >=1 and opcao <=4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o primeiro número: "))

        if opcao == 1:
            resultado = numero1 + numero2
            print("Resultado:", resultado)
        elif opcao == 2:
         resultado = numero1 + numero2
        print("Resultado:", resultado)

    elif opcao == 3:
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    elif opcao == 4:
        resultado = numero1 + numero2
        print("Resultado:", resultado)
        if numero2 !=0:
            resultado = numero1 / numero2
            print("Resultado: ", )
