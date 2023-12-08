menu = '''

Selecione uma opção:
[0] - Sair
[1] - Depositar
[2] - Sacar
[3] - Extrato

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Digite o valor do depósito: '))

        if deposito < 0:
            print('Não é possível depositar valores negativos.')
        else:
            saldo += deposito
            extrato += f'+ R$ {deposito}\n'

    elif opcao == '2':

        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingido, tente novamente amanhã.')
        else:
            saque = float(input('Digite o valor do saque: '))
        
            if saque <= saldo:
        
                if saque <= 500:
                    saldo -= saque
                    extrato += f'- R$ {saque}\n'
                    numero_saques += 1
                else:
                    print('Valor do saque acima do limite de saque, tente novamente com valor menor.')
        
            else:
                print('Saldo insuficiente.')
    
    elif opcao == '3':
        print(f'Extrato: \n{extrato}\nSaldo: {saldo:.2f}')

    elif opcao == '0':
        break

    else:
        print('Operação, ínvalida, por favor selecione novamente a operação desejada.')