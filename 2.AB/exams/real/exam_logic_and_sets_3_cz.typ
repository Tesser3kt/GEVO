// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.0"

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Set page and fonts
#let page-counter(cur, last) = {
  strfmt("Strana {} of {}", cur, last)
}
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Test C
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #icu-datetime.fmt(datetime.today(), locale: "cs-CZ", length: "long")
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
  Logika a teorie množin
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Test C]
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
    Pokud není uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně)
    vysvětlete svůj myšlenkový pochod. I v uzavřených otázkách.
  ]
]
#v(12pt)

= Logika -- výroky a operátory
#v(6pt)
#block(width: 100%)[
  #points(25)
  Je výrok
  #align(center)[
    $(p => q) or not q$
  ]
]
*tautologie*? Čili, je #text(crimson)[*vždy pravdivý*] bez ohledu na to, zda
jsou $p$ a $q$ pravdivé nebo lživé? *Vysvětlete*.
#v(30%)

#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Uvažujte nový logický operátor $plus.o$ daný následující pravdivostní
  tabulkou.
  #align(center)[
    #table(
      columns: (auto, auto, auto),
      inset: 8pt,
      align: horizon,
      stroke: (x, y) => {
        if 0 <= y and y < 4 {
          (bottom: 1pt + ashgray)
        }
        if (0 <= x and x < 2) {
          (right: 1pt + ashgray)
        }
      },
      table.header([$p$], [$q$], [$p plus.o q$]),
      [$T$], [$T$], [$F$],
      [$T$], [$F$], [$T$],
      [$F$], [$T$], [$T$],
      [$F$], [$F$], [$F$],
    )
  ]
  Zapište výrok $p plus.o q$ pouze pomocí standardních logických operátorů
  $not$, $and$ a $or$.
]
#pagebreak()

= Základní množinové operace

#block(width: 100%)[
  #points(35)
  Jsou dány množiny $A = {a, b, c, d, e}$, $B = {b, e}$ a $C = {a, d, f}$.
  Pomocí množinových operací (kterýchkoliv chcete) použitých na $A$, $B$ a $C$
  vytvořte množiny
  #math.equation(numbering: none, block: true)[
    ${b, e, f}$ #h(1em) and #h(1em) ${a, d}$.
  ]
]
Nic *nemusíte* *vysvětlovat*.
#v(45%)

#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Uvažujte logický operátor $plus.o$ z předchozí bonusové úlohy. Určete množinu
  $A triangle C = {x | x in A plus.o x in C}$, kde $A$ a $C$ jsou definovány
  výše. *Okomentujte* způsob, který jste k určení množiny použili.
]

#pagebreak()

= Vennovy diagramy

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Na základě Vennova diagramu níže určete množinu, kterou znázorňuje.
    *Nemusíte* uvádět *vysvětlení*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          a-fill: raingreen,
          b-fill: raingreen,
          ab-fill: raingreen,
          ac-fill: raingreen,
        )
      })
    ]
  ]
  #v(15%)
][
  #block(width: 100%)[
    #points(20)
    Nakreslete Vennův diagram pro následující výraz.
    #math.equation(numbering: none, block: true)[
      $(A inter B inter C) union (B without C)$
    ]
    *Nemusíte* nic *vysvětlovat*.
  ]
]
#v(35%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusový příklad]
  *Doplněk* množiny $X$ v množině $Y$ je definován jako $Y without X$.
  Nakreslete Vennův diagram *doplňku* množiny $(A without B) inter C$ v množině
  $A union B union C$.
]


