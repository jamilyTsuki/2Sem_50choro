numeros = [8, 5, 2, 9, 1, 6, 3, 7, 4, 10]

for i in range(1, len(numeros)):
    chave = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > chave:
        numeros[j + 1] = numeros[j]
        j -= 1

    numeros[j + 1] = chave

    print(f"Passo {i}: {numeros}")

print("\nLista ordenada:")
print(numeros)