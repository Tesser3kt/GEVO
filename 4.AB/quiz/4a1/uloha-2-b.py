def spravne_jmeno(seznam_slabik):
    for slabika in seznam_slabik:
        if "u" not in slabika and "ík" not in slabika:
            return False
    return True
