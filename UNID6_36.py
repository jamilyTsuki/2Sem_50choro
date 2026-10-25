numeros = [5, 12, 8, 20, 15, 3, 9, 25, 18, 7]

valor = int(input("Digite um número: "))

encontrado = False

for numero in numeros:
    if numero == valor:
        encontrado = True
        break

if encontrado:
    print("Número encontrado na lista.")
else:
    print("Número não encontrado.")