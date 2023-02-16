ceny = [499, 599, 499, 479]
doprava = [79, 0, 99, 139]

nejmensi_cena = 0
for i in range(len(ceny)):
    nejmensi_cena = nejmensi_cena + ceny[i] + doprava[i]

print(nejmensi_cena)
