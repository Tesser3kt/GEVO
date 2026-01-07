#import "../template.typ": *

== Geometrický pohled na řešení lineárních systémů

Nyní se podíváme na to, jak si lze v prostoru $RR^n$ visualisovat množiny řešení
lineárních systémů a vlastně i systémy samotné. V celé sekci budeme prvky $RR^n$
vnímat buď jako body, nebo jako vektory, podle toho, který pohled se více hodí.
Jak jsme uvedli v úvodu do kapitoly, formálně se jedná o tytéž objekty.

Podle @thm:tvar-reseni[věty] má lineární systém množinu řešení tvaru
#math.equation(numbering: none, block: true)[
  ${vc(p) + t_1 dot vc(v)_1 + t_2 dot vc(v)_2 + ... + t_k dot vc(v)_k}$,
]
kde $t_1,...,t_k$ jsou volné proměnné. Abychom si mohli tuto množinu
"nakreslit", musíme nejprve pochopit, jak lze geometricky vyjádřit násobení
vektorů čísly a sčítání vektorů.

Posuňme se pročež do dvou dimensí (v jedné dimensi jsou vektory totéž, co čísla)
a uvažme vektor $#clr[$vc(u)$] = vec(3, 1)$. To je vektor se začátkem v bodě
$(0, 0)$ a koncem v bodě $(3, 1)$. Nakreslíme si jej jako šipku na obrázku níže.

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // X axis
    line((-4, 0), (4, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    for x in (1, 2, 3) {
      line((x, -3pt), (x, 3pt), stroke: 1pt)
      content((x, 0), anchor: "north", padding: .3, [$#x$])
    }

    // Y axis
    line((0, -3), (0, 3), mark: (start: ">", end: ">"), stroke: 1pt)
    for y in (1, 2) {
      line((-3pt, y), (3pt, y), stroke: 1pt)
      content((0, y), anchor: "east", padding: .3, [$#y$])
    }

    content((0, 0), anchor: "north-east", padding: .2, [$0$])

    line(
      (0, 0),
      (3, 1),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "south",
      padding: .2,
      [#clr[$vc(u)$]],
    )
  })
]

Násobení vektoru #clr[$vc(u)$] *kladným* číslem se projevuje jeho *prodloužením*
nebo *zkrácením*. Velmi přirozeně, vektor $0.5 dot #clr[$vc(u)$]$ je přesně o
polovinu kratší než #clr[$vc(u)$] a vektor $3 dot #clr[$vc(u)$]$ je přesně
třikrát delší, jak vidno níže.

#grid(
  columns: (1fr, 1fr),
  rows: 1fr,
  align: center,
  [
    #cetz.canvas({
      import cetz.draw: *
      import cetz.decorations: *

      // X axis
      line((-1, 0), (4, 0), mark: (start: ">", end: ">"), stroke: 1pt)
      for x in (1, 2, 3) {
        line((x, -3pt), (x, 3pt), stroke: 1pt)
        content((x, 0), anchor: "north", padding: .3, [$#x$])
      }

      // Y axis
      line((0, -1), (0, 3), mark: (start: ">", end: ">"), stroke: 1pt)
      for y in (1, 2) {
        line((-3pt, y), (3pt, y), stroke: 1pt)
        content((0, y), anchor: "east", padding: .3, [$#y$])
      }

      content((0, 0), anchor: "north-east", padding: .2, [$0$])

      line(
        (0, 0),
        (1.5, 0.5),
        stroke: red + 2pt,
        mark: (end: ">", fill: red),
        name: "v",
      )
      content(
        ("v.start", 50%, "v.end"),
        anchor: "south",
        padding: .3,
        [#clr[$0.5 dot vc(u)$]],
      )
    })],
  [
    #cetz.canvas({
      import cetz.draw: *
      import cetz.decorations: *

      // X axis
      line((-1, 0), (6, 0), mark: (start: ">", end: ">"), stroke: 1pt)
      for x in (1, 2, 3, 4, 5, 6, 7, 8, 9) {
        line((x / 2, -3pt), (x / 2, 3pt), stroke: 1pt)
        content((x / 2, 0), anchor: "north", padding: .3, [$#x$])
      }

      // Y axis
      line((0, -1), (0, 3), mark: (start: ">", end: ">"), stroke: 1pt)
      for y in (1, 2, 3, 4) {
        line((-3pt, y / 2), (3pt, y / 2), stroke: 1pt)
        content((0, y / 2), anchor: "east", padding: .3, [$#y$])
      }

      content((0, 0), anchor: "north-east", padding: .2, [$0$])

      line(
        (0, 0),
        (4.5, 1.5),
        stroke: red + 2pt,
        mark: (end: ">", fill: red),
        name: "v",
      )
      content(
        ("v.start", 50%, "v.end"),
        anchor: "south",
        padding: .2,
        [#clr[$3 dot vc(u)$]],
      )
    })
  ],
)

Násobení *záporným* číslem se navíc projevuje otočením směru.
