ceny = [499, 599, 499, 479]
doprava = [79, 0, 99, 139]

nejmensi_cena = 999999
for cena_produktu, cena_dopravy in zip(ceny, doprava):
    if cena_produktu + cena_dopravy < nejmensi_cena:
        nejmensi_cena = cena_produktu + cena_dopravy

print(nejmensi_cena)
