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
#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // X axis
    line((-4, 0), (4, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    for x in (-3, -2, -1, 1, 2, 3) {
      line((x, -3pt), (x, 3pt), stroke: 1pt)
      content((x, 0), anchor: "south", padding: .3, [$#x$])
    }

    // Y axis
    line((0, -3), (0, 3), mark: (start: ">", end: ">"), stroke: 1pt)
    for y in (-2, -1, 1, 2) {
      line((-3pt, y), (3pt, y), stroke: 1pt)
      content((0, y), anchor: "west", padding: .3, [$#y$])
    }

    content((0, 0), anchor: "south-west", padding: .2, [$0$])

    line(
      (0, 0),
      (-3, -1),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "north",
      padding: .2,
      [#clr[$-1 dot vc(u)$]],
    )
  })
]

Sčítání vektorů lze charakterisovat slovy "nejdřív jedním směrem, pak druhým".
Tedy, součet vektorů je vektor, který končí v bodě, kam se dostaneme, když
nejprve sledujeme jeden z vektorů a pak druhý (na pořadí pochopitelně nezáleží,
výsledek je stejný). Na obrázku můžete vidět vektor $#clg[$vc(w)$] =
#clr[$vc(u)$] + #clb[$vc(v)$] = #clb[$vc(v)$] + #clr[$vc(u)$]$, kde
$#clr[$vc(u)$] = vec(3, 1)$ a $#clb[$vc(v)$] = vec(1, 2)$.

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // X axis
    line((-1, 0), (5, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    for x in (1, 2, 3, 4) {
      line((x, -3pt), (x, 3pt), stroke: 1pt)
      content((x, 0), anchor: "north", padding: .3, [$#x$])
    }

    // Y axis
    line((0, -1), (0, 4), mark: (start: ">", end: ">"), stroke: 1pt)
    for y in (1, 2, 3) {
      line((-3pt, y), (3pt, y), stroke: 1pt)
      content((0, y), anchor: "east", padding: .3, [$#y$])
    }

    content((0, 0), anchor: "north-east", padding: .2, [$0$])

    line(
      (0, 0),
      (3, 1),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "north-west",
      padding: .1,
      [#clr[$vc(u)$]],
    )

    line(
      (3, 1),
      (4, 3),
      stroke: blue + 2pt,
      mark: (end: ">", fill: blue),
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "north-west",
      padding: .1,
      [#clb[$vc(v)$]],
    )

    line(
      (0, 0),
      (1, 2),
      stroke: blue + 2pt,
      mark: (end: ">", fill: blue),
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "south-east",
      padding: .1,
      [#clb[$vc(v)$]],
    )

    line(
      (1, 2),
      (4, 3),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "south-east",
      padding: .1,
      [#clr[$vc(u)$]],
    )

    line(
      (0, 0),
      (4, 3),
      stroke: green + 2pt,
      mark: (end: ">", fill: green),
      name: "w",
    )
    content(
      ("w.start", 50%, "w.end"),
      anchor: "south-east",
      padding: .1,
      [#clg[$vc(w)$]],
    )
  })
]

Nyní si již můžeme představit, jak vypadá množina řešení lineárního systému.
Začněme příkladem ve 2D. Řešením systému o dvou rovnicích a dvou neznámých je
většinou pouze bod, takže tento případ přeskočíme. Uvažme místo toho systém o
rovnici _jedné_.

#math.equation(numbering: none, block: true)[
  $2x_1 - x_2 = 3$
]

Jistě tušíte, že "grafem" takové rovnice je přímka. Tento fakt si teď umíme
odvodit přes vektory a znalost tvaru řešení takové rovnice.

Označíme $x_2$ jako volnou proměnnou $t_1$ a spočítáme $x_1 = (3 + t_1) slash
2$. Když toto řešení přepíšeme do tvaru z @thm:tvar-reseni[věty], dostaneme
#math.equation(numbering: none, block: true)[
  $vec(x_1, x_2) = #clb[$vec(3 slash 2, 0)$] + t_1 dot #clr[$vec(
    1 slash 2,
    1
  )$]$.
]

Odtud vidíme, že řešením rovnice budou všechny vektory, které umíme získat jako
součet vektoru #clb[$vec(3 slash 2, 0)$] s libovolným násobkem vektoru
#clr[$vec(1 slash 2, 1)$]. Protože všechny násobky vektoru #clr[$vec(
  1 slash 2,
  1
)$] tvoří přímku s přesně tímto směrem, je množinou řešení rovnice vlastně
přímka se směrem #clr[$vec(1 slash 2, 1)$] posunutá od počátku o vektor
#clb[$vec(3 slash 2, 0)$] jako na obrázku níže.

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // X axis
    line(
      (-5, 0),
      (5, 0),
      stroke: (thickness: 1pt, dash: "dashed"),
    )
    for x in (-4, -3, -2, -1, 1, 2, 3, 4) {
      line((x, -3pt), (x, 3pt), stroke: 1pt)
      content((x, 0), anchor: "north", padding: .3, [$#x$])
    }

    // Y axis
    line(
      (0, -4),
      (0, 4),
      stroke: (thickness: 1pt, dash: "dashed"),
    )
    for y in (-3, -2, -1, 1, 2, 3) {
      line((-3pt, y), (3pt, y), stroke: 1pt)
      content((0, y), anchor: "east", padding: .3, [$#y$])
    }

    content((0, 0), anchor: "north-east", padding: .2, [$0$])

    line(
      (0, 0),
      (3 / 2, 0),
      stroke: blue + 2pt,
      mark: (end: ">", fill: blue),
      name: "u",
    )
    line((0, -3), (3, 3))
    line(
      (3 / 2, 0),
      (2, 1),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "v",
    )
  })
]

Do více dimensí se tento pohled na množiny řešení přenáší snadno. Totiž, mají-li
vektory $vc(p), vc(v)_1, ..., vc(v)_k$ třeba $n$ reálných složek, pak je množina
#math.equation(numbering: none, block: true)[
  ${vc(p) + t_1 dot vc(v)_1 + ... + t_k dot vc(v)_k}$
]
rovná $k$-dimensionální plocha -- tedy vlastně prostor s $k$ "směry pohybu"
určenými vektory $vc(v)_1,...,vc(v)_k$ -- posunutá o vektor $vc(p)$ od počátku.

Pochopitelně, pro dimensi větší dvěma se takový prostor nekreslí lehko.
Nakreslíme si pročež ještě množinu ${#clb[$vc(p)$] + t_1 dot #clr[$vc(v)_1$] +
  t_2 dot #clg[$vc(v)_2$]}$ uvnitř $RR^3$, která popisuje řešení obecného systému
o třech neznámých a jedné rovnici. Je jím právě dvoudimensionální rovina určená
vektory #clr[$vc(v)_1$] a #clg[$vc(v)_2$] posunutá o vektor #clb[$vc(p)$].

#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // Axes
    line((-4, 0), (4, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    line((0, -4), (0, 4), mark: (start: ">", end: ">"), stroke: 1pt)
    line((-4, -3), (4, 3), mark: (start: ">", end: ">"), stroke: 1pt)

    line(
      (0, 0),
      (2, 1),
      stroke: blue + 2pt,
      mark: (end: ">", fill: blue),
      name: "p",
    )
    content(
      ("p.start", 50%, "p.end"),
      anchor: "north-west",
      padding: .1,
      [#clb[$vc(p)$]],
    )

    line(
      (2, 1),
      (0, 3),
      stroke: red + 2pt,
      mark: (end: ">", fill: red),
      name: "v1",
    )
    content(
      ("v1.start", 50%, "v1.end"),
      anchor: "north-east",
      padding: .1,
      [#clr[$vc(v_1)$]],
    )

    line(
      (2, 1),
      (4, 1),
      stroke: green + 2pt,
      mark: (end: ">", fill: green),
      name: "v2",
    )
    content(
      ("v2.start", 50%, "v2.end"),
      anchor: "north-east",
      padding: .1,
      [#clg[$vc(v_2)$]],
    )

    line(
      (-2, 1),
      (7, 1),
      (3, 4),
      (-6, 4),
      close: true,
      fill: black.transparentize(90%),
      stroke: none,
    )
  })
]

Předchozí odstavec nám pomůže nahlížet geometricky nejen na množiny řešení
lineárních systémů, ale i na systémy samotné. Totiž, množina řešení *jedné*
lineární rovnice o $n$ neznámých je -- jak jsme právě viděli --
$(n-1)$-dimensionální rovina v $RR^n$, protože má $n - 1$ volných proměnných.
Takže, počítáme-li systém o $m$ rovnicích v $n$ proměnných, hledáme vlastně
průnik právě $m$ #box[$(n-1)$-dimensionálních] rovin. V obecném případě (roviny
nejsou rovnoběžné ani stejné) je průnik dvou $(n-1)$-dimensionálních rovin
rovina dimense $n - 2$. Jako příklady uvažte bod (dimense $0$) jako průnik dvou
přímek (dimense $1$) nebo přímku jako průnik dvou rovin (dimense $2$).

Nejčastěji (když se žádné roviny neshodují a nejsou rovnoběžné) bude řešením
lineárního systému o $n$ proměnných a $m$ rovnicích rovina dimense $n - m$. Z
toho též plyne, že má-li takový systém více rovnic než proměnných, nebude mít
řešení (jinak by totiž dimense výsledného objektu byla záporná).

Ukažme si právě diskutovaný pohled na příkladu lineárního systému
#math.equation(numbering: none, block: true)[
  $
    #grid(
      columns: (auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, start),
      clr[$x_1$], clr[$+$], clr[$2x_2$], clr[$=$], clr[$3$],
      clb[$-x_1$], clb[$-$], clb[$x_2$], clb[$=$], clb[$-2$],
    )
  $
]
Z toho, co víme, je množinou řešení každé z rovnic přímka v rovině (2D
prostoru). Pokud se nejedná o stejné ani rovnoběžné přímky, pak bude jejich
průnikem rovina dimense $0$, tj. *bod*. Ten představuje geometrickou paralelu
jednoprvkové množiny řešení systému bez volných proměnných (v množině řešení je
pouze onen vektor $vc(p)$ a žádné vektory volných proměnných). Tento systém je
vyobrazen níže.
#align(center)[
  #cetz.canvas({
    import cetz.draw: *
    import cetz.decorations: *

    // Axes
    line((-4, 0), (4, 0), mark: (start: ">", end: ">"), stroke: 1pt)
    line((0, -4), (0, 4), mark: (start: ">", end: ">"), stroke: 1pt)

    line((1, -3pt), (1, 3pt), stroke: 1pt)
    content((1, 0), anchor: "north", padding: .3, [$1$])

    line((-3pt, 1), (3pt, 1), stroke: 1pt)
    content((0, 1), anchor: "east", padding: .3, [$1$])

    line(
      (-3, 3),
      (5, -1),
      stroke: red + 2pt,
      name: "p",
    )

    line(
      (-3, 5),
      (5, -3),
      stroke: blue + 2pt,
      mark: (end: ">", fill: red),
      name: "q",
    )

    circle(
      (1, 1),
      radius: .15,
      fill: black,
    )
    line((1, 0), (1, 1), stroke: (dash: "dashed"))
    line((0, 1), (1, 1), stroke: (dash: "dashed"))
  })
]
