soma = 0
quantidade = 0

nota = float(input("Digite uma nota (-1 para encerrar): "))

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input("Digite uma nota (-1 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
    print("Média das notas:", media)
else:
    print("Nenhuma nota válida foi informada.")