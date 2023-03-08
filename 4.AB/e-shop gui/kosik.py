class Kosik:
    """ Trida reprezentujici kosik s nakupem. """

    def __init__(self, seznam_produktu):
        """ Konstruktor tridy Kosik. """
        self.kosik = {
            produkt[0]: {
                "id": produkt[0],
                "nazev": produkt[1],
                "cena": produkt[2],
                "popis": produkt[3],
                "pocet": 0
            }
            for produkt in seznam_produktu
        }

    def nacti_ze_seznamu(self, seznam_polozek):
        """ Metoda pro nacteni kosiku ze seznamu polozek. """

        for polozka in seznam_polozek:
            self.kosik[polozka[2]]["pocet"] = polozka[3]

    def pridej_do_kosiku(self, produkt, pocet_kusu):
        """ Metoda pro pridani produktu do kosiku. """

        if pocet_kusu <= 0:
            return ValueError("Počet kusů musí být kladné číslo.")

        if pocet_kusu > produkt[4]:
            return ValueError("Není dostatek produktů na skladě.")

        if produkt[0] in self.kosik:
            self.kosik[produkt[0]]["pocet"] += pocet_kusu
        else:
            self.kosik[produkt[0]]["pocet"] = pocet_kusu

        return None

    def odeber_z_kosiku(self, id_produktu):
        """ Metoda pro odebrani produktu z kosiku. """

        if id_produktu not in self.kosik:
            return ValueError("Produkt není v košíku.")

        self.kosik[id_produktu]["pocet"] = 0

        return None

    def vyprazdni_kosik(self):
        """ Metoda pro vyprazdneni kosiku. """

        for polozka in self.kosik.values():
            polozka["pocet"] = 0

    @property
    def soucet(self):
        """ Metoda pro vypocet souctu kosiku. """

        return sum(
            int(polozka["cena"]) * polozka["pocet"]
            for polozka in self.kosik.values()
        )
