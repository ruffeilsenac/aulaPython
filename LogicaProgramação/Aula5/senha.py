senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

    if senha == "1234":
            print("Acesso permitido!")
    else:
            print("Senha incorreta. tente novamente.")