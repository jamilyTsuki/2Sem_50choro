soma = 0
quantidade = 0

for i in range(10):
    nota = float(input(f"Digite a {i+1}ª nota: "))

    if nota < 0 or nota > 10:
        continue

    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print("Média das notas válidas:", media)
else:
    print("Nenhuma nota válida foi informada.")