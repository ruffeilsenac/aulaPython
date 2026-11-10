#Chave já existente, o valor será alterado:

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "curso": "Desenvolvedor de Sistemas"
}

print(aluno)
aluno["idade"] = 21


#chave não existente, o valor será adicionado:
aluno = {
    "nome": "Carlos",
    "idade": 20
}

aluno["curso"] = "Programador"
print(aluno)
