// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.5.2"
#import "@preview/cetz-venn:0.2.0"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.2" as icu

// Emojis
#import emoji: airplane, alien, banana, broom, chicken, drum, lollipop, magnet

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Set page and fonts
#let page-counter(cur, last) = {
  strfmt("Strana {} z {}", cur, last)
}

// Set list properties
#set list(indent: 12pt)

#set text(lang: "cs")
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    set text(size: 12pt, font: "TeX Gyre Schola")
    if current-page > 1 [
      Mock test
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #icu.fmt(datetime.today(), locale: "cs", length: "long")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  },
)
#show heading.where(
  level: 1,
): it => block(width: 100%)[
  #set text(font: "TeX Gyre Adventor", 14pt)
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

// Color functions.
#let clr(body) = text(fill: crimson)[#body]
#let clb(body) = text(fill: airblue)[#body]
#let clg(body) = text(fill: raingreen)[#body]
#let cla(body) = text(fill: ashgray)[#body]

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
  Množinové operace
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[1.C Matematika -- Mock test]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

// Warning
#align(center)[
  #box(
    stroke: 1pt + airblue.transparentize(60%),
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: airblue.transparentize(90%),
  )[
    Není-li uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně) objasněte
    svůj myšlenkový pochod. I v uzavřených otázkách.\
    Hodnotí se především systematický přístup k řešení.\
    Při řešení #text(airblue)[*smíte*] používat své poznámky i online materiály.
    Umělou inteligenci používat #text(crimson)[*nesmíte*].
  ]
]
#v(12pt)

