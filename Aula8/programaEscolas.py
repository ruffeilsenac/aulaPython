alunos = []


while  True:
    print("\n=== CONTROLE DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - listar alunos")
    print("3 - Persquisar aluno")
    print("4 - Remover aluno")
    print("5 - Qauntidade de alunos cadastrados")
    print("6 - Organizar alunos")
    print("7 - Encerrar")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 7:
        print("Encerrando o programa...")
        break
    elif opcao == 1:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
        print("Aluno cadastrado com sucesso!")
    elif opcao == 2:
        print("Lista de alunos cadastrados:")
        for aluno in alunos:
            print(aluno)
    elif opcao == 3:
        nome = input("Digite o nome do aluno a ser pesquisado: ")
        if nome in alunos:
            print(f"Aluno {nome} encontrado!")
        else:
            print(f"Aluno {nome} não encontrado!")
    elif opcao == 4:
        nome = input("Digite o nome do aluno a ser removido: ")
        if nome in alunos:
            alunos.remove(nome)
            print(f"Aluno {nome} removido com sucesso!")
        else:
            print(f"Aluno {nome} não encontrado!")
    elif opcao == 5:
        print(f"Quantidade de alunos cadastrados: {len(alunos)}")
    elif opcao == 6:
        alunos.sort()
        print("Alunos organizados em ordem alfabética:")
        for aluno in alunos:
            print(aluno)
    else:
        print("Opção inválida!")