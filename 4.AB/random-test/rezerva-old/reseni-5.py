seznam = ["rokle", 4, "auto", [1, 4, 5], 8]

# na zacatku si vytvorim promennou soucet, ke ktere budu postupne pricitat
# cisla z vnitrniho seznamu
soucet = 0
# vnitrni seznam je na pozici 3 (to vim ze zadani)
for cislo in seznam[3]:
    # kazdy prvek prictu k promenne soucet a vysledek ulozim zpatku do soucet
    soucet = soucet + cislo

# nakonec misto vnitrniho seznamu vlozim na pozici 3 ten soucet
seznam[3] = soucet
