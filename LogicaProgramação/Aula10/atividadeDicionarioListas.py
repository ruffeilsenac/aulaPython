# acessar dados carlos:

alunos = [
    {
        "nome": "Ana",
        "idade": 18,
        "curso": "desenvolvimento de Sistemas"
    },
    {
        "nome": "Carlos",
        "idade": 20,
        "curso": "Redes de Computadores"
    },

    {
        "nome": "Mariana",
        "idade": 19,
        "curso": "Desenvolvimento de Sistemas"
    }
]

print(alunos)
print(alunos[1]["idade"])  # acessando a idade do segundo aluno
print(alunos[2]["curso"])  # acessando o curso do terceiro aluno

# trocar cruso do Carlos de rede de computador para BD
alunos[1]["cursos"] = "Banco de Dados"


# adicionando alunos
novo_aluno = {
    "nome": "João",
    "idade": 22,
    "curso": "Banco de Dados"
}

alunos.append(novo_aluno)
print(alunos) # Mostrando a lista de alunos atualizada