#block(width: 100%)[
  #points(25)
  Ať #clr[$a$], #clb[$b$], #clg[$c$] jsou libovolné množiny vyobrazené na
  diagramu níže. Zakreslete do něj množinu $#clr[$a$] without (#clb[$b$] union
    #clg[$c$])$. Najděte jiné vyjádření pro téže množinu *bez využití
  sjednocení*. *Vysvětlete, jak jste na toto vyjádření přišli.*
  #align(center)[
    #cetz.canvas({
      cetz-venn.venn3(stroke: none)
      for (angle, color) in (
        (150deg, crimson),
        (30deg, airblue),
        (270deg, raingreen),
      ) {
        cetz.draw.circle((angle, 0.75), radius: 1, stroke: color)
      }
    })
  ]
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Nejprve si zvlášť zakreslíme do diagramu množinu #clr[$a$] a množinu
  $#clb[$b$] union #clg[$c$]$.
  #align(center)[
    #grid(columns: 2, gutter: 1em)[
      #cetz.canvas({
        cetz-venn.venn3(
          stroke: none,
          a-fill: black,
          ab-fill: black,
          ac-fill: black,
          abc-fill: black,
        )
        for (angle, color) in (
          (150deg, crimson),
          (30deg, airblue),
          (270deg, raingreen),
        ) { cetz.draw.circle((angle, 0.75), radius: 1, stroke: color) }
      })
    ][
      #cetz.canvas({
        cetz-venn.venn3(
          stroke: none,
          ab-fill: black,
          ac-fill: black,
          abc-fill: black,
          b-fill: black,
          c-fill: black,
          bc-fill: black,
        )
        for (angle, color) in (
          (150deg, crimson),
          (30deg, airblue),
          (270deg, raingreen),
        ) {
          cetz.draw.circle((angle, 0.75), radius: 1, stroke: color)
        }
      })
    ]
  ]
  Teď od obrázku nalevo "odmažeme" vše z obrázku napravo. Odmazanou část
  zvýrazníme #cla[šedě]. Výsledkem je černá část diagramu níže.
  #align(center)[
    #cetz.canvas({
      cetz-venn.venn3(
        stroke: none,
        a-fill: black,
        ab-fill: ashgray,
        ac-fill: ashgray,
        abc-fill: ashgray,
      )
      for (angle, color) in (
        (150deg, crimson),
        (30deg, airblue),
        (270deg, raingreen),
      ) { cetz.draw.circle((angle, 0.75), radius: 1, stroke: color) }
    })
  ]
  Nalézt jiné vyjádření pro množinu $#clr[$a$] without (#clb[$b$] union
    #clg[$c$])$ lze mnoha způsoby, klidně i metodou "pokus, omyl" podle obrázku.
  My ukážeme jeden postup využívající logiky. Totiž, když je množina $x$ prvkem
  $#clr[$a$] without (#clb[$b$] union #clg[$c$])$, pak leží v #clr[$a$] a
  zároveň neleží v #clb[$b$] ani v #clg[$c$]. Zapsáno v jazyce výrokové logiky:
  #math.equation(numbering: none, block: true)[
    $(x in #clr[$a$]) and (x in.not #clb[$b$]) and (x in.not #clg[$c$])$.
  ]
  Ovšem, množina všech prvků $x$, které splňují $(x in #clr[$a$]) and (x in.not
    #clb[$b$])$, je množina $#clr[$a$] without #clb[$b$]$. Podobně, množina všech
  prvků $x$, které splňují, že $(x in #clr[$a$]) and (x in.not #clg[$c$])$, je
  množina $#clr[$a$] without #clg[$c$]$. Když musí $x$ být v obou těchto
  množinách zároveň, tak musí být v jejich *průniku*. Platí tedy
  #math.equation(numbering: none, block: true)[
    $#clr[$a$] without (#clb[$b$] union #clg[$c$]) = (#clr[$a$] without
      #clb[$b$]) inter (#clr[$a$] without #clg[$c$])$.
  ]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Použitím *axiomu dvojice* a *axiomu sumy* vytvořte ze tří množin #clr[$a$],
  #clb[$b$], #clg[$c$] množinu ${#clr[$a$], #clb[$b$], #clg[$c$]}$. Napište
  *přesně*, jak je používáte.\
  #show math.equation: set text(
    font: "TeX Gyre Schola Math",
    size: 10pt,
  )
  #text(size: 10pt)[*Hint*: axiom dvojice též říká, že ke každé množině $a$
    existuje množina ${a}$ (stačí v jeho znění položit $a = b$, čili vzít dvě
    stejné množiny).]
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Použijeme *axiom dvojice* třikrát a *axiom sumy* jednou.

  Nejprve z množin #clr[$a$] a #clb[$b$] vyrobíme dvojici ${#clr[$a$],
    #clb[$b$]}$. Potom opět pomocí axiomu dvojice vyrobíme množinu
  ${#clg[$c$]}$, jak radí *hint*. Konečně, na množiny ${#clr[$a$], #clb[$b$]}$ a
  ${#clg[$c$]}$ pustíme ještě naposled axiom dvojice, čímž získáme množinu
  ${{#clr[$a$], #clb[$b$]}, {#clg[$c$]}}$. Na tuto množinu použijeme axiom sumy
  a dostaneme množinu ${#clr[$a$], #clb[$b$], #clg[$c$]}$.

  Povšimněte si, že poslední dva kroky jsou prostě sjednocení množin
  ${#clr[$a$], #clb[$b$]}$ a ${#clg[$c$]}$. Z definice sjednocení je totiž
  #math.equation(numbering: none, block: true)[
    ${#clr[$a$], #clb[$b$]} union {#clg[$c$]} = union.big {{#clr[$a$],
        #clb[$b$]}, {#clg[$c$]}}$.
  ]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  #block(width: 100%)[
    Mějme množiny
    #list[
      $#clr[$a$] = {airplane, banana, lollipop, drum}$,
    ][
      $#clb[$b$] = {banana, drum, chicken, broom}$,
    ][
      $#clg[$c$] = {alien, drum, banana, magnet}$.
    ]
  ]
  Popište následující množiny:
  #list[
    $#clr[$a$] without #clb[$b$]$,
  ][
    ${x in #clg[$c$] | (x in.not #clr[$a$]) or (x in.not #clb[$b$])}$,
  ][
    $union.big {#clg[$c$] without #clb[$b$], {lollipop}}$.
  ]
  *Svůj postup stručně vysvětlete.*
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  #list[
    Množina $#clr[$a$] without #clb[$b$]$ obsahuje všechny prvky z #clr[$a$],
    které nejsou v #clb[$b$]. Je to tudíž množina ${airplane, lollipop}$.
  ][
    Množina ${x in #clg[$c$] | (x in.not #clr[$a$]) or (x in.not #clb[$b$])}$
    obsahuje prvky množiny #clg[$c$], které nejsou v #clr[$a$] nebo nejsou v
    #clb[$b$]. Zde si můžeme pomoci základní výrokovou logikou. Totiž, výrok $(x
      in.not #clr[$a$]) or (x in.not #clb[$b$])$ je ekvivalentní výroku $not(
      (x
        in #clr[$a$]) and (x in #clb[$b$])
    )$. Výrok v závorkách je ale přesně výrok, který definuje *průnik* množin
    #clr[$a$] a #clb[$b$], tedy množinu všech prvků, jež *jsou v #clr[$a$] a
    zároveň v #clb[$b$]*. Proto je zadaná množina přesně $#clg[$c$] without
    (#clr[$a$] inter #clb[$b$])$. Tu již snadno dopočítáme: ${alien, magnet}$.

    Pochopitelně, tuto množinu jsme byli mohli určit i bez hrátek s výrokovou
    logikou...
  ][
    Nejprve určíme, že $#clg[$c$] without #clb[$b$] = {alien, magnet}$. Množina
    $union.big {{alien, magnet}, {lollipop}}$ je zkrátka *sjednocením* množin
    ${alien, magnet}$ a ${lollipop}$, čili ${alien, magnet, lollipop}$.
  ]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Pomocí *axiomu vydělení* popište množinu zakreslenou černě na diagramu níže
  vzniklou z množin #clr[$a$] a #clb[$b$]. Přesněji: najděte množinu $z$ a výrok
  $p(x)$, tak aby černá množina níže přesně odpovídala množině ${x in z |
    p(x)}$. *Vysvětlete.*
  #align(center)[
    #cetz.canvas({
      cetz-venn.venn2(
        stroke: none,
        a-fill: black,
        b-fill: black,
      )
      for (angle, color) in (
        (180deg, crimson),
        (0deg, airblue),
      ) { cetz.draw.circle((angle, 0.61), radius: 1, stroke: color) }
    })
  ]
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Protože výsledná množina obsahuje prvky z obou množin: #clr[$a$] i #clb[$b$],
  bude muset být množinou $z$ jejich sjednocení: $#clr[$a$] union #clb[$b$]$.

  Vidíme, že černá množina obsahuje všechny prvky z $#clr[$a$] union #clb[$b$]$
  až na ty, které jsou v~průniku $#clr[$a$] inter #clb[$b$]$. Můžeme tedy za
  výrok $p(x)$ zvolit výrok $x in.not #clr[$a$] inter #clb[$b$]$. Pak dostaneme
  výsledný zápis
  #math.equation(numbering: none, block: true)[
    ${x in #clr[$a$] union #clb[$b$] | x in.not #clr[$a$] inter #clb[$b$]}$,
  ]
  který je jedním možným popisem černé množiny na diagramu.
]
#v(1fr)
#block(width: 100%)[
  #points(20)
  === #text(airblue)[Bonusová úloha]
  *Podrobně* argumentujte, že platí-li pro dvě množiny #clr[$a$] a #clb[$b$]
  rovnost $#clr[$a$] without #clb[$b$] = #clb[$b$] without #clr[$a$]$, pak již
  nezbytně $#clr[$a$] = #clb[$b$]$.
]

