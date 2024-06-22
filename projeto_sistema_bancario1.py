menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair   
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input('digite o valor que voce deseja depositar:'))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("valor invalido, por favor tente novamente.")

    elif opcao == "2":
        valor = float(input('d1igite o valor que voce deseja sacar:'))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao falhou! valor desejado e maior que o seu saldo atual.")

        elif excedeu_limite:
            print("Operacao falhou! valor desejado excedeu o limite de saque da sua conta. [limite: R$ 500.00]")
        
        elif excedeu_saque:
            print("Operacao falhou! o limite de saques diarios foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operacao falhou! o valor informado e invalido.")

    elif opcao == "3":
        print('\n============Extrato============')
        print('Nao foram realizadas movimentacoes' if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "0":
        break
    
    else:
        print("operacao invalida, por favor selecione novamente a operacao desejada.")

