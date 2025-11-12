menu = """
******************MENU ****************
[c] Nova Conta
[u] Novo Usuario
[d] Depositar
[s] Sacar
[e] Extrato
[lu] Listar Usuarios
[q] Sair

=> """
def exibir_extrato(saldo,/,*, extrato):
    mensagem = "\n================ EXTRATO ================"
    mensagem += "\nNão foram realizadas movimentações." if not extrato else f"\n{extrato}"
    mensagem += f"\nSaldo: R$ {saldo:.2f}"
    mensagem += "\n=========================================="
    
    return mensagem

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        mensagem = "\nOperação Realizada com sucesso!"

    else:
        mensagem = "Operação falhou! O valor informado é inválido."
    
    return saldo, extrato, mensagem

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    mensagem = ""

    if excedeu_saldo:
        mensagem = "Operação falhou! Você não tem saldo suficiente."
    
    elif excedeu_limite:
        mensagem = "Operação falhou! O valor do saque excede o limite."
    
    elif excedeu_saques:
        mensagem = "Operação falhou! Número máximo de saques excedido."
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        mensagem = "\nOperação Realizada com sucesso!"
    else:
        mensagem = "Operação falhou! O valor informado é inválido."

    return saldo, extrato, mensagem

def criar_conta(agencia, numero_conta, lista_usuarios):
    mensagem = ""
    conta = ""
    cpf = input("Informe o CPF do usuário: ")
    usuario = [user for user in lista_usuarios if user["cpf"] == cpf]

    if usuario:
        conta = f"Agencia: {agencia} \n Numero conta: {numero_conta} \n  Usuario: {usuario}"
        mensagem = "\n *********Conta criada com sucesso! **********\n"
        mensagem += conta
        
    else:
        mensagem = "\n**** Usuário não encontrado, Nao foi possivel criar essa conta! "
    
    return mensagem, conta

def criar_usuario(lista_usuarios):
    mensagem =""
    cpf = input("Informe o CPF (somente número): ")
    usuario = fusuario = [user for user in lista_usuarios if user["cpf"] == cpf]

    if usuario:
        mensagem = "\n***** Já existe usuário com esse CPF! *******"
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        mensagem = "***** Usuário criado com sucesso! *******"
    
    return mensagem

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    saldo = 0    
    limite = 500
    numero_conta = 0
    extrato = ""
    numero_saques = 0
    lista_contas = []
    lista_usuario = []

    while True:

        opcao = input(menu)

        if opcao == "c":
            numero_conta += 1
            mensagem,conta = criar_conta(AGENCIA, numero_conta, lista_usuario)

            if conta:
                lista_contas.append(conta)
            
            print(mensagem)                

        elif opcao == "u":
            mensagem = criar_usuario(lista_usuario)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato, mensagem = depositar(saldo, valor, extrato)

            print(mensagem)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, mensagem = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            
            print(mensagem)


        elif opcao == "e":
            print(exibir_extrato(saldo, extrato=extrato))        

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
