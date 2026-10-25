numero = int(input("Digite um número (0 para encerrar): "))

maior = numero

while numero != 0:
    if numero > maior:
        maior = numero

    numero = int(input("Digite um número (0 para encerrar): "))

print("Maior número informado:", maior)