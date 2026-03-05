from random import random, seed


# Úloha 1 (25 %)
# Ve slovníku 'users' máte seznam uživatelů spolu s jejich "zahashovanými"
# hesly. Ověřte, zda jsou v proměnných 'login' a 'password' správné
# přihlašovací údaje, tj. jestli jménu 'login' odpovídá 'hash(password)'.
# Pokud ano, vytiskněte "LOGIN SUCCESSFUL", jinak "ERROR".
def hash(password):
    return password[len(password) // 2 :] + password[: len(password) // 2][::-1]


users = {
    "xXxYourM0mxXx": "56784321",
    "DeathKnight": "yhardsrtzegg",
    "PythonKing": "rajty223KujuLiM",
}
login = "PythonKing"
password = "MilujuKrajty223"

# Sem pište řešení.


# Úloha 2 (25 %)

# Podle seznamu slov 'words' vytvořte seznam s jejich délkami na příslušných místech,
# tedy například k seznamu ["kocka", "pes"] vyrobte seznam [5, 3].
# Připomínám, že délku stringu získáte přes funkci len().

words = ["slunce", "mesic", "planeta"]
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
