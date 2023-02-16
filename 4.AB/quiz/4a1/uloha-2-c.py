def spravne_jmeno(slabiky):
    if "u" not in slabiky[0]:
        return False

    if len(slabiky) == 2:
        if slabiky[-1][-1] == "k" and slabiky[-1][-2] == "í":
            return True

    if len(slabiky) == 3:
        if slabiky[-1] == "ka" and (slabiky[1][-2] + slabiky[1][-1] == "in"):
            return True

    return False
