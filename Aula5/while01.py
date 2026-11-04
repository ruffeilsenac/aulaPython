while True:
    #entrada de valores
    x = int(input("Digite o valor do x: "))
    y = int(input("Digite o valor do y: "))

    #verifica se os valores são iguais
    if x == y:
        print("Vaores iguais. Programa encerrado!")
        break
    #verifica a ordem
    elif x < y:
        print("Ordem crescente")
    else:
        print("Ordem decrescente")