menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Foi realizado o depósito de R$ {valor:.2f} com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*,valor, saldo, extrato, limite, num_saq):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = num_saq >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saq += 1
        print(f"Foi realizado o saque de R$ {valor:.2f} com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
                
    return saldo, extrato, num_saq

def historico_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso! ")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        print(f"""
        \nAgência:{conta['agencia']}
C/C:{conta['numero_conta']}
Titular:{conta['usuario']['nome']}
        """)


while True:

    opcao = input(menu)
    match opcao:
        case "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)

        case "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, limite=limite, num_saq=numero_saques)
            
        case "3":
            historico_extrato(saldo, extrato=extrato)

        case "4":
            criar_usuario(usuarios)

        case "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        case "6":
            listar_contas(contas)
            
        case "7":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")