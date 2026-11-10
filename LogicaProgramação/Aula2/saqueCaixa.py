saldo = float(input('Digite o seu saldo: '))
saque = float(input('Digite o valor do saque: '))

if saque <= saldo:
    print('saque realizado')
    
    print('Novo saldo:', saldo)

else:
    print('Saldo insuficiente')
