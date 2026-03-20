// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

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
  #text(size: 18pt)[2.AB PreIB Maths -- Exam A]
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
  Let #text(crimson)[$A = {#mycirc(), #myrect()}$] and #text(airblue)[$B = {dog,
    flamingo, eagle}$]. Check all *correct* statements of the ones below. You
  *don't have to* explain yourself.

  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] ${(dog, #mycirc()), (dog, #myrect()), (flamingo, #mycirc())}$ is a
    relation from #clr[$A$] to #clb[$B$].
  #v(6pt)
  - [ ] The product $#clr[$A$] times #clb[$B$]$ has exactly *six* elements.
  #v(6pt)
  - [ ] The element $(flamingo, flamingo)$ lies in $#clb[$B$] times #clb[$B$]$.
  #v(6pt)
  - [ ] The sets $#clr[$A$] times #clb[$B$]$ and $#clb[$B$] times #clr[$A$]$
    share exactly *two* elements.
  #v(6pt)
  - [ ] ${(#mycirc(), #mycirc()), (#myrect(), #myrect())}$ is a relation on
    #clr[$A$].
  #v(6pt)
]
#v(5%)
#block(width: 100%)[
  #points(25)
  A relation #clg[$F$] from #clr[$A$] to #clb[$B$] (#clr[$A$] and #clb[$B$] are
  the same as above) is called a *function* if every element #clr[$a in A$] is
  #clg[related] to *exactly one* element #clb[$b in B$]. Below, you see pictures
  of two relations from #clr[$A$] to #clb[$B$]. Are they functions? *Why*?
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
    #text(
      raingreen,
    )[$R = {(a, a), (b, b), (d, d), (d, e), (e, d), (a, b), (a, c)}$]
  ]
  is an equivalence on the set #text(crimson)[$A = {a, b, c, d, e}$]. If not,
  add *as few pairs as possible* to make it into an equivalence. *Explain*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  Describe (as a set of pairs, by a picture, ...) an equivalence on the set
  #clr[$A = {1, 2, 3, 4, 5}$] which has the following *classes of equivalence*:
  #v(6pt)
  #list(indent: 1em)[
    ${1, 3}$ and ${2, 4, 5}$
  ][
    ${1, 4}$, ${2}$, ${3}$ and ${5}$.
  ]
  *Explain*.
]
