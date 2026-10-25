soma = 0
numero = int(input("Digite um número (0 para encerrar): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para encerrar): "))

print("A soma dos números informados é:", soma)