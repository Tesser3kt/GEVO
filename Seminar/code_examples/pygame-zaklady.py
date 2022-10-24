""" PyGame funguje tak, ze na casti platna (coz je okno nejake velikosti)
kresli casti povrchu (coz jsou proste pole ruzne barevnych pixelu).

Zajima nas realne jen par trid a metod:
    - Surface
    - Rect
    - Sprite
    - Group

Surface je ta trida povrchu. Uchovava realne jen 2D seznam pixelu ruznych barev.

Rect je trida obdelniku. Obdelnik je v PyGamu urceny parametry 'left', 'top',
'width' a 'height'. ('left', 'top') je levy horni roh a ('width', 'height')
jsou rozmery.

Sprite je trida hernich objektu. Kazdy Sprite ma parametry 'image' a 'rect'.
Dost neprekvapive je 'image' povrch (Surface) a 'rect' obdelnik (Rect). Tyhle
dva parametry staci k tomu, abychom urcili, jak herni objekt vypada, jak je
velky a kde je.

Group je seznam Spritu. Usnadnuje veci jako "mazani" a "vykreslovani" hernich
objektu (Sprite) na platno.

Samotny zpusob, jak "hybete" objekty (Sprite) je pak takovy, ze v kazdem snimku
nakreslite na misto herniho objektu pozadi (coz je nejaky predpripraveny
povrch) a pak na jeho novou pozici (rect) nakreslite jeho texturu (image).
PyGamu pak reknete, ze ma updatovat jen ty casti platna, ktere jste prekreslili.
Treba tenhle posledni krok za vas Group dela automaticky. Slouzi k tomu metody
Group.clear(pozadi, platno), ktera dostane jako parametry pozadi a platno a
prekresli pozadi pres vsechny objekty v Group. Na vykreslovani je pak
Group.draw(platno), ktera vykresli textury vsech objektu v Group.

Idealne mate objekty rozmistene tak, ze vsechny hybajici se objekty mate
v jedne Group a kazdy snimek je prekreslujete. Nepohyblive objekty pak mate
v jine Group a prekreslujete jen tehdy, kdyz je treba (podle pravidel hry --
muze se stat, ze nejake neprekreslite nikdy, treba steny).
"""

# ukazka tech veci nahore
import pygame as pg
from random import randint

# par konstant
WIDTH = 800     # sirka okna / platna
HEIGHT = 800    # vyska okna / platna


# POZOR! Trida Sprite z modulu sprite je ABSTRAKTNI, to znamena, ze si musim
# vytvorit vlastni podtridu, pokud chci treba automatizovat kresleni hernich
# objektu.
class GameObject(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, rect: pg.Rect):
        # v Pythonu (a v podstate vsude jinde) musi podtrida volat
        # inicializator (konstruktor) nadtridy
        pg.sprite.Sprite.__init__(self)
        # textura objektu se MUSI jmenovat 'image', aby PyGame mohl kreslit
        # automaticky
        self.image = image
        # podobne, obdelnik pozice a velikosti se musi jmenovat 'rect'
        self.rect = rect

    # Tohle NEMUSI byt soucasi GameObject. PyGame tuhle metodu nijak nevyuziva.
    # Hodi se ale pro pohodlme hybani s objekty.
    def move(self, x, y) -> None:
        # Rect ma metodu move(x, y), ktera proste vrati obdelnik stejne
        # velikosti, posunuty o vektor (x, y).
        self.rect = self.rect.move(x, y)


# musim volat vzdycky, inicializuje PyGame
pg.init()

# takhle vytvorim platno / okno na kresleni. Metode 'set_mode' z modulu
# 'display' predam dvojici (sirka, vyska) a pak zpusob kresleni. Skoro vzdycky
# se vyplati bud pg.SCALED (textury se zvetsuji/zmensuji podle absolutni
# velikosti okna na danem monitoru) nebo pg.FULLSCREEN (to je asi jasny).
# screen je taky Surface jako kazdy jiny.
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)

# vytvorim prazdny povrch (pixely zatim nemaji zadnou barvu) velikost stejne
# jako ma screen. Metoda get_size() vraci dvojici (sirka, vyska) daneho povrchu.
background = pg.Surface(screen.get_size())

# vybarvim background cerne (0, 0, 0)
background.fill((0, 0, 0))

# metoda convert() vraci Surface, ktery je ale ulozeny mnohem efektivneji.
# V tomhle pripade byl background proste 2D seznam 800 * 800 pixelu, kazdy
# z nich barvy (0, 0, 0). Po konvertovani si PyGame jen pamatuje barvu --
# -- (0, 0, 0) -- a pocet po sobe jdoucich pixelu -- 800 * 800. To znamena, ze
# misto 800 * 800 trojic cisel od 0 do 255 (coz zabira asi 640 kilobytu) si
# pamatuju jednu trojici -- (0, 0, 0) -- a cislo 800 * 800 (coz zabira asi
# 7 bytu). To je uzitecne jak pro efektivitu vykreslovani, tak pro uvolneni
# pameti. TL;DR = VZDYCKY KONVERTUJTE.
background = background.convert()

# vytvorim si par hybajicich ctverecku (treba nahodnych rozmeru a barvy)

# vytvorim si Group pro ty ctverecky. Ta trida, co me zajima je RenderUpdates
# (to je podtrida Group) z modulu sprite. ZADNOU JINOU SE NEVYPLATI POUZIVAT.
# Je to nejuplnejsi trida pro uchovavani Spritu v tom smyslu, ze je umi
# automaticky prekreslit, znovu vykreslit a navic si pamatovat, ktere casti
# platna se zmenily.
squares = pg.sprite.RenderUpdates()

for _ in range(4):
    # vytvorim si 'image' pro ctverecek. Proste si vytvorim povrch nahodne
    # velikosti na nahodne pozici (jenom bude stejna vyska jako sirka) a
    # vyplnim ho nahodnou barvou
    side_length = randint(40, 100)
    x = randint(0, WIDTH)   # x-ova pozice, pocita se zleva doprava
    y = randint(0, HEIGHT)  # y-ova pozice, pocita se seshora dolu
    color = tuple(randint(0, 255) for _ in range(3))

    image = pg.Surface((side_length, side_length))
    image.fill(color)
    # VZDYCKY KONVERTUJTE!
    image = image.convert()

    # obdelnik objektu. Trida Rect potrebuje informace (x/left, y/top, width,
    # height)
    rect = pg.Rect(x, y, side_length, side_length)

    square = GameObject(image, rect)
    squares.add(square)

# vytvorim si steny kolem herniho okna, aby nemohly ctverecky vylezt ven
walls = pg.sprite.RenderUpdates()

# uz to trochu zestrucnim (ujistete se, ze tenhle zapis CHAPETE)
# textura zdi je irelevantni, protoze neni videt, PyGame ale stejne musi mit
# v promenne 'image' nejaky povrch (v tomhle pripade velikosti (0, 0))
for i in range(2):
    rects = [
            pg.Rect(-10 + i * (WIDTH + 20), -10, 10, HEIGHT + 20),
            pg.Rect(-10, -10 + i * (HEIGHT + 20), WIDTH + 20, 10)
    ]

    walls.add(*[GameObject(
            pg.Surface((0, 0)),  # faaaaaajn, prazdnej povrch nemusite konvertovat
            pg.Rect(rect)
        )
        for rect in rects
    ])

# udelam si takovou jednoduchou simulaci. Necham ctverecky se nahodne hybat a
# zrat vetsi ctverecky, kdyz do sebe narazi.

