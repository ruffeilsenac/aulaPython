# Aluno: José Fernando Leite Ruffeil Júnior.


#cálculo do valor cobrado pelos veículos.


#registrar a entrada e a saída de veículos, calculando o valor a ser pago de acordo com o 
#tempo de permanência

#1.	Registrar entrada de veículo.

#2.	Registrar saída de veículo.

#3.	Consultar quantidade de veículos registrados.

#4.	Encerrar sistema.

#criar variáveis para cada vaga que acumulem horas e valor por hora:

#veiculos = 0
#opcao = 0

#while opcao != 4:

 #   print("=====ESTACIONAMENTO=====")
  #  print("1 - Registrar entrada")
   # print("2 - Registrar saída")
    #print("3 - Consultar veículos")
    #print("4 - Encerrar")

    #opcao= int(input("ESCOLHA: "))

    #if opcao == 1:
     #   veiculos += 1
      #  print("Entrada registrada")
    #elif opcao == 2:
     #   if veiculos == 0:
      #   print("Não existem veículos estacio0nados!")
       # else:
        #    horas = int(input("Quantas horas permaneceu?"))
         #   if horas <= 0:
          #      print("Tempo inválido")
           # elif horas == 1:
            #    valor = 10

             #   veiculos -= 1
              #  print(f"Valor a pagar: R$ {valor:.2f}")
            #else:
             #   valor = 10 + (horas - 1 ) * 5

        #veiculos -= 1
        #print(f"Valor a pagar: R$ {valor:.2f}")



# PROGRAMA PARA LANCHONETE:

# variável para armazenar o total do pedido


#total = 0

# #while True:
#     print("\n=== CARDÁPIO ===")
#     print("1 - Hambúrguer - R$18,00")
#     print("2 - X-Bacon - R$22,00")
#     print("3 - Batata frita - R$12,00")
#     print("4 - Refrigerante - R$7,00")
#     print("5 - Finalizar pedido")

#     codigo = int(input("Escolha um código: "))

#     if codigo == 5:
#         break

#     match codigo:
#         case 1:
#             preco = 18

#         case 2:
#             preco = 22

#         case 3:
#             preco = 12

#         case 4:
#             preco = 7

#         case _:
#             print("Código inválido!")
#             continue

#     quantidade = int(input("Digite a quantidade: "))

#     if quantidade <= 0:
#         print("Quantidade inválida! Digite um valor maior que zero.")
#         continue

#     subtotal = preco * quantidade
#     total += subtotal

#     print(f"Subtotal: R$ {subtotal:.2f}")

#print(f"\nValor total do pedido: R$ {total:.2f}")
#print("Pedido finalizado!")



#Controle de estoque de uma loja

# Atividade – Controle de estoque de uma loja
# Contexto: uma loja de informática precisa de um sistema simples para acompanhar o estoque de seus produtos.
# Desenvolva um programa que permita controlar a quantidade de produtos disponíveis em estoque.
# O sistema deverá apresentar o seguinte menu:


# 1.	Registrar entrada de produtos.
# 2.	Registrar saída de produtos.
# 3.	Consultar estoque.
# 4.	Verificar situação do estoque.
# 5.	Encerrar.


# O estoque inicial será de 20 unidades.
# Regras:


# •	A entrada deverá aumentar a quantidade disponível.
# •	A saída deverá diminuir a quantidade disponível.
# •	Não permitir retirar uma quantidade maior do que a disponível.
# •	Não aceitar quantidades menores ou iguais a zero.
# •	Na consulta, apresentar a quantidade atual.
# •	Na situação do estoque:
# o	Quantidade igual a zero: Estoque zerado.
# o	Quantidade entre 1 e 5: Estoque crítico.
# o	Quantidade acima de 5: Estoque normal.


# estoque = 20

# while True:
#     print("\n=== CONTROLE DE ESTOQUE ===")
#     print("1 - Registrar entrada")
#     print("2 - Registrar saída")
#     print("3 - Consultar estoque")
#     print("4 - Verificar situação")
#     print("5 - Encerrar")

#     opcao = int(input("Escolha uma opção: "))

#     match opcao:
#         case 1:
#             quantidade = int(input("Quantidade de entrada: "))

#             if quantidade <= 0:
#                 print("Quantidade inválida!")
#             else:
#                 estoque += quantidade
#                 print("Entrada registrada!")

#         case 2:
#             quantidade = int(input("Quantidade de saída: "))

#             if quantidade <= 0:
#                 print("Quantidade inválida!")

#             elif quantidade > estoque:
#                 print("Estoque insuficiente!")

#             else:
#                 estoque -= quantidade
#                 print("Saída registrada!")

#         case 3:
#             print(f"Estoque atual: {estoque} unidades")

#         case 4:
#             if estoque == 0:
#                 print("Estoque zerado.")

#             elif estoque <= 5:
#                 print("Estoque crítico.")

#             else:
#                 print("Estoque normal.")

#         case 5:
#             print("Sistema encerrado.")
#             break

#         case _:
#             print("Opção inválida!")