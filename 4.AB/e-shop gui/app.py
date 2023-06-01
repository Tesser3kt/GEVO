import hashlib
import os
import PySimpleGUI as sg
from spravce_databaze import SpravceDatabaze
from rozhrani import Rozhrani
from kosik import Kosik
from nastaveni import MOTIV, VYCHOZI_FONT, VYCHOZI_VELIKOST, POZICE_OKNA

# cesta k databazi
cesta_k_databazi = os.path.join(os.path.dirname(__file__), 'data.db')

# vytvoreni instance tridy SpravceDatabaze
spravce_databaze = SpravceDatabaze(cesta_k_databazi)

# pripojeni databaze a ziskani chyby
chyba_pripojeni = spravce_databaze.pripoj_databazi()

if chyba_pripojeni:
    sg.popup_ok("Chyba při připojení k databázi: ", chyba_pripojeni,
                relative_location=POZICE_OKNA)

# inicializace databaze
chyba_inicializace = spravce_databaze.inicializuj_databazi()
if chyba_inicializace:
    sg.popup_ok("Chyba při inicializaci databáze: ", chyba_inicializace,
                relative_location=POZICE_OKNA)

# vytvoreni instance tridy Rozhrani
rozhrani = Rozhrani(MOTIV, VYCHOZI_FONT, VYCHOZI_VELIKOST)

# nacti produkty z databaze
seznam_produktu = spravce_databaze.vsechny_produkty()

# vytvor kosik
kosik = Kosik(seznam_produktu)

# zobraz login
okno = rozhrani.zobraz_login()


def prijatelne_jmeno(jmeno):
    """ Jmeno musi mit aspon tri znaky a obsahovat jen pismena a cislice."""

    # Sem piste kod


def najdi_uzivatele(jmeno):
    """Najde uzivatele v tabulce uzivatelu a vrati jeho id, jmeno a heslo jako
    slovnik."""

    # nacti vsechny uzivatele
    vsichni_uzivatele = spravce_databaze.vsichni_uzivatele()

    # Projdete vsechny uzivatele a najdete uzivatele s danym jmenem.
    # Jeho udaje vratte jako slovnik s klici 'id', 'jmeno' a 'heslo'.

    for uzivatel in vsichni_uzivatele:
        if uzivatel[1] == jmeno:
            return {
                'id': uzivatel[0],
                'jmeno': uzivatel[1],
                'heslo': uzivatel[2]
            }
    return None

def prijatelne_heslo(heslo):
    """Heslo musi mit aspon sest znaku, aspon jedno velke pismeno, jedno male
    pismeno a jednu cislici. """

    # Sem piste kod


def zakoduj_heslo(heslo):
    """Zakoduje heslo pomoci hashovaci funkce sha256."""
    return hashlib.sha256(heslo.encode()).hexdigest()


def uloz_uzivatele(jmeno, heslo):
    """Ulozi noveho uzivatele do databaze."""
    spravce_databaze.uloz_uzivatele(jmeno, heslo)


def zobraz_upozorneni(zprava):
    """Zobrazi okno s upozornenim."""
    sg.popup_ok(zprava, relative_location=POZICE_OKNA)


