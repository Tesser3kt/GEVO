ceny = [499, 599, 499, 479]
doprava = [79, 0, 99, 139]


def secti(dvojice):
    return dvojice[0] + dvojice[1]


print(min(map(secti, zip(ceny, doprava))))
