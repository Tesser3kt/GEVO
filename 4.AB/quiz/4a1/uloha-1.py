ceny = [499, 599, 499, 479]
doprava = [79, 0, 99, 139]

nejmensi_cena = 9999999
for i in range(len(ceny)):
    cena = ceny[i] + doprava[i]
    if cena < nejmensi_cena:
        nejmensi_cena = cena

print(nejmensi_cena)
