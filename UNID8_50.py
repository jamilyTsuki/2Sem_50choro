numeros = []

print("Cadastro de 20 números inteiros")

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

while True:
    print("\n===== MENU =====")
    print("1 - Calcular média")
    print("2 - Maior número")
    print("3 - Menor número")
    print("4 - Ordenar em ordem crescente")
    print("5 - Ordenar em ordem decrescente")
    print("6 - Busca linear")
    print("7 - Busca binária")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        soma = 0

        for numero in numeros:
            soma += numero

        media = soma / len(numeros)

        print("Média:", media)

    elif opcao == "2":
        maior = numeros[0]

        for numero in numeros:
            if numero > maior:
                maior = numero

        print("Maior número:", maior)

    elif opcao == "3":
        menor = numeros[0]

        for numero in numeros:
            if numero < menor:
                menor = numero

        print("Menor número:", menor)

    elif opcao == "4":
        crescente = sorted(numeros)

        print("Ordem crescente:")
        print(crescente)

    elif opcao == "5":
        decrescente = sorted(numeros, reverse=True)

        print("Ordem decrescente:")
        print(decrescente)

    elif opcao == "6":
        valor = int(input("Digite o número que deseja buscar: "))

        comparacoes = 0
        encontrado = False

        for i in range(len(numeros)):
            comparacoes += 1

            if numeros[i] == valor:
                print("Número encontrado no índice", i)
                print("Comparações realizadas:", comparacoes)
                encontrado = True
                break

        if not encontrado:
            print("Número não encontrado.")
            print("Comparações realizadas:", comparacoes)

    elif opcao == "7":
        valor = int(input("Digite o número que deseja buscar: "))

        lista_ordenada = sorted(numeros)

        inicio = 0
        fim = len(lista_ordenada) - 1

        comparacoes = 0
        encontrado = False

        while inicio <= fim:
            comparacoes += 1

            meio = (inicio + fim) // 2

            if lista_ordenada[meio] == valor:
                print("Número encontrado no índice", meio)
                print("Comparações realizadas:", comparacoes)
                encontrado = True
                break

            elif valor < lista_ordenada[meio]:
                fim = meio - 1

            else:
                inicio = meio + 1

        if not encontrado:
            print("Número não encontrado.")
            print("Comparações realizadas:", comparacoes)

    elif opcao == "8":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")