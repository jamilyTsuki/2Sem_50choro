alunos = []
notas = []

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar aluno")
    print("2 - Pesquisar aluno")
    print("3 - Listar alunos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        nota = float(input("Nota do aluno: "))

        alunos.append(nome)
        notas.append(nota)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome para pesquisar: ")

        encontrado = False

        for i in range(len(alunos)):
            if alunos[i].lower() == nome.lower():
                print("Aluno:", alunos[i])
                print("Nota:", notas[i])
                print("Média:", notas[i])
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "3":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for i in range(len(alunos)):
                print(f"{alunos[i]} - Nota: {notas[i]}")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
