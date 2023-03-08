def divna_morseovka(zprava):
    pocet_tecek = 0
    pocet_carek = 0

    for znak in zprava:
        if znak == ".":
            pocet_tecek = pocet_tecek + 1
        elif znak == "-":
            pocet_carek = pocet_carek + 1
        else:
            return False

    return pocet_tecek == pocet_carek
