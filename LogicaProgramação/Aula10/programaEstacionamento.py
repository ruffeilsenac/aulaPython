estacionamento = {}

opcao = 0

while opcao !=4:

    print("\n=====ESTACIONAMENTO=====")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Consultar veículos")
    print("4 - Encerrar")

    opcao = int(input("Escolha: "))

    #REGISTRAR ENTRADA

    if opcao == 1:
        placa = input("Digite a placa: ").upper()

        if placa in estacionamento:
            print("Este veículo já está cadastrado: ")
        else:
            modelo = input("Digite o modelo do veículo:")

            estacionamento[placa] = {
                "modelo": modelo
            }

            print("Entrada registrada com sucesso!")

    # Registrar saída:
    elif opcao == 2:
        placa = input("Digite a placa do veículo: ").upper()

        if placa not in estacionamento:
            print("Veiculo não encontrado!")
        else:
            horas = int(input("Quantas horas permaneceu?"))

            if horas <= 0:
                print('tempo inválido')
            else:
                if horas == 1:
                    valor = 10
                else:
                    valor = 10 + (horas - 1) * 5

                print("\n====COMPROVANTE====")
                print(F"Placa: {placa}")
                print(f'{estacionamento[placa][modelo]}')
                print(f"Horas: {horas}")
                print(f"Valor a pagar: R$ {valor:.}")

                del estacionamento[placa]

    elif opcao == 3:
        if len(estacionamento) == 0:
            print("Estacionamento vazio!")
        else:
            print("\n====VEÍCULOS ESTACIONADOS====")
            for placa, dados in estacionamento.items():
                print(f"\nPlaca: {placa}")
                print(f"Modelo:{dados['modelo']}")

            print(f"\nTotal de veículos: {len(estacionamento)}")

    elif opcao == 4:
        print("Sistema encerrado!")
    else:
        print("Opção inválida!")