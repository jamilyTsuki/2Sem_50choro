numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

ordenados = sorted(numeros)

print("Números em ordem crescente:")
print(ordenados)