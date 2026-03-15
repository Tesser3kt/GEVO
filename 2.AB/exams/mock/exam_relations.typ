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
  Relations \& Equivalence
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Mock Exam]
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
    Unless specified otherwise, you are to #text(crimson)[*always*] (at least
    briefly) explain your reasoning. Even in closed questions.
  ]
]
#v(12pt)

// First page
= Product of Sets \& Relations
#v(6pt)
#block(width: 100%)[
  #points(25)
  Let #text(crimson)[$A = {1, 2}$] and #text(airblue)[$B = {a, b, c}$]. Check
  all *correct* statements of the ones below. You *don't have to* explain
  yourself.
  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] ${(1, a), (1, b), (1, c)}$ is a relation from #text(crimson)[$A$]
    to~#text(airblue)[$B$].
  #v(6pt)
  - [ ] ${(a, b), (a, a), (c, a)}$ is a relation *on* #text(airblue)[$B$] (that
    is, a relation from #text(airblue)[$B$] to #text(airblue)[$B$]).
  #v(6pt)
  - [ ] There are *five* relations from #text(crimson)[$A$] to
    #text(airblue)[$B$].
  #v(6pt)
  - [ ] The element $(b, 2)$ lies in $#text(crimson)[$A$] times
    #text(airblue)[$B$]$.
  #v(6pt)
  - [ ] ${(a, 1), (a, 2)}$ is a relation from #text(airblue)[$B$] to
    #text(crimson)[$A$].
  #v(6pt)
]
#v(5%)
#block(width: 100%)[
  #points(25)
  A relation $#text(raingreen)[$R$]$ from #text(crimson)[$A = {1, 2}$] to #text(airblue)[$B = {a, b,
  c}$] is *anti-symmetric* if whenever #text(crimson)[$a$] is
  #text(raingreen)[related] to #text(airblue)[$b$], #text(airblue)[$b$] cannot
  be #text(raingreen)[related] to #text(crimson)[$a$] (for #text(crimson)[$a in
  A$] and #text(airblue)[$b in B$]). As an example, take the relation of "being
  a mother" on the set of people. If a woman is a child's mother, the child is
  of course not its mother's own mother.

  Give an example of an *anti-symmetric* relation from #text(crimson)[$A$] to
  #text(airblue)[$B$] with *at least three pairs*. *Explain*.
]
#pagebreak()

// Second page
= Equivalence
#v(12pt)
#block(width: 100%)[
  #points(25)
  Recall that the relation of _equivalence_ is given by three conditions:
  - *reflexivity*: every element is equivalent to itself;
  - *symmetry*: if $a$ is equivalent to $b$, then $b$ is equivalent to $a$;
  - *transitivity*: if $a$ is eq. to $b$ and $b$ is eq. to $c$, then $a$ is eq. to $c$.

  Determine if the relation
  #math.equation(numbering: none, block: true)[
    #text(raingreen)[$R = {(1, 1), (2, 2), (3, 3), (1, 3), (3, 1), (1, 2)}$]
  ]
  is an equivalence on the set #text(crimson)[$A = {1, 2, 3, 4}$]. If not, add
  *as few pairs as possible* to make it into an equivalence. *Explain*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  In the diagrams below, there are two different equivalences on the set
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

  For both equivalences, determine the *class of equivalence* of every element
  from the set #text(crimson)[$A$]. That is, if we label the equivalences
  #text(airblue)[$E_1$] and #text(raingreen)[$E_2$], determine
  #math.equation(numbering: none, block: true)[
    $[#text(crimson)[$1$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$2$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$3$]]_(#text(airblue)[$E_1$]),
    [#text(crimson)[$4$]]_(#text(airblue)[$E_1$])$  and 
    $[#text(crimson)[$1$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$2$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$3$]]_(#text(raingreen)[$E_2$]),
    [#text(crimson)[$4$]]_(#text(raingreen)[$E_2$])$.
  ]
  You *don't have to* explain yourself.
]
