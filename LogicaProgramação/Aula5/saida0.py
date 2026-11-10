#usuario precisa advinhar o numero certo que será "0"

numeroCerto = ""

while numeroCerto != "0":
    numeroCerto = input("Digite o numero certo e 0 até 5: ")
    if  numeroCerto == "0":
        print("PARABÉNS NÃO TRAVOU A MÁQUINA")
    else:
        print(" Mais uma tentativa de um número de 0 até 5: ")
