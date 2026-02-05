#import "../template.typ": *

== Norma vektoru

Pokračujeme s geometrickou interpretací vektorů jako šipek v prostoru. První
možnost, jak určit vektor, je specifikovat jeho začátek (my zásadně používáme
počátek soustavy souřadnic) a konec. Takto jsme ztotožnili body s vektory, tedy
vlastně vektory s jejich konci. Ovšem, další přirozenou alternativou, jak
definovat "šipku", je udat její *velikost* a *směr*. Směr vektoru je ošemetná
záležitost (lze definovat jen _relativně_ vůči ostatním vektorům). Velikost (či
formálně _norma_) vektoru je však popsatelná výrazně snadněji.

Začneme pozorováním: velikost šipky z bodu $(0, 0)$ do bodu $(v_1, v_2)$ je
přesně délka uhlopříčky obdélníku se stranami $|v_1|$ a $|v_2|$ (musíme psát
absolutní hodnoty, bo souřadnice $v_1$ a $v_2$ mohou být záporné). Vizte
obrázek.

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // Axes
    line((-4, 0), (1, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    line((0, -1), (0, 5), mark: (start: ">", end: ">"), stroke: 1pt)

    line(
      (0, 0),
      (-3, 4),
      stroke: black + 2pt,
      mark: (end: ">", fill: black),
      name: "p",
    )
    content(
      ("p.start", 70%, "p.end"),
      anchor: "west",
      padding: .2,
      [$vc(v) = vec(v_1, v_2)$],
    )

    line((0, 0), (-3, 0), stroke: blue + 2pt)
    line((0, 4), (-3, 4), stroke: blue + 2pt)
    flat-brace((-0.1, -0.1), (-2.9, -0.1), stroke: blue)
    content((-1.5, -.6), [#clb[$|v_1|$]])

    line((-3, 0), (-3, 4), stroke: red + 2pt)
    line((0, 0), (0, 4), stroke: red + 2pt)
    flat-brace((-3.1, 0.1), (-3.1, 3.9), stroke: red)
    content((-3.8, 2), [#clr[$|v_2|$]])
  })
]
Tu spočteme snadno přes Pythagorovu větu. Podle ní je délka odvěsny pravoúhlého
trojúhelníku s odvěsnami $|v_1|$ a $|v_2|$ rovna $sqrt(|v_1|^2 + |v_2|^2)$.
Pochopitelně, při sudé mocnině vždy vychází kladné číslo, můžeme tedy absolutní
hodnoty zanedbat a psát zkrátka $sqrt(v_1^2 + v_2^2)$. Normu vektoru $vc(v) =
vec(v_1, v_2)$ označíme jako $||vc(v)||$. Právě jsme ukázali, že ve 2D platí
rovnost $||vc(v)|| = sqrt(v_1^2 + v_2^2)$.

Ve více dimensích můžeme normu spočítat podobně. Totiž, obecně v $RR^n$ je
velikost šipky s~počátkem v bodě $(0,0,...,0)$ a koncem v bodě
$(v_1,v_2,...,v_n)$ rovna délce tělesové uhlopříčky $n$-dimensionálního kvádru
se stranami $|v_1|, |v_2|, ..., |v_n|$. To je samozřejmě obtížné si představit.
Podívejme se ještě na případ dimensí tří. Spočítáme délku tělesové uhlopříčky
kvádru se stranami délek $|v_1|, |v_2|$ a $|v_3|$.

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    line((-3, 0), (-1.5, 1.5), stroke: (thickness: .5pt, dash: "dashed"))
    line((-1.5, 1.5), (-1.5, 5.5), stroke: (thickness: .5pt, dash: "dashed"))
    line((-1.5, 1.5), (1.5, 1.5), stroke: (thickness: .5pt, dash: "dashed"))

    line((0, 0), (-3, 0), stroke: blue + 2pt)
    line((0, 4), (-3, 4), stroke: blue + 2pt)
    flat-brace((-0.1, -0.1), (-2.9, -0.1), stroke: blue)
    content((-1.5, -.6), [#clb[$|v_1|$]])

    line((-3, 0), (-3, 4), stroke: red + 2pt)
    line((0, 0), (0, 4), stroke: red + 2pt)
    flat-brace((-3.1, 0.1), (-3.1, 3.9), stroke: red)
    content((-3.8, 2), [#clr[$|v_3|$]])

    line((0, 0), (1.5, 1.5), stroke: purple + 2pt)
    line((0, 4), (1.5, 5.5), stroke: purple + 2pt)
    flat-brace((0.2, 0), (1.5, 1.3), stroke: purple, flip: true)
    content((1.5, 0.3), [#clp[$|v_2|$]])

    line((1.5, 1.5), (1.5, 5.5), stroke: red + 2pt)
    line((-3, 4), (-1.5, 5.5), stroke: purple + 2pt)
    line((1.5, 5.5), (-1.5, 5.5), stroke: blue + 2pt)

    line(
      (-3, 0),
      (1.5, 5.5),
      stroke: black + 2pt,
      mark: (end: ">", fill: black),
      name: "p",
    )
    content(
      ("p.start", 50%, "p.end"),
      anchor: "north-west",
      padding: .05,
      [$vc(v) = vec(v_1, v_2, v_3)$],
    )

    line(
      (-3, 0),
      (1.5, 1.5),
      stroke: black + 2pt,
      mark: (end: ">", fill: black),
      name: "x",
    )
    content(
      ("x.start", 50%, "x.end"),
      anchor: "north-west",
      padding: .1,
      [$vc(x)$],
    )
  })
]
Budeme muset použít Pythagorovu větu dvakrát: nejprve na obdélník (podstavu) s
uhlopříčkou $vc(x)$ a stranami $|v_1|$ a $|v_2|$ a potom na obdélník s
uhlopříčkou $vc(v)$ a stranami $vc(x)$ a $|v_3|$.

První výpočet dá $||vc(x)|| = sqrt(v_1^2 + v_2^2)$. Potom
#math.equation(numbering: none, block: true)[
  $||vc(v)|| = sqrt(||vc(x)||^2 + v_3^2) = sqrt(
    (sqrt(v_1^2 + v_2^2))^2 +
    v_3^2
  ) = sqrt(v_1^2 + v_2^2 + v_3^2)$.
]
Snad trochu překvapivě vyšla norma vektoru $||vc(v)||$ opět jako druhá odmocnina
součtu druhých mocnin jeho souřadnic. Aniž budeme tento fakt dokazovat, můžeme
stejný výpočet provést i s tělesovou uhlopříčkou $n$-dimensionálního kvádru
(akorát musíme Pythagorovu větu použít #box[$(n-1)$-krát]). Právě provedenou
úvahu shrneme v definici normy vektoru.

#box[
  #definition("Norma vektoru")[
    Ať $vc(v) = vec(v_1, dots.v, v_n) in RR^n$. Definujeme *normu* vektoru $vc(v)$
    jako číslo
    #math.equation(numbering: none, block: true)[
      $||vc(v)|| = sqrt(v_1^2 + v_2^2 + ... + v_n^2)$.
    ]
  ]
]
