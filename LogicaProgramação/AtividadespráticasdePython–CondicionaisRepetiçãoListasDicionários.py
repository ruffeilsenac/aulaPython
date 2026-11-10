livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Consultar livro")
    print("4 - Realizar empréstimo")
    print("5 - Devolver livro")
    print("6 - Exibir quantidade de livros disponíveis")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")

        if titulo == "" or autor == "":
            print("Título e autor são obrigatórios!")

        else:

            existe = False

            for livro in livros:
                if livro["titulo"].lower() == titulo.lower():
                    existe = True

            if existe:
                print("Este livro já está cadastrado!")

            else:
                ano = int(input("Ano: "))

                novo_livro = {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": ano,
                    "disponivel": True
                }

                livros.append(novo_livro)
                print("Livro cadastrado com sucesso!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        if len(livros) == 0:
            print("Nenhum livro cadastrado")

        else:

            for livro in livros:

                if livro["disponivel"]:
                    situacao = "Disponível"
                else:
                    situacao = "Emprestado"

                print("-" * 30)
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")
                print(f"Situação: {situacao}")

    elif opcao == "3":

        titulo = input("Digite o título do livro: ")

        encontrado = False

        for livro in livros:

            if livro["titulo"].lower() == titulo.lower():

                encontrado = True

                print("\nLivro encontrado!")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']}")

                if livro["disponivel"]:
                    print("Situação: Disponível")
                else:
                    print("Situação: Emprestado")

                break

        if not encontrado:
            print("Livro não encontrado!")

    elif opcao == "4":

        titulo = input("Qual livro deseja emprestar? ")

        encontrado = False

        for livro in livros:

            if livro["titulo"].lower() == titulo.lower():

                encontrado = True

                if livro["disponivel"]:
                    livro["disponivel"] = False
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("Este livro já está emprestado!")

                break

        if not encontrado:
            print("Livro não encontrado!")

    elif opcao == "5":

        titulo = input("Qual livro deseja devolver? ")

        encontrado = False

        for livro in livros:

            if livro["titulo"].lower() == titulo.lower():

                encontrado = True

                if not livro["disponivel"]:
                    livro["disponivel"] = True
                    print("Livro devolvido com sucesso!")
                else:
                    print("Este livro já está disponível!")

                break

        if not encontrado:
            print("Livro não encontrado!")

    elif opcao == "6":

        contador = 0

        for livro in livros:
            if livro["disponivel"]:
                contador += 1

        print(f"Livros disponíveis: {contador}")
        print(f"Total de livros cadastrados: {len(livros)}")

    elif opcao == "7":

        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")