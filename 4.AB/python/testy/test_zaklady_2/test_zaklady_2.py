# Úloha 1 (25 %)
# V seznamu words máte jednotlivá slova. Spojte je ve větu a uložte ji do
# proměnné. Nezapomeňte přidat na její konec tečku.
# Například ze seznamu ["Krajty", "jsou", "boží"] má vzniknout věta "Krajty jsou boží."

words = ["Tahle", "úloha", "je", "příliš", "lehká"]

# Sem pište řešení.



# Úloha 2 (25 %)

# Napište funkci final_price, která dostane dva parametry -- původní cenu a slevu (v procentech) --
# a vypočte výslednou cenu. Tedy, třeba, final_price(200, 30) = 140 
 
# Sem doplňte řešení.



# Úloha 3 (50 %)
# Hackeři se snaží prolomit systém jeden po jednom v daném pořadí.
# Každý hacker má "skill level" (celé číslo).
# Systém má "security level" (celé číslo).
# Po každém neúspěšném pokusu o prolomení se zvýší security level o danou hodnotu "increase".

# Máte dány proměnné
# - seznam "hackers" se skill levely jednotlivých hackerů,
# - číslo security level,
# - číslo increase (o kolik se má zvýšit security level po každém neúspěšném pokusu o prolomení)

# Pravidla:
# - Hackeři se snaží prolomit systém jeden po druhém.
# - Když je skill hackera *ostře větší* než security level, dojde k prolomení.
# - Když je skill hackera *menší nebo roven* security levelu, k prolomení nedojde a zvýší se security level o increase.

# Vytiskněte počet úspěšných prolomení systému hackery.

hackers = [7, 6, 8, 9]
security_level = 6
increase = 2

# Sem doplňte řešení.
