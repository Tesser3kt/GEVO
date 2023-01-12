# procedura, co dostane seznam trojic dims a trojici box
def vejdou_se_predmety(dims, box):
    # pro kazdy predmet, jehoz rozmery jsou v dims, zkontroluju, ze se vejde
    for rozmery in dims:
        # zkontroluju, ze kazdy rozmer (sirka, vyska, hloubky) je mensi nez
        # odpovidajici rozmer krabice
        if rozmery[0] > box[0] or rozmery[1] > box[1] or rozmery[2] > box[2]:
            # kdyz je nejaky rozmer moc velky vratim False
            return False
    # kdyz projdu vsechny predmety a nenarazil jsem na zadny vetsi, tak se
    # vsechny vejdou, takze vratim True
    return True
