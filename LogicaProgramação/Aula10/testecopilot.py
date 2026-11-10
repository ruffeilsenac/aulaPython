VAGAS_MAXIMAS = 10
faturamento = 0

while True:

    print("\n=== ESTACIONAMENTO ===")
    print("1 - Entrada")
    print("2 - Saída")
    print("3 - Consultar")
    print("4 - Encerrar")

    opcao = input("Opção: ")

    # ENTRADA
    if opcao == "1":

        if len(estacionamento) >= VAGAS_MAXIMAS:
            print("Estacionamento lotado!")
            continue

        placa = input("Placa: ").upper()

        if placa in estacionamento:
            print("Veículo já cadastrado.")
            continue

        estacionamento[placa] = {
            "modelo": input("Modelo: "),
            "cor": input("Cor: ")
        }

        print("Entrada registrada!")

    # SAÍDA
    elif opcao == "2":

        placa = input("Placa: ").upper()

        if placa not in estacionamento:
            print("Veículo não encontrado.")
            continue

        horas = int(input("Horas estacionadas: "))

        if horas <= 0:
            print("Tempo inválido.")
            continue

        valor = 10 + (horas - 1) * 5 if horas > 1 else 10

        dados = estacionamento.pop(placa)

        faturamento += valor

        relatorio.append({
            "placa": placa,
            "modelo": dados["modelo"],
            "valor": valor
        })

        print(f"Valor a pagar: R$ {valor:.2f}")

    # CONSULTA
    elif opcao == "3":

        if not estacionamento:
            print("Nenhum veículo estacionado.")
        else:
            print("\nVeículos estacionados:")

            for placa, dados in estacionamento.items():
                print(
                    f"{placa} - "
                    f"{dados['modelo']} - "
                    f"{dados['cor']}"
                )

            print(f"\nOcupadas: {len(estacionamento)}")
            print(f"Livres: {VAGAS_MAXIMAS - len(estacionamento)}")

    # RELATÓRIO FINAL
    elif opcao == "4":

        print("\n=== RELATÓRIO FINAL ===")

        if relatorio:

            for item in relatorio:
                print(
                    f"{item['placa']} | "
                    f"{item['modelo']} | "
                    f"R$ {item['valor']:.2f}"
                )

            maior = max(item["valor"] for item in relatorio)
            media = faturamento / len(relatorio)

            print("\n=== RESUMO ===")
            print(f"Veículos atendidos: {len(relatorio)}")
            print(f"Faturamento: R$ {faturamento:.2f}")
            print(f"Maior cobrança: R$ {maior:.2f}")
            print(f"Ticket médio: R$ {media:.2f}")

        else:
            print("Nenhuma saída registrada.")

        break

    else:
        print("Opção inválida.")