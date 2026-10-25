votos1 = 0
votos2 = 0
votos3 = 0

while True:
    print("\n1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("0 - Encerrar votação")

    voto = int(input("Digite seu voto: "))

    if voto == 0:
        break
    elif voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    else:
        print("Voto inválido!")

print("\nResultado da votação:")
print("Candidato 1:", votos1, "votos")
print("Candidato 2:", votos2, "votos")
print("Candidato 3:", votos3, "votos")