from random import random, seed

# Úloha 1 (25 %)
# Ve slovníku prices máte ceny produktů. Spočtěte celkovou cenu potravin v
# nákupním košíku cart. Tj. sečtěte dohromady ceny všech produktů v seznamu
# cart.
prices = {"bread": 39, "milk": 24, "cheese": 65, "apple": 8}
cart = ["milk", "cheese", "apple"]

# Sem doplňte řešení.




# Úloha 2 (25 %)
# Napište funkci, která dostane string a rozhodne o něm, zda se jedná o
# bezpečné heslo.

# Heslo je bezpečné, pokud:
# - má délku alespoň 8
# - obsahuje znak "!" nebo "?"
# - není přesně "password"

# Funkce vrátí "OK", když je heslo bezpečné, jinak "SLABÉ".

# Sem doplňte řešení.




# Úloha 3 (50 %)
# Máte dány proměnné
# - tank_volume: kapacita nádrže
# - goal: počet km do cíle
# - refuel_km: počet km, po kterých můžete znovu natankovat (tedy pokaždé po tolika ujetých kilometrech od posledního tankování)
# - refuel_volume: objem paliva, který můžete natankovat
# a funkci
# - get_consumption(): ta vrátí náhodné číslo představující spotřebu za poslední JEDEN KILOMETR

# Napište program, který spočítá, zda dojedete do cíle. Pokud ano, vytiskněte
# "CÍL", jinak vypište počet najetých kilometrů před vyprázdněním nádrže.
# Počítejte s tím, že na začátku máte plnou nádrž.

# HINT: Použijte while cyklus a postupně zvyšujte km. Po každém kilometru
# odečtěte od objemu nádrže výsledek funkce get_consumption. Pozor!
# Nezapomeňte, že můžete natankovat maximálně do objemu nádrže, takže nelze
# prostě přičíst refuel_volume.

def get_consumption():
    return 8.8 * random() / 100 + 0.075


seed() # Nevšímejte si, inicializuje generátor náhodných čísel
tank_volume = 60
goal = 2000
refuel_km = 500
refuel_volume = 28

# Sem doplňte řešení.
