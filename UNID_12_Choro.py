while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Programa encerrado.")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", n1 + n2)
    elif opcao == 2:
        print("Resultado:", n1 - n2)
    elif opcao == 3:
        print("Resultado:", n1 * n2)
    else:
        print("Opção inválida!")