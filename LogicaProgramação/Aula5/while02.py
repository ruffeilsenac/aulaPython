x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor do y: "))


while x != y:
    #verifica a ordem
    if x < y:
        print("Ordem crescente")
    else:
        print("Ordem decrescente")

    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    
    