aluno = {
    "nome": "Carlos",
    "idade": 20,
    "curso": "DS"
}

print("Mostrando as chaves:")
for chave in aluno.keys():
    print(chave)


#Percorrendo os valores:
print("Mostrando os valores:")
for valor in aluno.values():
    print(valor)

#Percorrendo chave e valor:
print("Mostrando chave e valor:")
for chave, valor in aluno.items():
    print(chave, ":", valor)
