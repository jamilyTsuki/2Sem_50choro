estoque = int(input("Quantidade inicial em estoque: "))

while estoque > 0:
    retirada = int(input(f"Estoque atual: {estoque}. Quantidade para retirar: "))

    if retirada <= estoque:
        estoque -= retirada
        print("Retirada realizada.")
    else:
        print("Quantidade indisponível em estoque.")

print("Estoque zerado.")