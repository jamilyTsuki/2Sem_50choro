palavra = input("Digite uma palavra: ")

vogais = 0

for letra in palavra.lower():
    if letra in "aeiou":
        vogais += 1

print("Quantidade de vogais:", vogais)
