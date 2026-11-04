saldo = 1000

print('=====CAIXA ELETRÔNICO======')
print('1- consultar saldo')
print('2 - realizar deposito')
print('3 - realizar saque')
print('4 - sair')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        print('Saldo disponivel', saldo)
    case 2:
        deposito = float(input('digite o deposito: '))
        if deposito <= 0:
            print('valor invalido')
        else:
            saldo = deposito + saldo
            print(f'{saldo}')
    case 3:
        saque = float(input('valor do saque: '))
        if saldo <= saldo:
            saldo = saldo - saque
            print(f'saque realizado {saque}')
            print(f'novo saldo:{saldo:.2f}')
    case 4:
        print('obrigado')
    case _:
        print('opção invalida!')