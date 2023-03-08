import PySimpleGUI as sg
import textwrap
from nastaveni import VRCHNI_LISTA, POZICE_OKNA


class Rozhrani:
    """ Trida grafickeho rozhrani. """

    def __init__(self, motiv, vychozi_font, vychozi_velikost):
        # nastaveni vychoziho fontu
        sg.set_options(font=(vychozi_font, vychozi_velikost))

        # nacteni motivu
        sg.theme_add_new('Nord', motiv)
        sg.theme('Nord')
        self.vychozi_font = vychozi_font
        self.vychozi_velikost = vychozi_velikost

    def __rozlozeni_produktu(self, produkt):
        """ Metoda pro vyrobu rozlozeni produktu. """

        popis = '\n'.join(textwrap.wrap(produkt[3], 40))
        rozlozeni_produktu = [
            [sg.Text(produkt[1], font=(self.vychozi_font, 16))],
            [sg.Text(f"Cena: {int(produkt[2])} Kč")],
            [sg.Text(f"Popis: {popis}")],
            [sg.Text(f"Na skladě: {produkt[4]} ks",
                     key=f"Na sklade {produkt[0]}")],
            [
                sg.Text("Množství: "),
                sg.Input('1', size=(3, 1), key=f"Mnozstvi {produkt[0]}"),
                sg.Button('Koupit', font=(self.vychozi_font, 12),
                          key=f"Koupit {produkt[0]}")
            ]
        ]

        return rozlozeni_produktu

    def __rozlozeni_polozky(self, polozka):
        """ Metoda pro vyrobu rozlozeni polozky kosiku. """

        rozlozeni_polozky = [[
            sg.Text(polozka["nazev"], font=(self.vychozi_font, 16)),
            sg.Text(f"Cena: {int(polozka['cena'])} Kč"),
            sg.Text(f"Množství: {polozka['pocet']} ks"),
            sg.Text(
                f"Celková cena: {int(polozka['cena']) * polozka['pocet']} Kč"),
            sg.Button('Odebrat', size=(10, 1), key=f"Odebrat {polozka['id']}")
        ]]

        return rozlozeni_polozky

    def zobraz_login(self):
        """ Metoda pro vyrobu rozlozeni login okna. """

        sloupce = [
            [
                [sg.Text("Uživatelské jméno: ")],
                [sg.Text("Heslo: ")]
            ],
            [
                [sg.InputText()],
                [sg.InputText(password_char='*')],
                [sg.Button('Přihlásit se'), sg.Button('Zaregistrovat se')]
            ]
        ]

        rozlozeni_login = [
            [sg.Column(sloupce[0], vertical_alignment='t'),
             sg.Column(sloupce[1], vertical_alignment='t')],
        ]

        okno = sg.Window('GEVO E-Shop',
                         rozlozeni_login, finalize=True,
                         relative_location=POZICE_OKNA)
        okno['Přihlásit se'].set_cursor('hand2')
        okno['Zaregistrovat se'].set_cursor('hand2')

        return okno

    def zobraz_hlavni_menu(self, uzivatel):
        """ Metoda pro vyrobu rozlozeni hlavniho menu. """

        vrchni_lista = [
            [sg.Text('GEVO E-Shop', font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.HorizontalSeparator(
                 color=VRCHNI_LISTA["POZADI"], pad=(150, 0)),
             sg.Text(uzivatel, font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.Button('Odhlásit se')]
        ]

        tlacitka = [
            [sg.Button('Produkty', size=(20, 2)),
             sg.Button('Košík', size=(20, 2))],
        ]

        rozlozeni = [
            [sg.Column(vrchni_lista, pad=(0, 0),
                       background_color=VRCHNI_LISTA["POZADI"])],
            [sg.Column(tlacitka, pad=(50, 50))]
        ]

        okno = sg.Window('GEVO E-Shop', rozlozeni, finalize=True,
                         relative_location=POZICE_OKNA, margins=(0, 0),
                         element_justification='c')
        okno['Odhlásit se'].set_cursor('hand2')
        okno['Produkty'].set_cursor('hand2')
        okno['Košík'].set_cursor('hand2')

        return okno

    def zobraz_produkty(self, uzivatel, seznam_produktu):
        """ Metoda pro vyrobu rozlozeni okna s produkty. """
        vrchni_lista = [
            [sg.Text('GEVO E-Shop', font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.HorizontalSeparator(
                color=VRCHNI_LISTA["POZADI"], pad=(500, 0)),
             sg.Text(uzivatel, font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.Button("Košík"),
             sg.Button('Odhlásit se')]
        ]

        produkty = []
        for i, produkt in enumerate(seznam_produktu):
            if i % 3 == 0:
                produkty.append([])

            produkty[-1].append(
                sg.Frame('', self.__rozlozeni_produktu(produkt),
                         border_width=1, size=(400, 250), pad=(10, 10))
            )

        rozlozeni = [
            [sg.Column(vrchni_lista, pad=(0, 0),
                       background_color=VRCHNI_LISTA["POZADI"])],
            [sg.Column(produkty, pad=(50, 50))]
        ]

        okno = sg.Window('GEVO E-Shop', rozlozeni, finalize=True,
                         relative_location=POZICE_OKNA, margins=(0, 0),
                         element_justification='c')

        okno['Odhlásit se'].set_cursor('hand2')
        okno['Košík'].set_cursor('hand2')
        for produkt in seznam_produktu:
            okno[f"Koupit {produkt[0]}"].set_cursor('hand2')

        return okno

    def zobraz_kosik(self, uzivatel, kosik, soucet):
        """ Zobrazi seznam polozek kosiku. """

        vrchni_lista = [
            [sg.Text('GEVO E-Shop', font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.HorizontalSeparator(
                color=VRCHNI_LISTA["POZADI"], pad=(300, 0)),
             sg.Text(uzivatel, font=(self.vychozi_font, 20),
                     background_color=VRCHNI_LISTA["POZADI"]),
             sg.Button("Produkty"),
             sg.Button('Odhlásit se')]
        ]

        polozky_k_zobrazeni = [
            polozka for polozka in kosik.values() if polozka["pocet"] > 0
        ]
        polozky = [
            [sg.Frame('', self.__rozlozeni_polozky(polozka),
                      border_width=1, size=(600, 50), pad=(10, 10),
                      key=f"Polozka {polozka['id']}")]
            for polozka in polozky_k_zobrazeni
        ] if polozky_k_zobrazeni else [
            [sg.Text("Košík je prázdný.", font=(self.vychozi_font, 20))]
        ]

        rozlozeni = [
            [sg.Column(vrchni_lista, pad=(0, 0),
                       background_color=VRCHNI_LISTA["POZADI"])],
            [sg.Column(polozky, pad=(50, 50))],
            [sg.Column(
                [[sg.Text(f"Celková cena: {soucet} Kč", key="Soucet",
                          font=(self.vychozi_font, 20))]])]
        ]

        okno = sg.Window('GEVO E-Shop', rozlozeni, finalize=True,
                         relative_location=POZICE_OKNA, margins=(0, 0),
                         element_justification='c')

        okno['Odhlásit se'].set_cursor('hand2')
        okno['Produkty'].set_cursor('hand2')
        for polozka in polozky_k_zobrazeni:
            okno[f"Odebrat {polozka['id']}"].set_cursor('hand2')

        return okno
