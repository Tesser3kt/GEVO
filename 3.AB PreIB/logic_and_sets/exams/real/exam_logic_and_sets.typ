// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.3.1"
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
      Exam A
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true
      )
      #h(1fr)
      #datetime.today().display("[month repr:long] [day], [year]")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  }
)
#show heading.where(
  level: 1
): it => block(width: 100%)[
  #set text(14pt)
  #it.body
]
#show math.equation: set text(
  font: "Tex Gyre Schola Math",
  size: 12pt
)
#show raw: set text(
  font: "TeX Gyre Cursor",
  size: 12pt
)
#set par(
  justify: true
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
    baseline: 3pt
  )
}

// Title
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt
)
#align(center)[
  Logic & Set Theory
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[3.AB PreIB Maths -- Exam A]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt
)

// Warning
#align(center)[
  #box(
    stroke: 1pt + ashgray,
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: ashgray.transparentize(80%)
  )[
    Unless specified otherwise, you are to #text(crimson)[*always*] (at least
    briefly) explain your reasoning. Even in closed questions.
  ]
]
#v(12pt)

// First page
= Logic -- propositions and conjunctions.
#v(6pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width:100%)[
  For each *truth value* (i.e. _true_ or _false_) of $p$ write down the *truth
  value* of the proposition
  #align(center)[
    $p or not p$.
  ]
]
  You *don't* have to show your method.
  #v(25%)
][
  #points(10)
  Decide whether the proposition
  #align(center)[
    $(p => q) or not (p => q)$
  ]
  is *always true* regardless of the truth values of $p$ and $q$. *Explain*.
]
#pagebreak()

// Second page
= Basic set operations.
#v(12pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
    Given sets $A = {\u{1F60E}, \u{1F369}, \u{1F608},\u{1FAA6}#h(-3pt)}, B =
    {\u{1F369}, \u{1FAA6}, \u{1F94C}#h(-3pt)} "and" C = emptyset $, determine
    the set
    #align(center)[
      $(A union B) sect C$.
    ]
    *Explain* your method.
  ]
  #v(40%)
][
  #points(10)
  #block(width: 100%)[
    Decide whether 
    #align(center)[
      $(A union B) sect C = A union (B sect C)$
    ]
    for any sets $A$, $B$, $C$. *Explain*.\
    *Hint*: Use Venn diagrams.
  ]
]
#pagebreak()

// Third page

= Cartesian product and relations.
#v(12pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
    You are given
    #align(center)[
      #text(airblue)[$A = {1, 2}$], #text(raingreen)[$B = {a, b, c}$] and
      #text(crimson)[$R = {(2, a), (2, b)}$],
    ]
    where #text(crimson)[$R$] is a relation from #text(airblue)[$A$] to
    #text(raingreen)[$B$]. Provide at least two other relations from
    #text(airblue)[$A$] to #text(raingreen)[$B$] that are different from the
    relation  #text(crimson)[$R$]. You *don't* have to *explain anything*.
  ]
  #v(40%)
][
  #points(10)
  #block(width: 100%)[
    How many relations are there from #text(crimson)[$A$] to #text(airblue)[$B$]
    if

    #align(center)[
      #text(crimson)[$A={5}$] and #text(airblue)[$B={ě,š,č,ř,ž}$]?
    ]
    *Hint:* It is *not* necessary to write all of them. A simple argument
    suffices.
  ]
]
#pagebreak()

// Fourth page
= Equivalence.
#v(12pt)

#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
  For each of the following relations decide if they are an equivalence on the
  set #text(airblue)[$A = {a,b,c}$] or not. You *don't* need to *explain
  anything*.
  #v(6pt)
  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  - [ ] $R = {(a, a), (b, b), (c, c)}$
  #v(6pt)
  - [ ] $R = {(a, b), (b, a), (a, a), (b, b), (c, c)}$
  #v(6pt)
  - [ ] $R = {(1, 2), (2, 3), (1, 3)}$
  #v(6pt)
  - [ ] $R = A times A$
  #v(6pt)
  - [ ] $R = {(a, a), (b, b), (c, c), (a,b), (b,c), (c,b), (b,a) }$
  #v(6pt)
  You may use the empty diagrams below to draw the relations from above.
  #align(center)[
    #cetz.canvas({
      import cetz.draw: *

      content((-1, 1), text(airblue)[$a$], anchor: "mid")
      content((-1, 2), text(airblue)[$b$], anchor: "mid")
      content((-1, 3), text(airblue)[$c$], anchor: "mid")

      content((0, 0), text(airblue)[$a$], anchor: "mid")
      content((1, 0), text(airblue)[$b$], anchor: "mid")
      content((2, 0), text(airblue)[$c$], anchor: "mid")
      for x in range(0, 3) {
        for y in range(1, 4) {
          circle((x, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
        }
      }
    
      content((5, 1), text(airblue)[$a$], anchor: "mid")
      content((5, 2), text(airblue)[$b$], anchor: "mid")
      content((5, 3), text(airblue)[$c$], anchor: "mid")

      content((6, 0), text(airblue)[$a$], anchor: "mid")
      content((7, 0), text(airblue)[$b$], anchor: "mid")
      content((8, 0), text(airblue)[$c$], anchor: "mid")
      for x in range(0, 3) {
        for y in range(1, 4) {
          circle((x +6, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
        }
      }

      content((10, 1), text(airblue)[$a$], anchor: "mid")
      content((10, 2), text(airblue)[$b$], anchor: "mid")
      content((10, 3), text(airblue)[$c$], anchor: "mid")

      content((11, 0), text(airblue)[$a$], anchor: "mid")
      content((12, 0), text(airblue)[$b$], anchor: "mid")
      content((13, 0), text(airblue)[$c$], anchor: "mid")
      for x in range(0, 3) {
        for y in range(1, 4) {
          circle((x + 11, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
        }
      }
    })
  ]
]
#v(12pt)
][
  #points(10)
  #block(width: 100%)[
    Recall that the relation of _equivalence_ is given by three conditions:
    - *reflexivity*: every element is equivalent to itself;
    - *symmetry*: if $a$ is equivalent to $b$, then $b$ is equivalent to $a$;
    - *transitivity*: if $a$ is eq. to $b$ and $b$ is eq. to $c$, then $a$ is eq. to $c$.

    To every point in the visualization of the equivalences from part a) assign
    one defining condition of equivalence that forces its presence in the
    equivalence.

    For example: _'This specific pair is present because otherwise the symmetry
    property would not be satisfied'_.
    
    *Hint:* Try assigning only the reflexivity and symmetry conditions. The
    geometrical representation of transitivity is harder to see. 
  ]
]
