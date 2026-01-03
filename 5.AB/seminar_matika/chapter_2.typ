#import "template.typ": *

= Lineární geometrie

V této relativně krátké kapitole prozkoumáme geometrické vlastnosti vektorů a
lineárních systémů. Ukážeme si, jak se jednoduché lineární systémy dají
vizualizovat a dáme geometrický význam pojmům jako pivoty, volné proměnné apod.

Celou dobu budeme pracovat nad množinou reálných čísel, kterou značíme $RR$.
Důvod je jednoduchý: reálná čísla jsou tou nejjednodušší číselnou množinou,
která umí modelovat souvislý prostor a tím pádem jsou nejvhodnější právě
ke geometrické představě.

Začneme tím, co vlastně myslíme slovem _prostor_. V matematice si pod prostorem
můžeme představovat množinu _bodů_ s daným počet směrů pohybu, kterým říkáme
_dimense_ prostoru. Například, my obýváme třídimensionální prostor, protože v
každém bodě se můžeme hýbat nezávisle nahoru/dolu, doleva/doprava a
dopředu/dozadu.

Prostor s pouze jediným směrem pohybu je _přímka_. Tu matematicky modelujeme
zkrátka jako množinu reálných čísel $RR$. Totiž, stačí si na přímce vybrat dva
význačné body: bod $0$ a bod $1$. Jakoukoli jinou vzdálenost na přímce pak
můžeme vyjádřit zkrátka jako násobek vzdálenosti mezi body $0$ a $1$. Hýbeme-li
se od bodu $0$ doleva, bude tato vzdálenost záporná, a hýbeme-li se doprava,
bude kladná.

#figure(
  cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    line((-5, 0), (5, 0), mark: (start: ">", end: ">"))
    for x in (0, 1, 3.14) {
      let color = rgb(0, 0, 0)
      if x == 3.14 {
        color = red
      }

      line((x, -3pt), (x, 3pt), stroke: color + 1pt)
      content(
        (x, 0),
        anchor: "north",
        padding: .3,
        [#text(color)[$#x$]],
      )
    }

    brace(
      (0, .2),
      (3.14, .2),
      stroke: red,
      amplitude: .3,
      pointiness: 1,
      outer-inset: .3,
      inner-outset: .5,
    )
    content(
      (3.14 / 2, .8),
      [$#text(red)[3.14] dot 1$],
    )
  }),
  caption: [Přímka jako množina reálných čísel.],
)

S vyšším počtem dimensí zkrátka zvyšujeme počet přímek, na kterých měříme
vzdálenosti. Dvoudimensionální prostor získáme jako dvojici přímek, které
obvykle kreslíme vzájemně kolmé (ale není to nutné) -- jedna přímka pro pohyb
doleva a doprava, druhá pro pohyb nahoru a dolu. Každé místo, kam se těmito
dvěma směry pohybu umím dostat vyjádřím dvojicí čísel, tzv. souřadnicemi, která
udává vzdálenost ušlou po těchto dvou přímkách zvlášť. Když jednu přímku
modelujeme jako $RR$, snad není překvapivé, že dvojici přímek budeme modelovat
jako součin #box[$RR times RR$], tedy jako množinu všech dvojic reálných čísel.
Zápis $RR times RR$ obvykle zkracujeme na $RR^2$.

#figure(
  cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // X axis
    line((-3, 0), (3, 0), mark: (start: ">", end: ">"), stroke: blue + 1pt)
    for x in (1, 2) {
      line((x, -3pt), (x, 3pt), stroke: blue + 1pt)
      content(
        (x, 0),
        anchor: "north",
        padding: .3,
        [#text(blue)[$#x$]],
      )
    }

    // Y axis
    line((0, -3), (0, 3), mark: (start: ">", end: ">"), stroke: red + 1pt)
    for y in (1, 2) {
      line((-3pt, y), (3pt, y), stroke: red + 1pt)
      content(
        (0, y),
        anchor: "east",
        padding: .3,
        [#text(red)[$#y$]],
      )
    }

    content(
      (0, 0),
      anchor: "north-east",
      padding: .2,
      [$0$],
    )

    line((2, 1), (2, 0), stroke: (paint: blue, dash: "dashed"))
    line((2, 1), (0, 1), stroke: (paint: red, dash: "dashed"))
    circle((2, 1), radius: .1, fill: black)
    content(
      (2, 1),
      anchor: "south-west",
      padding: .2,
      [$(#clb[2], #clr[1])$],
    )
  }),
  caption: [Dvoudimensionální prostor (rovina) jako množina $RR^2$.],
)

Obecně, prostor s $n$ různými směry (kde $n$ je jakékoliv přirozené číslo)
budeme representovat jako množinu $RR^n$, čili jako $n$-tice reálných čísel.

Přestože intuitivně vnímáme vektory jako šipky mezi body, formálně není mezi
vektorem z~počátku do nějakého bodu a tímto bodem vlastně žádný rozdíl. Obojí
jsou jen $n$-tice čísel.
