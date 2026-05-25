#import "../template.typ": *

== Soustavy souřadnic (aspoň trochu) prakticky

=== Krystaly

Krystaly jsou látky, jejichž atomová struktura je extrémně pravidelná,
uspořádaná do čtverců, obdélníků nebo mnohoúhelníků a jejich
vícedimensionálních variant. Vezměme například sůl, tj. chlorid sodný. Atomy
chloru a sodíku jsou zde uspořádány v krychlích, jejichž vrcholy a středy stěn
okupuje chlorid a středy hran sodík.

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Cube
    line((0, 0), (2, 0))
    line((0, 0), (0, 2))
    line((0, 0), (0.8, 0.8), stroke: (dash: "dashed"))
    line((2, 0), (2.8, 0.8))
    line((0, 2), (0.8, 2.8))
    line((0, 2), (2, 2))
    line((2, 0), (2, 2))
    line((2, 2), (2.8, 2.8))
    line((2.8, 0.8), (2.8, 2.8))
    line((0.8, 2.8), (2.8, 2.8))
    line((0.8, 0.8), (0.8, 2.8), stroke: (dash: "dashed"))
    line((0.8, 0.8), (2.8, 0.8), stroke: (dash: "dashed"))

    // Chloride
    circle(
      (0.8, 0.8),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.8, 1.8),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (0.4, 1.4),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.4, 0.4),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    for x in (0, 2) {
      for y in (0, 2) {
        circle((x, y), radius: 6pt, fill: blue)
        if (x, y) != (0, 0) {
          circle((x + 0.8, y + 0.8), radius: 6pt, fill: blue)
        }
      }
    }

    circle((1, 1), radius: 6pt, fill: blue)
    circle((1.4, 2.4), radius: 6pt, fill: blue)
    circle((2.4, 1.4), radius: 6pt, fill: blue)

    // Sodium
    circle(
      (0.4, 0.4),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (0.8, 1.8),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.8, 0.8),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle((0, 1), radius: 3pt, fill: yellow)
    circle((1, 0), radius: 3pt, fill: yellow)
    circle((1, 2), radius: 3pt, fill: yellow)
    circle((2, 1), radius: 3pt, fill: yellow)
    circle((0.4, 2.4), radius: 3pt, fill: yellow)
    circle((1.8, 2.8), radius: 3pt, fill: yellow)
    circle((2.4, 2.4), radius: 3pt, fill: yellow)
    circle((2.4, 2.4), radius: 3pt, fill: yellow)
    circle((2.4, 0.4), radius: 3pt, fill: yellow)
    circle((2.4, 0.4), radius: 3pt, fill: yellow)
    circle((2.8, 1.8), radius: 3pt, fill: yellow)
  }),
  caption: [Atomová struktura soli.],
)

Při práci s takovouto strukturou bychom rádi uměli vyjádřit pozice jednotlivých
atomů nějakým jednoduchým způsobem. Pro přehlednost se soustřeďme jenom na
přední stěnu krystalické struktury.

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Grid
    for x in (0, 2, 4, 6) {
      line((x, 0), (x, 4))
    }
    for y in (0, 2, 4) {
      line((0, y), (6, y))
    }

    for x in (0, 2, 4, 6) {
      for y in (0, 2, 4) {
        // Chloride
        circle((x, y), radius: 6pt, fill: blue)
        if (x <= 4 and y <= 2) {
          circle((x + 1, y + 1), radius: 6pt, fill: blue)
        }
        // Sodium
        if (x <= 4) {
          circle((x + 1, y), radius: 3pt, fill: yellow)
        }
        if (y <= 2) {
          circle((x, y + 1), radius: 3pt, fill: yellow)
        }
      }
    }
  }),
  caption: [Přední stěna atomové struktury soli.],
)

Délka jedné hrany sítě je 3.34 Ångstromů (jednotek značících $10^(-10)$ metrů).
Není výpočetně praktické, abychom při representaci takovéto mříže v počítači
museli neustále počítat s násobky desetinných čísel. Přirozenou "soustavou
souřadnic" je v tomto případě zřejmě dvojice kolmých os, kde jednotková
vzdálenost na obou osách odpovídá přesně délce hrany krychle. Označíme-li levý
dolní atom chloru jako počátek této soustavy, pak atom v prostředním řádku a
třetím sloupci má v této soustavě souřadnice $(2, 1)$ místo neohrabaných 6.68
Ångstromů doprava a 3.34 Ångstromů nahoru. Jak si brzy vysvětlíme, volbu
soustavy souřadnic v prostoru můžeme provést výběrem vhodných vektorů, které
určují právě směr i jednotkovou vzdálenost všech os. V tomto případě by
rozumnou volbou byla dvojice vektorů
#math.equation(numbering: none, block: true)[
  $(vec(3.34, 0), vec(0, 3.34))$.
]

Krychlová struktura soli nám při volbě soustavy souřadnic byla velmi nápomocná.
Mohli jsme vyjít z běžné kartézské soustavy souřadnic a akorát vynásobit
jednotkovou vzdálenost obou os vhodnou konstantou (číslem $3.34$). Příroda není
vždy tak shovívavá.

