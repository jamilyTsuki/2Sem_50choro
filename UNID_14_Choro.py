while True:
    nome = input("Digite o nome do aluno: ")
    print("Aluno cadastrado:", nome)

    continuar = input("Deseja continuar? (s/n): ")

    if continuar.lower() != "s":
        break

print("Cadastro encerrado.")