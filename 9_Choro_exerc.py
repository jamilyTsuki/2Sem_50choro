numero = int(input("Digite um número inteiro não negativo: "))

fatorial = 1

while numero > 0:
    fatorial *= numero
    numero -= 1

print("Fatorial =", fatorial)