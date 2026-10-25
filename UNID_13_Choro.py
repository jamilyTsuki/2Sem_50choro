while True:
    numero = int(input("Digite um número positivo: "))

    if numero > 0:
        print("Número válido:", numero)
        break

    print("Valor inválido. Tente novamente.")