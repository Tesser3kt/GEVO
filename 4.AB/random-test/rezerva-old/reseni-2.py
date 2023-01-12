# tady si proste musim napsat proceduru, co dostane dve slova
# ta podminka uvnitr kontroluje, ze posledni pismeno prvniho slova je stejne
# jako prvni pismeno druheho slova

def slep_stringy(slovo1, slovo2):
    if slovo1[-1] == slovo2[0]:
        return slovo1 + slovo2
    else:
        return "Nelze"
