den_dnes = 29
mesic_dnes = 7
rok_dnes = 2023

den_uzivatel = int(input("Zadej den narozeni: "))
mesic_uzivatel = int(input("Zadej mesic narozeni: "))
rok_uzivatel = int(input("Zadej rok narozeni: "))

vek = rok_dnes - rok_uzivatel
if mesic_dnes < mesic_uzivatel:
    vek -= 1
elif mesic_dnes == mesic_uzivatel and den_dnes < den_uzivatel:
    vek -= 1

print("Je vam", vek, "let.")