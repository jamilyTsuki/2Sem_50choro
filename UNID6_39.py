numeros = [12, 8, 45, 23, 67, 34, 89, 15, 56, 78,
           10, 92, 41, 17, 38, 64, 29, 81, 53, 7]

maior = numeros[0]
indice = 0

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        indice = i

print("Maior valor:", maior)
print("Índice:", indice)