# tohle je slovnik, kde pod predcislimi jsou ulozena jmena zemi
slovnik_predcisli = {
    "420": "Ceska republika",
    "421": "Slovensko",
    "034": "Spanelsko"
}

# v te samotne procedure mi staci vytahnout z tel. cislo predcisli - to jsou
# cisla na pozici 1 az 3 (na pozici 0 je +)
# pak se jen podivam do slovniku, jakou zemi mam pod timhle predcislim a
# vytisknu ji na konci vety "Hovor ze zeme "


def urci_zemi(tel_cislo):
    predcisli = tel_cislo[1] + tel_cislo[2] + tel_cislo[3]
    print("Hovor ze zeme " + slovnik_predcisli[predcisli])
