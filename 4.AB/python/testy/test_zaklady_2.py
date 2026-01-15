# Úloha 1
# V seznamu "cisla" nahraďte poslední prvek číslem 99 a vytiskněte druhý prvek
# ZEZADU.
cisla = [3, -1, 7, 0, 12]



# Úloha 2
# Ve slovníku "sklad" jsou údaje o ceně a počtu kusů. Spočtěte celkovou hodnotu
# skladu, čili součet cena * kusy přes všechny položky na skladě.
sklad = {
    "mys": {"cena": 250, "kusy": 6},
    "klavesnice": {"cena": 799, "kusy": 3},
    "monitor": {"cena": 3490, "kusy": 2}
}



# Úloha 3
# Máte cenu nákupu, typ zákazníka a informaci, zda má kupón. Určete výslednou
# cenu "finalni_cena" podle pravidel:

# Pravidla:
# 1) Základní sleva podle typu zákazníka:
#    - "student"  -> 10 %
#    - "senior"   -> 15 %
#    - "bezny"    -> 0 %
#
# 2) Pokud má kupón (ma_kupon == True), přidejte další slevu 5 %.
#
# Vytiskněte finální cenu na základě proměnných níže.

cena = 1240
typ = "student"
ma_kupon = True
