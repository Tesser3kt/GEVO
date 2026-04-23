// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.1" as icu

#import emoji: dog, eagle, flamingo

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Aux functions
#let mycirc(fill: crimson) = {
  circle(radius: 4pt, stroke: fill)
}
#let myrect(fill: crimson) = {
  rect(width: 7pt, height: 7pt, stroke: fill)
}

#let clr(body) = {
  text(crimson)[#body]
}
#let clb(body) = {
  text(airblue)[#body]
}
#let clg(body) = {
  text(raingreen)[#body]
}

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
      Test A
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #icu.fmt(
        datetime.today(),
        locale: "cs",
        length: "long",
      )
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
  Relace a ekvivalence
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Test A]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
  lang: "cs",
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
    Není-li řečeno jinak, #clr[*vždy*] aspoň stručně objasněte svůj myšlenkový
    pochod. I v uzavřených úlohách.
  ]
]
#v(12pt)

// First page
= Součin množin a relace
#v(6pt)
#block(width: 100%)[
  #points(25)
  Nechť #text(crimson)[$A = {#mycirc(), #myrect()}$] a #text(airblue)[$B = {dog,
    flamingo, eagle}$]. Zaškrtněte všechna *pravdivá* tvrzení z níže uvedených.
  *Nemusíte nic vysvětlovat*.

  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] ${(dog, #mycirc()), (dog, #myrect()), (flamingo, #mycirc())}$ je
    relace z #clr[$A$] do #clb[$B$].
  #v(6pt)
  - [ ] Součin $#clr[$A$] times #clb[$B$]$ má právě *šest* prvků.
  #v(6pt)
  - [ ] Prvek $(flamingo, flamingo)$ leží v $#clb[$B$] times #clb[$B$]$.
  #v(6pt)
  - [ ] Množiny $#clr[$A$] times #clb[$B$]$ a $#clb[$B$] times #clr[$A$]$
    mají společné právě *dva* prvky.
  #v(6pt)
  - [ ] ${(#mycirc(), #mycirc()), (#myrect(), #myrect())}$ je relace na
    #clr[$A$].
  #v(6pt)
]
#block(width: 100%)[
  #points(25)
  Relace #clg[$F$] z #clr[$A$] do #clb[$B$] (#clr[$A$] a #clb[$B$] jsou
  stejné jako výše) se nazývá *funkce*, jestliže každý prvek #clr[$a in A$] je
  #clg[v relaci] s *právě jedním* prvkem #clb[$b in B$]. Níže vidíte obrázky
  dvou relací z #clr[$A$] do #clb[$B$]. Jsou to funkce? *Proč*?
  #grid(
    columns: (1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), dog, anchor: "mid", name: "dog")
      content((0, 1), flamingo, anchor: "mid", name: "flam")
      content((0, 2), eagle, anchor: "mid", name: "eagle")

      content((2, 0), mycirc(), anchor: "mid", name: "circ")
      content((2, 1), myrect(), anchor: "mid", name: "rect")

      line("dog", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("eagle", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("flam", "rect", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), dog, anchor: "mid", name: "dog")
      content((0, 1), flamingo, anchor: "mid", name: "flam")
      content((0, 2), eagle, anchor: "mid", name: "eagle")

      content((2, 0), mycirc(), anchor: "mid", name: "circ")
      content((2, 1), myrect(), anchor: "mid", name: "rect")

      line("dog", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("dog", "rect", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("flam", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("eagle", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
  )
]
=== #clb[Bonusová úloha]
#block(width: 100%)[
  #points(10)
  *Složení* relací $R$ z $A$ do $B$ a $S$ z $B$ do $C$ je
  relace značená jako $R compose S$ z $A$ do $C$, která je definována tak, že:
  #math.equation(numbering: none, block: true)[
    $a(R compose S)c$~právě když~$a R b$~a~$b S c$
  ]
  pro libovolné prvky $a in A, b in B, c in C$. Nakreslete obrázek relace
  $R compose S$, jestliže obrázky relací $R$ a $S$ jsou níže.
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), dog, anchor: "mid", name: "dog")
      content((0, 1), flamingo, anchor: "mid", name: "flam")
      content((0, 2), eagle, anchor: "mid", name: "eagle")

      content((2, 0), mycirc(fill: black), anchor: "mid", name: "circ")
      content((2, 1), myrect(fill: black), anchor: "mid", name: "rect")

      content((1, 3), [#clg[$R$]], anchor: "mid")

      line("dog", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("eagle", "circ", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("flam", "rect", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), mycirc(fill: black), anchor: "mid", name: "circ")
      content((0, 1), myrect(fill: black), anchor: "mid", name: "rect")

      content((2, 0), [$1$], anchor: "mid", name: "1")
      content((2, 1), [$2$], anchor: "mid", name: "2")
      content((2, 2), [$3$], anchor: "mid", name: "3")

      content((1, 3), [#clb[$S$]], anchor: "mid")

      line("circ", "1", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
      line("circ", "2", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
      line("rect", "3", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), dog, anchor: "mid", name: "dog")
      content((0, 1), flamingo, anchor: "mid", name: "flam")
      content((0, 2), eagle, anchor: "mid", name: "eagle")

      content((2, 0), [$1$], anchor: "mid", name: "1")
      content((2, 1), [$2$], anchor: "mid", name: "2")
      content((2, 2), [$3$], anchor: "mid", name: "3")

      content(
        (1, 3),
        [Sem nakreslete $R compose S$.],
        anchor: "mid",
        name: "eagle",
      )
    })],
  )
]
#pagebreak()

// Second page
= Ekvivalence
#v(12pt)
#block(width: 100%)[
  #points(25)
  Připomeňme, že relace _ekvivalence_ je dána třemi podmínkami:
  - *reflexivita*: každý prvek je ekvivalentní sám sobě;
  - *symetrie*: jestliže je $a$ ekvivalentní s $b$, pak je $b$ ekvivalentní s $a$;
  - *transitivita*: jestliže je $a$ ekvivalentní s $b$ a $b$ je ekvivalentní s $c$, pak je $a$ ekvivalentní s $c$.

  Rozhodněte, zda relace
  #math.equation(numbering: none, block: true)[
    #text(
      raingreen,
    )[$R = {(a, a), (b, b), (d, d), (d, e), (e, d), (a, b), (a, c)}$]
  ]
  je ekvivalence na množině #text(crimson)[$A = {a, b, c, d, e}$]. Pokud ne,
  přidejte *co nejméně dvojic*, aby se z ní ekvivalence stala. *Vysvětlete*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  Popište (jako množinu dvojic, obrázkem, ...) ekvivalenci na množině
  #clr[$A = {1, 2, 3, 4, 5}$], která má následující *třídy ekvivalence*:
  #list(indent: 1em)[
    ${1, 3}$ a ${2, 4, 5}$,
  ][
    ${1, 4}$, ${2}$, ${3}$ a ${5}$.
  ]
  *Vysvětlete*.
]
#v(15%)
=== #clb[Bonusová úloha]
#block(width: 100%)[
  #points(10)
  Předpokládejme, že nějaká množina $A$ má právě $5$ prvků. Kolik různých
  *ekvivalencí* na množině $A$ existuje? *Vysvětlete*.
]
