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
  strfmt("Page {} of {}", cur, last)
}
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Mock Exam
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
  #text(size: 18pt)[2.AB PreIB Maths -- Mock Test]
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
    Není-li uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně) objasněte
    svůj myšlenkový pochod. I v uzavřených otázkách.
  ]
]
#v(12pt)

// První strana
= Logika -- výroky a operátory
#v(6pt)
#block(width: 100%)[
  #points(25)
  Předpokládejme, že výrok $p$ je lživý a jiný výrok $q$ je také lživý. Je výrok
  #align(center)[
    $(p => q) or q$
  ]
  pravdivý, nebo lživý? #text(crimson)[*Rozveďte.*]
]
#v(30%)
#block(width: 100%)[
  === #text(airblue)[Bonusový úkol]
  #points(10)
  Doplňte výroky $p$ a $q$ (nemusíte nutně použít oba) do prázdných míst tak,
  aby výrok
  #align(center)[
    $(not p => #blank()) <=> (#blank() or q)$
  ]
  byl *vždy* pravdivý nezávisle na tom, zda jsou samy $p$ a $q$ pravdivé nebo
  lživé. #text(crimson)[*Ověřte, že je vaše odpověď správná.*]
]
#pagebreak()

// Druhá strana
= Základní množinové operace
#v(12pt)
#block(width: 100%)[
  #points(35)
  #block(width: 100%)[
    Jsou dány množiny $A = {2, 3, 5}$, $B = {3, 4, 5}$ a $C = {1, 2, 3, 4}$.
    Určete množiny
    #align(center)[
      $(A union B) inter C$ #h(1em) a #h(1em) $C without (A inter B)$.
    ]
    Nemusíte uvádět *žádné vysvětlení*.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusový úkol]
  #block(width: 100%)[
    Existuje množinová operace zvaná *symetrický rozdíl* množin $A$ a $B$,
    symbolicky $A triangle.stroked.t B$. Lze ji definovat takto:
    #align(center)[
      $A triangle.stroked.t B = (A without B) union (B without A)$.
    ]
    Popište tuto množinu užitím #text(crimson)[*pouze logických operátorů*]. Čili,
    najděte výrok $p(x)$ (složený z výroků $x in A$ a $x in B$) takový, aby $A
    triangle.stroked.t B = {x | p(x)}$.
  ]
]
#pagebreak()

= Vennovy diagramy

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Na základě níže uvedeného Vennova diagramu určete množinu, kterou
    zobrazuje. Nemusíte uvádět *žádné vysvětlení*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          b-fill: raingreen,
          c-fill: raingreen,
          bc-fill: raingreen,
          abc-fill: raingreen,
          ac-fill: raingreen,
        )
      })
    ]
  ]
  #v(20%)
][
  #block(width: 100%)[
    #points(20)
    Nakreslete Vennův diagram pro následující výraz:
    #align(center)[
      $(A inter B) union (A without C)$.
    ]
    Nemusíte *nic vysvětlovat*.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusový úkol]
  Dokažte (pomocí Vennových diagramů, logiky nebo čehokoli jiného), že
  #align(center)[
    $(A inter C) without (A inter B) subset.eq C without B$
  ]
  pro libovolné tři množiny $A$, $B$ a $C$.
]

