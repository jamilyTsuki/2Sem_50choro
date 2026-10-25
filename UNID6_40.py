numeros = [12, 8, 45, 23, 67, 34, 89, 15, 56, 78,
           10, 92, 41, 17, 38, 64, 29, 81, 53, 7]

menor = numeros[0]
indice = 0

for i in range(len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
        indice = i

print("Menor valor:", menor)
print("Índice:", indice)