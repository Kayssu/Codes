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

#Primeira rotação para os pesados e leves receberem valor
    if cadastrados == 0:
        pesados.append(nomepeso[:])
        leves.append(nomepeso[:])

#Apartir da segunda rotação pra saber se são mais pesados ou leves e mudarem os valores anteriores
    #Pesados:
    if cadastrados >= 1:
        if pesados > pessoas and pesados > leves:
            pesados.clear()
            pesados.append(nomepeso[:])
    #Leves:
        elif leves < pessoas:
            leves.clear()
            leves.append(nomepeso[:])


    cadastrados += 1
    nomepeso.clear()

#Rotação de confirmar caso o User digite algo diferente de S/N
    confirmar = input("Deseja continuar? [S/N] ").upper().strip()
    while confirmar != "S" and confirmar != "N":
        confirmar = input("Digite apenas: [S/N] ").upper().strip()
        if confirmar == "S" or confirmar == "N":
            break

print(f"Foram cadastradas {cadastrados} pessoas.")
print(f"O maior peso foi de {float(pesados[0][1])}kg. Peso de {pesados[0][0]}.")
print(f"O menor peso foi de {float(leves[0][1])}kg. Peso de {leves[0][0]}.")
