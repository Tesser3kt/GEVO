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
      Test D
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
  Logika a teorie množin
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Test D]
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
    Není-li uvedeno jinak, máte #text(crimson)[*vždy*] (alespoň stručně)
    vysvětlit svůj myšlenkových pochod. I v uzavřených otázkách.
  ]
]
#v(12pt)

= Logika -- výroky a operátory
#v(6pt)
#block(width: 100%)[
  #points(25)
  Je výrok
  #align(center)[
    $(p and q) or (not p and not q)$
  ]
]
*tautologie*? Tedy, je #text(crimson)[*vždy pravdivý*] bez ohledu na to, zda jsou
$p$ a $q$ pravdivé nebo lživé? *Vysvětlete*.
#v(30%)

#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Uvažujte nový logický operátor $dot.o$ daný následující pravdivostní tabulkou.
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
      table.header([$p$], [$q$], [$p dot.o q$]),
      [$T$], [$T$], [$T$],
      [$T$], [$F$], [$T$],
      [$F$], [$T$], [$F$],
      [$F$], [$F$], [$T$],
    )
  ]
  Zapište výrok $p dot.o q$ užitím standardních logických operátorů $not$,
  $and$, $or$, $=>$ a $<=>$.
]
#pagebreak()

= Základní množinové operace

#block(width: 100%)[
  #points(35)
  Jsou dány množiny $A = {1, 2, 3, 4, 5}$, $B = {2, 4, 5}$ a $C = {1, 4, 5}$.
  Určete množiny
  #math.equation(numbering: none, block: true)[
    $A without (B union C) " a " (A union B) inter C$.
  ]
]
Svůj postup *nemusíte vysvětlovat*.
#v(45%)

#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Uvažujte logický operátor $dot.o$ z předchozího bonusového příkladu.
  Určete množinu ${x | x in A dot.o x in B}$, kde $A$ a $B$ jsou definovány
  výše. *Okomentujte* způsob, který jste k určení množiny použili.
]

#pagebreak()

= Vennovy diagramy

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Určete množinu, kterou znázorňuje diagram níže. *Nemusíte* uvádět
    *vysvětlení*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          b-fill: raingreen,
          ab-fill: raingreen,
          ac-fill: raingreen,
          abc-fill: raingreen,
          bc-fill: raingreen,
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
      $(B union C) without (A inter C)$
    ]
    *Nemusíte* nic *vysvětlovat*.
  ]
]
#v(35%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusová úloha]
  *Doplněk* množiny $X$ v množině $Y$ je definován jako $Y without X$.
  Nakreslete Vennův diagram *doplňku* množiny $(A inter B) union C$ v množině
  $A union B union C$.
]

