numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,
           32, 35, 38, 41, 44, 47, 50, 53, 56, 59]

valor = int(input("Digite o número que deseja buscar: "))

inicio = 0
fim = len(numeros) - 1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2

    if numeros[meio] == valor:
        print("Número encontrado no índice", meio)
        encontrado = True
        break
    elif valor < numeros[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

if not encontrado:
    print("Número não encontrado.")