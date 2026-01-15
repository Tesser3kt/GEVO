// Importy balíčků
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

// Definice vlastních barev
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let darkmagenta = rgb("#8B008B")
#let ashgray = rgb("#B2BEB5")

// Nastavení stránky a písem
#let page-counter(cur, last) = {
  strfmt("Strana {} z {}", cur, last)
}
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Test A
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

// Funkce na body
#let points(number) = {
  place(
    top + right,
    dx: 1in - 18pt,
  )[#text(airblue)[[#number %]]]
}

// Prázdné políčko
#let blank(width: 12pt) = {
  box(
    fill: ashgray.transparentize(50%),
    width: width,
    height: 12pt,
    baseline: 3pt,
  )
}

// Titulek
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt,
)
#align(center)[
  Logika a teorie množin
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Test A]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

// Upozornění
#align(center)[
  #box(
    stroke: 1pt + ashgray,
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: ashgray.transparentize(80%),
  )[
    Není-li uvedeno jinak, máte #text(crimson)[*vždy*] (alespoň stručně)
    vysvětlit svůj myšlenkový pochod. Platí to i pro uzavřené otázky.
  ]
]
#v(12pt)

// První strana
= Logika -- výroky a logické spojky
#v(6pt)
#block(width: 100%)[
  #points(25)
  Pro daný výrok
  #math.equation(numbering: none, block: true)[
    $(q and not p) <=>  p$
  ]
  určete, kdy je pravdivý (pro které pravdivostní hodnoty $p$ a $q$) a kdy je
  lživý. #text(crimson)[*Svou odpověď objasněte.*]\
  *Nápověda:* Můžete použít pravdivostní tabulku, pokud chcete.
]
#v(30%)
#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Každý logický výrok lze vyjádřit pouze pomocí spojek $not$, $and$ a $or$.
  Proveďte to pro implikaci; tedy, najděte výrok, který používá jen spojky
  $not$, $and$ a $or$ a je ekvivalentní výroku $p => q$.
  #text(crimson)[*Svou odpověď vysvětlete*.]
]
#pagebreak()

// Druhá strana
= Základní množinové operace
#v(12pt)
#block(width: 100%)[
  #points(35)
  #block(width: 100%)[
    Jsou dány množiny #text(crimson)[$A = {b, c, e}$],
    #text(airblue)[$B = {a, c, d}$]
    a #text(raingreen)[$C = {a, b, c, d}$].
    Určete množiny
    #math.equation(numbering: none, block: true)[
      $(#text(crimson)[$A$] without #text(airblue)[$B$]) union
      #text(raingreen)[$C$] #h(1em) "a" #h(1em) #text(crimson)[$A$] inter
      (#text(airblue)[$B$] inter #text(raingreen)[$C$])$.
    ]
    
    *Nemusíte* dávat žádné *vysvětlení*.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusová úloha]
  Pro množinu $A$ existuje množina, která obsahuje všechny podmnožiny $A$, a
  značí se $2^A$. Například, pro
  #text(crimson)[$A = {a, b}$] je
    #math.equation(numbering: none, block: true)[
      $2^(#text(crimson)[$A$]) = {{}, {a}, {b}, {a,b}}$.
    ]
  Zkuste vysvětlit, *proč* se množina všech podmnožin značí $2^A$. Kolik prvků
  má $2^A$, pokud má $A$ $n$ (nějaké přirozené číslo) prvků?
  #text(crimson)[*Vysvětlete se.*]
]
#pagebreak()

= Vennovy diagramy

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Je dán následující Vennův diagram. Určete množinu, kterou znázorňuje.
    *Nemusíte* uvádět *vysvětlení*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          ab-fill: raingreen,
          bc-fill: raingreen,
        )
      })
    ]
  ]
  #v(10%)
][
  #block(width: 100%)[
    #points(20)
    Nakreslete Vennův diagram pro následující výraz:
    #math.equation(numbering: none, block: true)[
      $(A inter C) without B$.
    ]
    Nemusíte *nic vysvětlovat*.
  ]
]
#v(18%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonusová úloha]
  Nakreslit Vennův diagram se čtyřmi množinami je poměrně obtížné a nelze to
  udělat pouze pomocí kružnic. Uvažujte následující obrázek pro množiny
  #text(crimson)[$A$], #text(airblue)[$B$], #text(raingreen)[$C$] a
  #text(darkmagenta)[$D$]:
  #align(center)[
    #cetz.canvas({
      import cetz.draw: *
      circle((0, 0), radius: 1cm, stroke: 1pt + crimson);
      circle((1cm, 0), radius: 1cm, stroke: 1pt + airblue);
      circle((0cm, -1cm), radius: 1cm, stroke: 1pt + raingreen);
      circle((1cm, -1cm), radius: 1cm, stroke: 1pt + darkmagenta);
    })
  ]
  Dokázali byste najít takovou kombinaci množinových operací s
  #text(crimson)[$A$], #text(airblue)[$B$],
  #text(raingreen)[$C$] a #text(darkmagenta)[$D$], pro kterou v tomto
  diagramu neexistuje odpovídající oblast? *Nemusíte* uvádět *vysvětlení*.
]

