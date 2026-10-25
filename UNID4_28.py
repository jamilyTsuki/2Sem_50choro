saldo = 0

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Valor do depósito: "))
        saldo += valor

    elif opcao == 2:
        valor = float(input("Valor do saque: "))

        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente.")

    elif opcao == 3:
        print("Saldo atual:", saldo)

    elif opcao == 4:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")