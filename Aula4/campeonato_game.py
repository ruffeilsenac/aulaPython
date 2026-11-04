idade = int(input("Idade: "))
experiencia = int(input("Anos de experiencia: "))


if idade <= 0 or experiencia < 0:
    print("Dados inválidos")

elif idade < 12:
    print("Inscrição não permitida.")

elif idade < 18 and experiencia <= 2:
    print("Categoria iniciante.")

elif idade >= 18 and experiencia >=3:
    print("Categoria avançada.")

else:
    print("Encaminhado para avaliação manual.")

