
# Um sistema possui dois perfis: admin e funcionário. Solicite o usuário, a senha e o perfil desejado. 

# Considere o usuário sistema, a senha abc123 e os perfis válidos admin e funcionario. 

#O acesso deve ser autorizado somente quando o usuário e a senha estiverem corretos e o 

# perfil for válido. Se as credenciais estiverem corretas, mas o perfil for inválido, informe isso. 

# Nos demais casos, negue o acesso. 


usuario = input("Usuário: ")
senha = input("Senha: ")
perfil = input("Perfil (admin/funcionario): ").lower()

if usuario == "sistema" and senha == "abc123":
    if perfil == "admin" or perfil == "funcionario":
        print("Acesso autorizado: ")
        print(f"Perfil {perfil}")
    else:
        print("Perfil ineválido!")
else:
    print("Usuário ou senha incorretos")

    
