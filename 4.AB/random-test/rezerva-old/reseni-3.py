# tady mi staci prochazet seznam obycejnym for cyklem a u kazdeho cisla se
# podivat jaky dava zbytek po deleni deseti -- to je jeho posledni cislice
# kdyz je ten zbytek 3, cislo vytisknu

seznam = [15, 23, 7, 3, 50, 81, 99, 73]

for cislo in seznam:
    if cislo % 10 == 3:
        print(cislo)