while True:
    udalost, hodnoty = okno.read()

    if udalost == sg.WIN_CLOSED:
        # zavreni okna ukonci program
        break

    if udalost == 'Přihlásit se':
        # kliknuti na tlacitko prihlasit se
        jmeno = hodnoty[0]
        heslo = hodnoty[1]

        #######################################################################
        ############### SEM VYPLNUJTE LOGIKU PRIHLASOVANI #####################
        #######################################################################

        prihlaseny_uzivatel = najdi_uzivatele(jmeno)
        if prihlaseny_uzivatel == None:
            zobraz_upozorneni("Uzivatel nenalezen.")
            continue

        #######################################################################
        ################### TADY KONCI LOGIKA PRIHLASOVANI ####################
        #######################################################################

        # prihlaseni probehlo uspesne
        okno.close()
        # nacti kosik z databaze
        seznam_polozek = spravce_databaze.nacti_kosik_z_databaze(
            prihlaseny_uzivatel['id']
        )
        kosik.nacti_ze_seznamu(seznam_polozek)
        okno = rozhrani.zobraz_hlavni_menu(prihlaseny_uzivatel['jmeno'])

    if udalost == 'Zaregistrovat se':
        # kliknuti na tlacitko zaregistrovat se
        zadane_jmeno = hodnoty[0]
        zadane_heslo = hodnoty[1]

        #######################################################################
        ############### SEM VYPLNUJTE LOGIKU REGISTRACE #######################
        #######################################################################



        #######################################################################
        ################### TADY KONCI LOGIKA REGISTRACE ######################
        #######################################################################

        sg.popup_ok("Registrace proběhla úspěšně.",
                    relative_location=POZICE_OKNA)

    if udalost == 'Odhlásit se':
        # kliknuti na tlacitko odhlasit se
        chyba = spravce_databaze.uloz_produkty_do_databaze(seznam_produktu)
        if chyba:
            sg.popup_ok("Chyba při ukládání produktů: ", chyba,
                        relative_location=POZICE_OKNA)
        chyba = spravce_databaze.uloz_kosik_do_databaze(
            prihlaseny_uzivatel['id'], kosik.kosik)
        if chyba:
            sg.popup_ok("Chyba při ukládání košíku: ", chyba,
                        relative_location=POZICE_OKNA)

        kosik.vyprazdni_kosik()
        okno.close()
        okno = rozhrani.zobraz_login()

    if udalost == 'Produkty':
        if not seznam_produktu:
            sg.popup_ok("Žádné produkty nebyly nalezeny.",
                        relative_location=POZICE_OKNA)
            continue
        okno.close()
        okno = rozhrani.zobraz_produkty(
            prihlaseny_uzivatel['jmeno'], seznam_produktu
        )

    if udalost == 'Košík':
        # kliknuti na tlacitko kosik
        okno.close()
        okno = rozhrani.zobraz_kosik(prihlaseny_uzivatel['jmeno'],
                                     kosik.kosik, kosik.soucet)

    for i, produkt in enumerate(seznam_produktu):
        if udalost == f"Koupit {produkt[0]}":
            mnozstvi = hodnoty[f"Mnozstvi {produkt[0]}"]
            if not mnozstvi.isdigit():
                sg.popup_ok("Množství musí být celé číslo.",
                            relative_location=POZICE_OKNA)
                continue

            mnozstvi = int(mnozstvi)
            chyba = kosik.pridej_do_kosiku(produkt, mnozstvi)
            if chyba:
                sg.popup_ok("Nelze přidat zboží: ", chyba,
                            relative_location=POZICE_OKNA)
            else:
                sg.popup_ok(
                    (f"{mnozstvi} kusů zboží {produkt[1]} "
                     "bylo přidáno do košíku."),
                    relative_location=POZICE_OKNA
                )

                produkt = list(produkt)
                produkt[4] -= mnozstvi
                seznam_produktu[i] = tuple(produkt)

                okno[f"Na sklade {produkt[0]}"].update(
                    f"Na skladě: {produkt[4]} ks"
                )

    for polozka in kosik.kosik.values():
        if udalost == f"Odebrat {polozka['id']}":
            mnozstvi = polozka['pocet']
            chyba = kosik.odeber_z_kosiku(polozka['id'])
            if chyba:
                sg.popup_ok("Nelze odebrat zboží: ", chyba,
                            relative_location=POZICE_OKNA)
            else:
                sg.popup_ok(
                    (f"{mnozstvi} kusů zboží {polozka['nazev']} "
                     "bylo odebráno z košíku."),
                    relative_location=POZICE_OKNA
                )
                okno[f"Polozka {polozka['id']}"].update(visible=False)
                okno["Soucet"].update(f"Celková cena: {kosik.soucet} Kč")

                for i, produkt in enumerate(seznam_produktu):
                    if produkt[0] == polozka['id']:
                        produkt = list(produkt)
                        produkt[4] += mnozstvi
                        seznam_produktu[i] = tuple(produkt)

# zavri okno a databazi po skonceni programu
spravce_databaze.zavri_databazi()
okno.close()
