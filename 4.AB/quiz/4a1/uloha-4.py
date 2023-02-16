cisla = [47, 89, 12, 544, 87, 65, 13, 2]

soucet = 0
for cislo in cisla:
    if cislo % 2 == 1:
        soucet = soucet + cislo ** 3

print(soucet)
