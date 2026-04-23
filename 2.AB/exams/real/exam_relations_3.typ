// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

#import emoji: bacon, banana, blueberries, cookie

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")
#let ambergold = rgb("#C58B00")
#let deepplum = rgb("#5A2A6E")
#let slateblue = rgb("#4C5D91")
#let softteal = rgb("#3E8E8A")
#let warmtaupe = rgb("#8A7F73")
#let ivorymist = rgb("#E8E3D9")

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
#let cla(body) = {
  text(ambergold)[#body]
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
      Exam C
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
  #text(size: 18pt)[2.AB PreIB Maths -- Exam C]
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
  Let #text(crimson)[$A = {banana, bacon}$] and #text(airblue)[$B =
  {banana, blueberries, cookie}$]. Check all *correct* statements of the ones
  below. You *don't have to* explain yourself.

  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] The set ${(cookie, bacon), (cookie, cookie), (blueberries,
        banana)}$ is a relation from #clb[$B$] to #clr[$A$].
  #v(6pt)
  - [ ] The set $(#clr[$A$] times #clb[$B$]) inter (#clb[$B$] times #clr[$A$])$
    is *empty*.
    #v(6pt)
  - [ ] There are *more* relations from #clb[$B$] to #clr[$A$] than there are
    relations from #clr[$A$] to #clb[$B$].
    #v(6pt)
  - [ ] The element $(bacon, bacon)$ lies in $#clr[$A$] times #clr[$A$]$.
  #v(6pt)
  - [ ] The set $#clb[$B$] times #clb[$B$]$ has 9 elements.
  #v(6pt)
]
#block(width: 100%)[
  #points(25)
  A relation #clg[$R$] from #clr[$A$] to #clb[$B$] is called *injective* if
  whenever $#clr[$a_1$]#clg[$R$]#clb[$b$]$ and $#clr[$a_2$]#clg[$R$]#clb[$b$]$,
  then $#clr[$a_1$] = #clr[$a_2$]$ for $#clr[$a_1$], #clr[$a_2$] in #clr[$A$]$
  and $#clb[$b$] in #clb[$B$]$. In words, no two *different* elements from
  #clr[$A$] can be related to the *same* element in #clb[$B$]. Determine if the
  two relations below are injective or not. *Briefly explain*.
  #grid(
    columns: (1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), banana, anchor: "mid", name: "circ")
      content((0, 1), bacon, anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      line("circ", "ban", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("circ", "blu", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("circ", "coo", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("rect", "blu", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), banana, anchor: "mid", name: "circ")
      content((0, 1), bacon, anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      line("rect", "ban", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("circ", "blu", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("rect", "coo", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
  )
]
=== #clb[Bonus Problem]
#block(width: 100%)[
  #points(10)
  The *union* of relations #clg[$R$] and #cla[$S$] from #clr[$A$] to #clb[$B$]
  is the relation written as $#clg[$R$] union #cla[$S$]$ from #clr[$A$] to
  #clb[$B$] that is defined by
  #math.equation(numbering: none, block: true)[
    $#clr[$a$] (#clg[$R$] union #cla[$S$]) #clb[$b$]$ in the case that
    $#clr[$a$]#clg[$R$]#clb[$b$]$ *or* $#clr[$a$]#cla[$S$]#clb[$b$]$.
  ]
  for any elements $#clr[$a$] in #clr[$A$], #clb[$b$] in #clb[$B$]$. Draw the
  picture for the relation $#clg[$R$] union #cla[$S$]$ if the pictures of
  #clg[$R$] and #cla[$S$] are as below.
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *
      content((0, 0), banana, anchor: "mid", name: "circ")
      content((0, 1), bacon, anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      content((1, 2.7), [#clg[$R$]], anchor: "mid")

      line("circ", "ban", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
      line("circ", "blu", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), banana, anchor: "mid", name: "circ")
      content((0, 1), bacon, anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      content((1, 2.7), [#cla[$S$]], anchor: "mid")

      line("rect", "blu", stroke: ambergold + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: ambergold,
      ))
      line("circ", "coo", stroke: ambergold + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: ambergold,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), banana, anchor: "mid", name: "circ")
      content((0, 1), bacon, anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      content(
        (1, 2.7),
        [Draw $#clg[$R$] union #cla[$S$]$ here.],
        anchor: "mid",
        name: "eagle",
      )
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
    )[$R = {(1, 1), (1, 2), (2, 2), (3, 2), (4, 4), (4, 1)}$]
  ]
  is an equivalence on the set #text(crimson)[$A = {1, 2, 3, 4, 5}$]. If not,
  add *as few pairs as possible* to make it into an equivalence. *Explain*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  Describe (as a set of pairs, by a picture, ...) an equivalence on the set
  #clr[$A = {1, 2, 3, 4, 5}$] which has the following *classes of equivalence*:
  #list(indent: 1em)[
    ${1, 2}$, ${3, 4}$ and ${5}$.
  ][
    ${1, 5}$ and ${2, 3, 4}$.
  ]
  You *don't need to* explain anything.
]
#v(15%)
=== #clb[Bonus Problem]
#block(width: 100%)[
  #points(10)
  Find a relation on the set #clr[$A = {1, 2, 3, 4, 5}$], which is
  #enum(numbering: "(a)", indent: 12pt)[
    symmetric and transitive but *not* reflexive.
  ][
    reflexive and transitive but *not* symmetric.
  ]
]
