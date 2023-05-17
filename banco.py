saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor}\n"
        else:
            print("O valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("O valor do saque excede o limite!")
        elif excedeu_saques:
            print("Número máximo de saques excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido!")

    elif opcao == "3":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo}")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
