soma = 0

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))

    if i == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota

        if nota < menor:
            menor = nota

    soma += nota

media = soma / 10

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média da turma:", media)