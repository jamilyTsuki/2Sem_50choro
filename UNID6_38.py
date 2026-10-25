numeros = [10, 25, 30, 45, 50, 75, 80]

valor = int(input("Digite um valor: "))

encontrado = False

for i in range(len(numeros)):
    if numeros[i] == valor:
        print("Valor encontrado no índice:", i)
        encontrado = True
        break

if not encontrado:
    print("Valor não encontrado.")