def spravne_jmeno(slabiky):
    if "u" not in slabiky[0]:
        return False

    if len(slabiky) == 2:
        if slabiky[-1][-2] + slabiky[-1][-1] == "ík":
            return True

    if len(slabiky) == 3:
        if slabiky[-1] != "ka":
            return False
        if slabiky[1][-2] + slabiky[1][-1] != "in":
            return False
        return True

    return False
