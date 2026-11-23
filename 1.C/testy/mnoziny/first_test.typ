// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.5.3"
#import "@preview/cetz-venn:0.2.0": venn3
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.2" as icu


// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")
#let brown = rgb("#5C4033")
#let jazzberry = rgb("#A50B5E")
#let amber = rgb("#D48A00")

// diagram shorthand
#let venn-box(
  box-label,
  only-e,
  only-a,
  only-d,
  e-and-a,
  e-and-d,
  a-and-d,
  all-three,
) = {
  align(center)[
    // Box is 7.0 x 6.6 units -> ~7.35cm x 6.9cm at length: 1.05cm (fits 2x2 on one page)
    #cetz.canvas(length: 1.05cm, {
      import cetz.draw: *

      // Outer box
      rect((-3.5, -3.5), (3.5, 3.1), stroke: 1pt + black)

      // Box label (A, B, or C) in the top-left corner
      // content(
      //   (-3.25, 2.85),
      //   anchor: "north-west",
      //   text(weight: "bold", size: 13pt)[#box-label],
      // )

      // Three full circles of radius 2, spaced well apart
      circle((-1.0, 0.58), radius: 2, stroke: 1.5pt + amber) // e
      circle((1.0, 0.58), radius: 2, stroke: 1.5pt + crimson) // a
      circle((0, -1.15), radius: 2, stroke: 1.5pt + jazzberry) // d

      // Set labels just outside each circle
      content((-2.75, 2.25), text(fill: amber, weight: "bold")[e])
      content((2.75, 2.25), text(fill: crimson, weight: "bold")[a])
      content((-2.15, -2.85), text(fill: jazzberry, weight: "bold")[d])

      // Region numbers placed at the exact geometric centers of the 7 regions
      set-style(content: (padding: 0pt))
      content((-1.73, 1.0), text(size: 9pt)[#only-e])
      content((1.73, 1.0), text(size: 9pt)[#only-a])
      content((0, -2.0), text(size: 9pt)[#only-d])
      content((0, 1.35), text(size: 9pt)[#e-and-a])
      content((-1.17, -0.68), text(size: 9pt)[#e-and-d])
      content((1.17, -0.68), text(size: 9pt)[#a-and-d])
      content((0, 0), text(size: 9pt)[#all-three])
    })
  ]
}

// Emojis
#import emoji: airplane, banana, bird, bison, boat, darts, lollipop


// Set page and fonts
#let page-counter(cur, last) = {
  strfmt("Strana {} ze {}", cur, last)
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
      Test A
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

#let boxik() = box(width: 1.2em, height: 1.2em, fill: luma(220), baseline: 20%)

// Color functions.
#let clr(body) = text(fill: crimson)[#body]
#let clb(body) = text(fill: airblue)[#body]
#let clg(body) = text(fill: raingreen)[#body]
#let clbr(body) = text(fill: brown)[#body]
#let clm(body) = text(fill: jazzberry)[#body]
#let clo(body) = text(fill: amber)[#body]
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
  #text(size: 18pt)[1.C Matematika -- Test A]
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

Pro účely prvních tří úloh definujeme následující množiny
#list[
  $#clr[$a$] = {1,2,10,1004,12345,5}$,
][
  $#clb[$b$] = {10,2,1004}$,
][
  $#clg[$c$] = {12345,1004}$.
][
  $#clm[$d$] = {1,2,3,4,5}$
]
#block(width: 100%)[
  #points(25)
  Na prázdná místa doplňte buď symbol *podmnožiny* ($subset.eq$) nebo *rovnosti*
  (=), pokud je takto vytvořený výrok pravdivý, v opačném případě pole
  zaškrtněte. Argumentujte z *definice* podmnožiny nebo rovnosti.

  #v(0.5cm)
  #math.equation(numbering: none, block: true)[
    #clb[$b$] #boxik() #clr[$a$]  #h(3cm) #clm[$d$] #boxik() #clr[$a$]  #h(
      3cm,
    ) #clb[$b$] #boxik() ${1004,2,10}$
  ]

]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Pomocí *axiomu vydělení* získejte množiny #clb[$b$], #clg[$c$] z množiny
  #clr[$a$]. Přesněji: najděte výroky $p(x), q(x)$ takové, že $#clb[$b$] = {x in
    #clr[$a$] | p(x)}$ a $#clg[$c$] = {x in #clr[$a$] | q(x)}$. V definici obou
  výroků nesmíte použít přímo prvky #clb[$b$] ani #clg[$c$]. Hledejte nějaký
  společný vztah pro všechna čísla v těchto množinách.\
  #show math.equation: set text(
    size: 10pt,
  )
  #text(size: 10pt)[
    *Poznámka*: výroky $p(x)$ a $q(x)$ můžete psát slovy a přirozeně, například:
    "$x$ je sudé," nebo "$x$ končí nulou."
  ]
]

#pagebreak()

#points(25)
#block(width: 100%)[
  Z následujících diagramů vyberte ten, který správně representuje množiny
  #clr[$a$], #clm[$d$] a $#clo[$e$] = {6,7,1,10}$.  Dále do vybraného diagramu
  zvýrazněte množinu $#clr[$a$] without #clo[$e$]$.
  #v(1cm)
  // 2-column grid so A, B, and C fit comfortably on a single page
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,

    venn-box(
      "A",
      [6, 7],
      [1004, \ 12345],
      [3, 4],
      [10],
      [],
      [2, 5],
      [1],
    ),

    venn-box(
      "B",
      [],
      [12345],
      [3, 4],
      [10, 1004],
      [6, 7],
      [2, 5],
      [1],
    ),

    venn-box(
      "C",
      [7],
      [1004, \ 12345],
      [3, 4, 6],
      [10],
      [],
      [5],
      [1, 2],
    ),
  )
]

#pagebreak()

#block(width: 100%)[
  #points(25)
  Mějme množiny $#clr[$a$] = {{airplane},{lollipop,bison,boat.sail}}$ a
  $#clb[$b$]={{boat.sail},{darts}}$. *Pouze* pomocí *axiomu součtu* a *dvojice* z
  množin #clr[$a$], #clb[$b$] utvořte množinu $#clg[$c$]={airplane,lollipop,bison,boat.sail,darts}$. *Důkladně
  komentujte* použití axiomů.
]

#v(1fr)
#block(width: 100%)[
  #points(20)
  === #text(airblue)[Bonusová úloha]
  Jako opačný pojem k pojmu *podmnožina* definujeme *nadmnožinu*. Slovní
  definice nadmnožiny je, že $x$ je nadmnožinou $y$, když $y$ je podmnožinou
  $x$. Definujte tento pojem formálně, začněte s *axiomem extensionality* a ten
  upravte, aby odpovídal pojmu *nadmnožiny*.
]

