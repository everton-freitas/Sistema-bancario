def menu():
    menu = """
    digite a opcao que voce deseja
    ================MENU====================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar usuario
    [5]\tCriar conta
    [6]\tlistar contas
    [0]\tSair
    ========================================
    => """
    return input(menu)

def depositar(saldo,valor, extrato, /):
    
    if valor > 0:

        saldo = saldo + valor
        extrato += f"depositado:\tR${valor:.2f}\n"
        print("=== valor depositado com sucesso! ===")
    else:
        print("@@@valor invalido! tente novamente. @@@")

    return saldo, extrato
    
def sacar(*, valor, saldo,extrato, numero_saque, limite_saque, limite):

    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saque:
        print("\n@@@ numero maximo de saque diario atingido. @@@")
    
    elif excedeu_limite:
        print(f"\n@@@ limite maximo por saque atingido (limite: R${limite:.2f}) @@@")

    elif excedeu_saldo:
        print(f"\n@@@ voce nao tem saldo suficiente para efetuar esse saque (seu saldo: R${saldo:.2f}) @@@")

    elif valor > 0:

        saldo = saldo - valor
        extrato += f"sacado:\t\tR${valor:.2f}\n"
        numero_saque = numero_saque + 1
        print("=== valor sacado com sucesso! ===")  

    else:
        print("@@@ valor invalido! por favor tente novamente. @@@")

    return saldo, extrato

def exibir_extrato(extrato, /, *, saldo):

    print("================== EXTRATO ================")
    print("voce ainda nao tem historico de transacao." if not extrato else extrato)
    print(f"\nsaldo atual:\t{saldo:.2f}")
    print("===========================================")

def criar_usuario(usuarios):
    
    cpf = input("informe seu cpf (somente numeros):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ ja existe usuario com esse CPf! @@@")

    nome = input("informe seu nome completo: ")
    data_nascimento = input("infome data de nascimento (dd/mm/aaaa): ")
    endereco = input("informe seu endereco (rua, numero - bairro - cidade/estado):")

    usuarios.append({"nome": nome, "data_nascimento" : data_nascimento, "endereco": endereco})

    print("=== usuario cadastrado com sucesso! ===")

def filtrar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios, numero_conta, agencia):

    cpf = input("digite seu cpf (somente numeros):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== conta criada com sucesso! ===")
        return {"usuario":usuario, "numero_conta": numero_conta, "agencia": agencia }
    
    
    print("@@@ usuario nao encontrado! @@@")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
        Agencia:\t{conta["agencia"]}
        C\C:\t\t{conta["conta"]}
        Titular:\t{conta["usuario"]} 
        """
        print("=" * 100)
        print(linha)

def main():
    AGENCIA = "0001" 
    limite_saque = 3   
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    contas = []
    usuarios = []

    while True:
        
        opcao = menu()

        if opcao == "1":
            
            valor = float(input("informe o valor que voce deseja depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":

            valor = float(input("informe o valor que voce deseja sacar: "))
            
            saldo, extrato = sacar(valor= valor, saldo= saldo,extrato= extrato, numero_saque = numero_saque, limite_saque = limite_saque, limite= limite,)
        
        elif opcao == "3":

            exibir_extrato(extrato, saldo=saldo)

        elif opcao == "4":

            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(usuarios, numero_conta, AGENCIA)

            if conta:
                contas.append(conta)

        elif opcao == "6":

            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("operacao invalida, por favor selecione novamente a opcao desejada.")

main()
