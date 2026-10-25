numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,
           32, 35, 38, 41, 44, 47, 50, 53, 56, 59]

valor = int(input("Digite o valor procurado: "))

# Busca Linear
comparacoes_linear = 0

for numero in numeros:
    comparacoes_linear += 1

    if numero == valor:
        break

# Busca Binária
inicio = 0
fim = len(numeros) - 1
comparacoes_binaria = 0

while inicio <= fim:
    comparacoes_binaria += 1

    meio = (inicio + fim) // 2

    if numeros[meio] == valor:
        break
    elif valor < numeros[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

print("Comparações na busca linear:", comparacoes_linear)
print("Comparações na busca binária:", comparacoes_binaria)