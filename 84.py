nomepeso = []
pessoas = []
confirmar = "S"
cadastrados = 0
pesados = []
leves = []
while confirmar != "N":
    nomepeso.append(str(input("Nome: ")))
    nomepeso.append(int(input("Peso: ")))
    pessoas.append(nomepeso[:])
    if cadastrados == 0:
        pesados.append(nomepeso[:])
        leves.append(nomepeso[:])


    # if cadastrados >= 1:
    #     if pesados[0][1] >= pessoas[0][1] :
    #         pesados.append(nomepeso[:])
    #     elif leves [0][1] < pessoas[cadastrados-1][1]:
    #         leves.append(nomepeso[:])


    cadastrados += 1
    nomepeso.clear()

    confirmar = input("Deseja continuar? [S/N] ").upper().strip()
    while confirmar != "S" and confirmar != "N":
        confirmar = input("Digite apenas: [S/N] ").upper().strip()
        if confirmar == "S" or confirmar == "N":
            break

print(f"Foram cadastradas {cadastrados} pessoas.")
print(f"O maior peso foi de {float(pesados[0][1])}kg. Peso de {pesados[0][0]}.")
print(f"O maior peso foi de {float(leves[0][1])}kg. Peso de {leves[0][0]}.")