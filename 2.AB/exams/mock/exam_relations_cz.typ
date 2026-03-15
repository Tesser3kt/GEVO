// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Set page and fonts
#let page-counter(cur, last) = {
  strfmt("Strana {} z {}", cur, last)
}
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Mock test
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #datetime.today().display("[month repr:long] [day], [year]")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  },
)
#show heading.where(
  level: 1,
): it => block(width: 100%)[
  #set text(14pt)
  #it.body
]
#show math.equation: set text(
  font: "TeX Gyre Schola Math",
  size: 12pt,
)
#show raw: set text(
  font: "TeX Gyre Cursor",
  size: 12pt,
)
#set par(
  justify: true,
)

// Points function
#let points(number) = {
  place(
    top + right,
    dx: 1in - 18pt,
  )[#text(airblue)[[#number %]]]
}

// Blank box
#let blank(width: 12pt) = {
  box(
    fill: ashgray.transparentize(50%),
    width: width,
    height: 12pt,
    baseline: 3pt,
  )
}

// Title
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt,
)
#align(center)[
  Relace \& Ekvivalence
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Mock test]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

// Warning
#align(center)[
  #box(
    stroke: 1pt + ashgray,
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: ashgray.transparentize(80%),
  )[
    Není-li uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně) vysvětlete
    svůj myšlenkový pochod. I v uzavřených úlohách.
  ]
]
#v(12pt)

// First page
= Součin množin \& relace
#v(6pt)
#block(width: 100%)[
  #points(25)
  Ať #text(crimson)[$A = {1, 2}$] a #text(airblue)[$B = {a, b, c}$]. Označte
  všechna *správná* tvrzení z níže uvedených. *Nemusíte* své odpovědi
  vysvětlovat.
  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] ${(1, a), (1, b), (1, c)}$ je relace z #text(crimson)[$A$]
    do~#text(airblue)[$B$].
  #v(6pt)
  - [ ] ${(a, b), (a, a), (c, a)}$ je relace *na* #text(airblue)[$B$] (tedy
    relace z #text(airblue)[$B$] do #text(airblue)[$B$]).
  #v(6pt)
  - [ ] Existuje *pět* relací z #text(crimson)[$A$] do
    #text(airblue)[$B$].
  #v(6pt)
  - [ ] Dvojice $(b, 2)$ leží v $#text(crimson)[$A$] times
    #text(airblue)[$B$]$.
  #v(6pt)
  - [ ] ${(a, 1), (a, 2)}$ je relace z #text(airblue)[$B$] do
    #text(crimson)[$A$].
  #v(6pt)
]
#v(5%)
#block(width: 100%)[
  #points(25)
  Relace $#text(raingreen)[$R$]$ z #text(crimson)[$A = {1, 2}$] do
  #text(airblue)[$B = {a, b, c}$] je *antisymetrická*, jestliže kdykoli je
  #text(crimson)[$a$] #text(raingreen)[v relaci] s #text(airblue)[$b$], nemůže
  být #text(airblue)[$b$] #text(raingreen)[v relaci] s #text(crimson)[$a$] (pro
  #text(crimson)[$a in A$] a #text(airblue)[$b in B$]). Jako příklad vezměte
  relaci „být matkou“ na množině lidí. Je-li žena matkou dítěte, ono dítě
  samozřejmě není matkou své vlastní matky.

  Uveďte příklad *antisymetrické* relace z #text(crimson)[$A$] do
  #text(airblue)[$B$] s *alespoň třemi dvojicemi*. *Vysvětlete*.
]
#pagebreak()

// Second page
= Ekvivalence
#v(12pt)
#block(width: 100%)[
  #points(25)
  Připomeňme, že relace _ekvivalence_ je dána třemi podmínkami:
  - *reflexivita*: každý prvek je ekvivalentní sám sobě;
  - *symetrie*: jestliže $a$ je ekvivalentní s $b$, pak $b$ je ekvivalentní s $a$;
  - *transitivita*: jestliže $a$ je ekv. s $b$ a $b$ je ekv. s $c$, pak $a$ je ekv. s $c$.

  Určete, zda je relace
  #math.equation(numbering: none, block: true)[
    #text(raingreen)[$R = {(1, 1), (2, 2), (3, 3), (1, 3), (3, 1), (1, 2)}$]
  ]
  ekvivalence na množině #text(crimson)[$A = {1, 2, 3, 4}$]. Pokud ne, doplňte
  *co nejméně dvojic*, aby se z ní ekvivalence stala. *Vysvětlete*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  Na níže uvedených diagramech jsou dvě různé ekvivalence na množině
  #text(crimson)[$A = {1, 2, 3, 4}$].
  #align(center)[
    #cetz.canvas({
      import cetz.draw: *

      content((-1, 1), text(crimson)[$1$], anchor: "mid")
      content((-1, 2), text(crimson)[$2$], anchor: "mid")
      content((-1, 3), text(crimson)[$3$], anchor: "mid")
      content((-1, 4), text(crimson)[$4$], anchor: "mid")

      content((0, 0), text(crimson)[$1$], anchor: "mid")
      content((1, 0), text(crimson)[$2$], anchor: "mid")
      content((2, 0), text(crimson)[$3$], anchor: "mid")
      content((3, 0), text(crimson)[$4$], anchor: "mid")
      for x in range(0, 4) {
        for y in range(1, 5) {
          circle((x, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
        }
      }

      circle((0, 0.95), stroke: 1pt + airblue, radius: 6pt)
      circle((1, 1.95), stroke: 1pt + airblue, radius: 6pt)
      circle((2, 2.95), stroke: 1pt + airblue, radius: 6pt)
      circle((3, 3.95), stroke: 1pt + airblue, radius: 6pt)

      circle((2, 3.95), stroke: 1pt + airblue, radius: 6pt)
      circle((3, 2.95), stroke: 1pt + airblue, radius: 6pt)
    
      content((6, 1), text(crimson)[$1$], anchor: "mid")
      content((6, 2), text(crimson)[$2$], anchor: "mid")
      content((6, 3), text(crimson)[$3$], anchor: "mid")
      content((6, 4), text(crimson)[$4$], anchor: "mid")

      content((7, 0), text(crimson)[$1$], anchor: "mid")
      content((8, 0), text(crimson)[$2$], anchor: "mid")
      content((9, 0), text(crimson)[$3$], anchor: "mid")
      content((10, 0), text(crimson)[$4$], anchor: "mid")
      for x in range(0, 4) {
        for y in range(1, 5) {
          circle((x + 7, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
        }
      }

      circle((7, 0.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((8, 1.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((9, 2.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((10, 3.95), stroke: 1pt + raingreen, radius: 6pt)

      circle((7, 3.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((10, 0.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((8, 0.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((10, 1.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((8, 3.95), stroke: 1pt + raingreen, radius: 6pt)
      circle((7, 1.95), stroke: 1pt + raingreen, radius: 6pt)
    })
  ]

  Pro obě ekvivalence určete *třídu ekvivalence* každého prvku z množiny
  #text(crimson)[$A$]. Tedy -- označíme-li tyto ekvivalence
  #text(airblue)[$E_1$] a #text(raingreen)[$E_2$] -- určete
  #math.equation(numbering: none, block: true)[
    $[#text(crimson)[$1$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$2$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$3$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$4$]]_(#text(airblue)[$E_1$])$  a
    $[#text(crimson)[$1$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$2$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$3$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$4$]]_(#text(raingreen)[$E_2$])$.
  ]
  *Nemusíte* své odpovědi vysvětlovat.
]
