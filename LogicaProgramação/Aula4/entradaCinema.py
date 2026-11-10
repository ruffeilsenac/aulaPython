#Um cinema possui as seguintes regras: 
#• Menores de 12 anos não podem assistir a um filme de classificação 16 anos. 
#• Pessoas com 12 a 15 anos precisam estar acompanhadas de um responsável. 
#• Pessoas com 16 anos ou mais podem entrar sozinhas. 
#Solicite a idade e se a pessoa está acompanhada de um responsável (sim ou não). Informe se a entrada é permitida. 

idade = int(input("Idade: "))
acompanhante = (input("Tem acompanhante? "))

if idade < 12:
    print("barrado!")
elif idade < 16 and acompanhante == "sim":
    print("pode entrar!")
elif idade < 16 and acompanhante == "não":
    print("não pode entrar!")

else:
    print("liberado")