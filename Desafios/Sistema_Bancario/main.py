import textwrap

def menu():
    menu = '''\n
    ================= MENU =================
    [0] - Sair
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Nova Conta
    [5] - Listar Contas
    [6] - Novo Usuário
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito < 0:
        print('\n@@@ Erro na operação! O valor informado é inválido. @@@')
    else:
        saldo += valor_deposito
        extrato += f'+ R$ {valor_deposito}\n'
        print('\n=== Depósito realizado com sucesso ===')
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print('\n@@@ Erro na operação, limite de saques excedidos. @@@')
    elif valor_saque > saldo:
        print('\n@@@ Erro na operação, limite insuficiente. @@@')
    elif valor_saque > limite:
        print('\n@@@ Erro na operação, excedeu o valor limite por saque. @@@')
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f'- R$ {valor_saque}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Erro na operação, valor inválido. @@@')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f'Extrato: \n{extrato}\nSaldo: {saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n @@@ Falha na criação, já existe usuário para esse CPF! @@@')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf':cpf, 'endereco':endereco})

    print ('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n === Conta criada com Sucesso! ===')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}

    print('\n@@@ Falha na criação de conta, usuário inexistente! @@@')        
    
    return

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor_deposito = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == '2':
            valor_saque = float(input('Digite o valor do saque: '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == '5':
            listar_contas(contas)
        
        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '0':
            break

        else:
            print('Operação, ínvalida, por favor selecione novamente a operação desejada.')

main()        