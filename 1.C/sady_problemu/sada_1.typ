#import "@preview/sheetstorm:0.5.1": *

#set text(lang: "cs", size: 12pt)
#set list(indent: 12pt, spacing: 12pt)

#let sheetstorm-task = task
#let task(points: none, ..args) = {
  let point-count = if type(points) == int {
    points
  } else if type(points) == array and points.all(point => type(point) == int) {
    points.sum()
  }

  let points-prefix = if point-count == 1 {
    "bod"
  } else if point-count >= 2 and point-count <= 4 {
    "body"
  } else {
    "bodů"
  }

  sheetstorm-task(
    task-prefix: "Úloha",
    points: points,
    points-prefix: points-prefix,
    ..args,
  )
}

#show: assignment.with(
  title: "Výroková logika",
  course: "1.C Matematika",
  authors: "Adam Klepáč",
  date: datetime.today(),
  date-format: "[day]. [month padding:none]. [year]",
  score-box-enabled: true,
)

#task(points: 1, name: "Logická rozehřívačka (rozlogovačka?)")[
  Budete hledat negace výroků. *Pozor!* Myslete na to, že negace výroku je vždy
  lživá ve chvíli, kdy je ten výrok pravdivý a naopak. Tedy, například: "Neprší
  nebo nesněží," *není* negací věty: "Prší nebo sněží," protože když se stane,
  že prší, ale nesněží, tak jsou obě věty pravdivé. Přemýšlejte a najděte negace
  vět:
  - Nemám rád matiku a logika mě nebaví.
  - Když mě tu nutí sedět, tak se budu aspoň snažit.
]
#task(points: 1, name: "Tabulky, tabulky, tabulky...")[
  Rozhodněte, kdy je výrok
  #math.equation(numbering: none, block: true)[
    $p <=> (q or not r)$
  ]
  pravdivý a kdy lživý v závislosti na pravdivosti výroků $p$, $q$ a $r$.
]

#task(points: 2, name: "Mám krátký nos")[
  Najděte nějaký výraz, ve kterém se objeví aspoň tři různé výroky $p$, $q$ a
  $r$ a aspoň jednou každá z~logických operací $not, and, or, =>, <=>$, který je
  zároveň tzv. *tautologií*. To znamená, že je *vždy pravdivý*, ať už jsou $p, q,
  r$ pravdivé nebo lživé.

  Příklad tautologie pro dva výroky je třeba $(p and not p) => q$, protože $p
  and not p$ je vždy lež, a tedy je taková implikace vždycky pravda.
]

#task(points: 2, name: "Nebo s čárkou")[
  Zavedeme si novou logickou operaci $plus.o$, která se chová následovně: $p
  plus.o q$ je
  - lež, když $p$ je pravda i $q$ je pravda;
  - pravda, když $p$ je pravda a $q$ je lež;
  - pravda, když $p$ je lež a $q$ je pravda;
  - lež, když $p$ je lež i $q$ je lež.

  Této operaci se někdy říká "výlučné nebo" (exclusive or), protože je pravdivá
  jen tehdy, když přesně jeden z výroků (ale ne oba) je pravda.

  S použitím výroků $p, q$ a operací $not, and, or$ najděte výrok, který je
  ekvivalentní výroku $p plus.o q$. Pokud byste směli použít i $=>$ a $<=>$,
  dokázali byste najít jednodušší vyjádření?
]

#pagebreak()
#task(points: 3, name: "Alarm")[
  Bezpečnostní systém naší budovy má tři sensory: $d$, $o$ a $p$
  (#strong[d]veřní, #strong[o]kenní a #strong[p]ohybový). Alarm je
  naprogramovaný tak, aby se spustil za následujících situací ($0$ znamená, že
  sensor nezachytil aktivitu, $1$, že ano).
  #align(center)[
    #table(
      inset: 8pt,
      fill: (_, y) => {
        if calc.odd(y) { luma(240) } else { white }
      },
      align: center,
      stroke: (x, y) => {
        if y == 0 { (bottom: .5pt) }
        if x == 2 { (right: .5pt) }
      },
      columns: 4,
      [$d$], [$o$], [$p$], [alarm],
      [0], [0], [0], [0],
      [1], [0], [0], [0],
      [0], [1], [0], [1],
      [0], [0], [1], [1],
      [1], [1], [0], [1],
      [1], [0], [1], [1],
      [0], [1], [1], [0],
    )
  ]
  Bohužel, poslední řádek tabulky pro $d = 1$, $o = 1$ a $p = 1$ se ztratil.
  Školník Zdenda si ale pamatuje, že *aktivace nebo deaktivace přesně jednoho
  jakéhokoliv sensoru nemůže spustit alarm*. Dokážete doplnit poslední řádek? Je
  vůbec možné, že si školník Zdenda pamatuje chování alarmu správně?
]

#task(points: 3, name: "Obálky")[
  Na stole leží tři obálky s nadpisy:
  #align(center + horizon)[
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 1cm,
      [#rect(inset: 12pt, width: 4.5cm, height: 2cm)[Tato obálka obsahuje výhru.]],
      [#rect(inset: 12pt, width: 4.5cm, height: 2cm)[První obálka neobsahuje výhru.]],
      [#rect(inset: 12pt, width: 4.5cm, height: 2cm)[Tato obálka neobsahuje výhru.]],
    )
  ]
  *Přesně jedna z těchto obálek obsahuje výhru*. Ve které obálce výhra je, když
  víme, že *přesně jeden z nadpisů je pravdivý*?

  Co když ale změníme podmínku na
  - přesně dva nadpisy jsou pravdivé?
  - lichý počet nadpisů je pravdivý?
  - nadpis na obálce obsahující výhru je lživý?

  Ve které z těchto situací je pravda, že *je výhra stále v přesně jedné obálce?*
]

#pagebreak()
#task(points: 5, name: "Škodolibý vězeň")[
  Vyslýcháte zajatce a potřebujete z něj dostat pravdivost čtyř prohlášení: $a,
  b, c$ a $d$. Zajatec se ale poradil se svým právníkem a tvrdí, že ze zákona ho
  smíte vyslýchat jen za této podmínky:
  #rect(stroke: (left: 1pt), inset: (left: 12pt))[
    O každém výroku $p$ složeném z proměnných $a$, $b$, $c$ a $d$ vám řekne
    pouze *minimální počet proměnných, které musejí změnit pravdivostní
    hodnotu*, aby celý výrok $p$ také změnil pravdivostní hodnotu.
  ]
  Například, vězeň vám může říct, že ve výroku $(a and b) or (not c and d)$
  musíte změnit pravdivostní hodnotu přesně dvou proměnných, aby měl i celý
  výrok opačnou hodnotu.

  Zkuste najít _co nejkratší_ posloupnost výroků, pomocí níž se jednoznačně
  dozvíte pravdivost $a, b, c, d$.
]
