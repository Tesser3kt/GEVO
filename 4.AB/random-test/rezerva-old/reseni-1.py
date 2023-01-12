seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mam vytisknout seznam na preskacku,
# tj. v tomhle pripade 1, 10, 2, 9, 3, 8 atd.
# protoze python cisluje zepredu prvky cisly 0, 1, 2, 3, ...
# a odzadu cisly -1, -2, -3, ...
# vyuziju toho, ze chci tisknout nejdriv prvek s poradim 0, pak -1, pak 1, pak
# -2 atd.
# vsimnete si, ze z 0 na -1, z 1 na -2, z 2 na -3 atd. je to vzdycky vynasobeni
# minusem a odecteni jednicky -- to je presne to, co v tom cyklu dole delam
# musim skoncit v pulce seznamu, jinak bych ho cely vytiskl dvakrat
for poradi in range(5):
    print(seznam[poradi])
    print(seznam[-poradi-1])