Uvažme krystal zvaný _tuha_, tvořený atomy uhlíku uspořádanými do
šestiúhelníkové mříže. Jeho jedna atomová vrstva (též zvaná _grafen_) je
znázorněna na @fig:grafen[obrázku].

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Lattice
    let sq3 = 1.73
    for x in (0, 3, 6) {
      for y in (0, sq3) {
        line((x, y), (x + 1, y))
        line((x, y), (x - 0.5, y + sq3 / 2))
        line((x + 1, y), (x + 1.5, y + sq3 / 2))
        line((x - 0.5, y + sq3 / 2), (x, y + sq3))
        line((x, y + sq3), (x + 1, y + sq3))
        line((x + 1, y + sq3), (x + 1.5, y + sq3 / 2))

        let x = x + 1.5
        let y = y + sq3 / 2
        line((x, y), (x + 1, y))
        line((x, y), (x - 0.5, y + sq3 / 2))
        line((x + 1, y), (x + 1.5, y + sq3 / 2))
        line((x - 0.5, y + sq3 / 2), (x, y + sq3))
        line((x, y + sq3), (x + 1, y + sq3))
        line((x + 1, y + sq3), (x + 1.5, y + sq3 / 2))
      }
    }

    // Carbon
    let carbon(x, y) = circle((x, y), radius: 4pt, fill: green)
    for x in (0, 3, 6) {
      for y in (0, sq3) {
        carbon(x, y)
        carbon(x + 1, y)
        carbon(x - 0.5, y + sq3 / 2)
        carbon(x, y + sq3)
        carbon(x + 1, y + sq3)
        carbon(x + 1.5, y + sq3 / 2)

        let x = x + 1.5
        let y = y + sq3 / 2
        carbon(x, y)
        carbon(x + 1, y)
        carbon(x - 0.5, y + sq3 / 2)
        carbon(x, y + sq3)
        carbon(x + 1, y + sq3)
        carbon(x + 1.5, y + sq3 / 2)
      }
    }
  }),
  caption: [Atomová struktura grafenu.],
) <fig:grafen>

Možná vás napadá, že hrany hexagonu opět určují ty pravé ořechové vektory pro
soustavu souřadnic. Je tomu tak. Totiž, pravidelný hexagon má sice hrany ve
třech různých směrech, ale je záhodno si všimnout, že do hrany vedoucí "doleva
nahoru" se dostaneme přes hranu vedoucí doprava a hranu vedoucí "doprava
nahoru". Vizte @fig:baze-grafen[obrázek].

#figure(
  cetz.canvas({
    import cetz.draw: *

    polygon((0, 0), 6, radius: 2)

    let sq3 = 1.73

    // First vec
    line(
      (-1, -sq3),
      (1, -sq3),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "south",
      padding: .2,
      clb[$vc(u)$],
    )

    // Second vec
    line(
      (1, -sq3),
      (2, 0),
      mark: (end: ">", fill: red),
      stroke: red + 2pt,
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "south-east",
      padding: .1,
      clr[$vc(v)$],
    )

    line(
      (2, 0),
      (-2, 0),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "-2u",
    )
    content(
      ("-2u.start", 50%, "-2u.end"),
      anchor: "south",
      padding: .2,
      clb[$-2 dot.c vc(u)$],
    )

    line(
      (-1, -sq3),
      (-2, 0),
      mark: (end: ">", fill: purple),
      stroke: purple + 2pt,
      name: "w",
    )
    content(
      ("w.start", 50%, "w.end"),
      anchor: "north-east",
      padding: .1,
      $#clb[$-vc(u)$] + #clr[$vc(v)$]$,
    )
  }),
  caption: [Soustava souřadnic pro strukturu grafenu.],
) <fig:baze-grafen>

Délka jedné hrany je 1.42 Ångstromů, položme tedy
#math.equation(numbering: none, block: true)[
  $#clb[$vc(u)$] = vec(1.42, 0)$
]
a spočítejme, čemu se musí rovnat #clr[$vc(v)$]. Protože vnitřní úhel
pravidelného hexagonu má velikost $120 degree$, vektor #clr[$vc(v)$] svírá s
vektorem #clb[$vc(u)$] úhel $180 degree - 120 degree = 60 degree$. Zároveň,
velikost vektoru #clr[$vc(v)$] musí být rovna velikosti vektoru #clb[$vc(v)$],
tj. číslu $1.42$.

Podle @def:uhel-mezi-vektory[definice] musí platit
#math.equation(numbering: none, block: true)[
  $cos 60 degree = (#clb[$vc(u)$] dot.c #clr[$vc(v)$]) / (||#clb[$vc(u)$]||
  ||#clr[$vc(v)$]||) = (1.42 #clr[$v_1$]) / 1.42^2 = #clr[$v_1$] / 1.42$,
]
z čehož
#math.equation(numbering: none, block: true)[
  $#clr[$v_1$] = 1.42 dot.c cos 60 degree = 0.71$.
]
Z podmínky velikosti vektoru #clr[$vc(v)$] dopočteme jeho druhou složku, #clr[$v_2$]. Musí platit
#math.equation(numbering: none, block: true)[
  $1.42 = ||#clr[$vc(v)$]|| = sqrt(#clr[$v_1^2$] + #clr[$v_2^2$])$,
]
takže
#math.equation(numbering: none, block: true)[
  $#clr[$v_2$] = sqrt(1.42^2 - #clr[$v_1^2$]) = sqrt(1.42^2 - 0.71^2) = 1.23$.
]
Tím jsme hotovi. Zvolíme-li za soustavu souřadnic dvojici vektorů
#math.equation(numbering: none, block: true)[
  $(vec(1.42, 0), vec(0.71, 1.23))$,
]
pak pozici každého atomu uhlíku ve struktuře grafenu umíme vyjádřit
celočíselnými souřadnicemi. Například, atom uhlíku v pravém horním rohu
@fig:grafen[obrázku] má v naší soustavě souřadnic polohu $(6, 5)$ (je-li levým
dolním rohem bod $(0, 0)$) namísto odporného čísla, které jsem líný
dopočítávat.
