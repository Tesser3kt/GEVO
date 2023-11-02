with open('input.txt', 'r', encoding='utf-8') as f:
    M, N = tuple(map(int, f.readline().split()))
    pozice_krtin = list(map(int, f.readline().split()))

vzdalenosti_krtin = [pozice_krtin[i] - pozice_krtin[i - 1]
                     for i in range(1, len(pozice_krtin))]

soucet_vzdalenosti = 0
pocet_kopancu = 0
for index, vzdalenost in enumerate(vzdalenosti_krtin):
    if vzdalenost > M - 1:
        continue
    soucet_vzdalenosti += vzdalenost
    if soucet_vzdalenosti >= M - 1:
        if index == len(vzdalenosti_krtin) - 1:
            soucet_vzdalenosti -= M - 1
        else:
            soucet_vzdalenosti = 0
        pocet_kopancu += 1

if soucet_vzdalenosti > 0:
    pocet_kopancu += 1

print(pocet_kopancu)
print(vzdalenosti_krtin)
