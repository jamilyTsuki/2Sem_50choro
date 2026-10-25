produtos = []
quantidades = []

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Buscar produto")
    print("3 - Listar produtos")
    print("4 - Ordenar produtos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")

        if nome == "":
            continue

        quantidade = int(input("Quantidade: "))

        produtos.append(nome)
        quantidades.append(quantidade)

    elif opcao == "2":
        busca = input("Digite o nome do produto: ")

        encontrado = False

        for i in range(len(produtos)):
            if produtos[i].lower() == busca.lower():
                print("Produto:", produtos[i])
                print("Quantidade:", quantidades[i])
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "3":
        for i in range(len(produtos)):
            print(produtos[i], "-", quantidades[i])

    elif opcao == "4":
        for i in range(len(produtos)):
            for j in range(i + 1, len(produtos)):
                if produtos[i].lower() > produtos[j].lower():
                    produtos[i], produtos[j] = produtos[j], produtos[i]
                    quantidades[i], quantidades[j] = quantidades[j], quantidades[i]

        print("Produtos ordenados.")

    elif opcao == "5":
        break

    else:
        print("Opção inválida.")