numeros = [8, 5, 2, 9, 1, 6, 3, 7, 4, 10]

for i in range(len(numeros)):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:")
print(numeros)