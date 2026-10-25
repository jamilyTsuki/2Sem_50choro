numeros = [8, 5, 2, 9, 1, 6, 3, 7, 4, 10]

for i in range(len(numeros)):
    menor_indice = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor_indice]:
            menor_indice = j

    numeros[i], numeros[menor_indice] = numeros[menor_indice], numeros[i]

print("Lista ordenada:")
print(numeros)