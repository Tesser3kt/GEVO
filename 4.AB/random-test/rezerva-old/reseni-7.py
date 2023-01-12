# udaje draka a prince
drak = [100000, 50, 10]
princ = [100, 5000, 45]

# opakuju, dokud jak drak, tak princ, jsou nazivu
while drak[0] > 0 and princ[0] > 0:
    # princ prasti do draka -> z hp draka odeberu damage prince
    drak[0] = drak[0] - princ[1]
    # drak prasti do prince -> z hp prince odeberu damage draka
    princ[0] = princ[0] - drak[1]

    # drak i princ se vyleci
    drak[0] = drak[0] + drak[2]
    princ[0] = princ[0] + princ[2]

# kdyz ma drak na konci souboje jeste zivoty, tak vyhral
if drak[0] > 0:
    print("Drak vyhral souboj.")
# v opacnem pripade vyhral princ
else:
    print("Princ vyhral souboj.")
