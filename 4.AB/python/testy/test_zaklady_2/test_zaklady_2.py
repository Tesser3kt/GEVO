from random import random, seed


# Úloha 1 (25 %)
# V seznamu words máte jednotlivá slova. Spojte je ve větu a uložte ji do
# proměnné. Nezapomeňte přidat na její konec tečku.
# Například ze seznamu ["Krajty", "jsou", "boží"] má vzniknout věta "Krajty jsou boží."

words = ["Tahle", "úloha", "je", "příliš", "lehká"]

# Sem pište řešení.


# Úloha 2 (25 %)

# Napište funkci final_price, která dostane dva parametry -- původní cenu a slevu (v procentech) --
# a vypočte výslednou cenu. Tedy, třeba, final_price(200, 70) = 140 
 
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


seed()  # Nevšímejte si, inicializuje generátor náhodných čísel
tank_volume = 60
goal = 2000
refuel_km = 500
refuel_volume = 28

# Sem doplňte řešení.
