// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.5.2"
#import "@preview/cetz-venn:0.2.0"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.2" as icu

// Emojis
#import emoji: airplane, banana,darts, boat, bison, lollipop, bird

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
      Verse A
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
#let clbr(body) = text(fill: rgb("#5C4033"))[#body]
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
  #text(size: 18pt)[1.C Matematika -- Verse A]
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
      $#clbr[$d$] = {1,2,3,4,5}$
    ]
#block(width: 100%)[
  #points(25)
  Na prázdná místa doplntě buď symbol *podmnožiny* ($subset$) nebo *rovnosti*
  (=) pokud je takto vytvořený výrok pravdivý, v opačném případě pole
  zaškrtněte. Argumentuje z *definice* podmnožiny nebo rovnosti.

  #v(0.5cm)
#math.equation(numbering: none, block: true)[
  #clb[$b$] #boxik() #clr[$a$]  #h(3cm) #clbr[$d$] #boxik() #clr[$a$]  #h(3cm) #clb[$b$] #boxik() ${1004,2,10}$
]

]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Pomocí *axiomu vydělení* získejte množiny #clb[$b$], #clg[$c$] z množiny #clr[$a$]. Přesněji:
  najděte výroky $p(x), q(x)$ takové, že $#clb[$b$] = {x in #clr[$a$] |
  p(x)}$ a $#clg[$c$] = {x in  #clr[$a$] | q(x)}$. V definici obou výroků
  nemůžete použít explicitně prvky #clb[$b$] ani #clg[$c$]. Hledejte nějaký
  společný vztah pro všechna čísla v těchto množinách.
]

#pagebreak()

  #points(25)
  #block(width: 100%)[
    Do následujícího diagramu množin #clr[$a$], #clbr[$d$] dokreslete množinu
    $e = {6,7,1,10}$. Do každé části diagramu dopište jaké prvky representuje (jaké prvky se něm nacházejí). Dále v diagramu zvýrazněte množinu $#clr[$a$] without e$.
    #v(1cm)
  #align(center)[
    #cetz.canvas({
    for (angle, color, label, anchor) in (
          (180deg, crimson, "a", "east"),
          (0deg, rgb("#5C4033"), "d", "west"), 
        ) {
          cetz.draw.circle((angle, 1.5), radius: 3, stroke: color)
          cetz.draw.content(
            (angle, 5), 
            text(fill: color, weight: "bold", label),
            anchor: anchor,
          )
        }
      })
  ]
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
  definice nadmnožiny je, že $x$ je nadmnožinou $y$ když $y$ je podmnožinou
  $x$. Definujte tento pojem formálně, začněte s *axiomem existenzionality* a z
  nten upravte aby seděl pojmu *nadmnožiny*.
]

