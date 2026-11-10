#excluindo item do dicionário:

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "cidade": "Belém"
}

print(aluno)
del aluno["idade"]

print(aluno)

#excluindo nitem do dicionário:

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "cidade": "Belém"
}

aluno.pop("idade")

print(aluno)
