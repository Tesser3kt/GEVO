// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

#import emoji: banana, blueberries, cookie

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
      Exam B
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
  #text(size: 18pt)[2.AB PreIB Maths -- Exam B]
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
  Let #text(crimson)[$A = {#mycirc(), #myrect()}$] and #text(airblue)[$B =
  {banana, blueberries, cookie}$]. Check all *correct* statements of the ones
  below. You *don't have to* explain yourself.

  #show: checklist.with(fill: white, stroke: black, radius: 0pt)
  #v(6pt)
  - [ ] The set ${(cookie, cookie), (cookie, blueberries), (blueberries,
    banana)$ is a relation on #clb[$B$].
  #v(6pt)
  - [ ] The product $#clr[$A$] times #clb[$B$]$ has the *same number of
    elements* as $#clb[$B$] times #clr[$A$]$. 
  #v(6pt)
  - [ ] The set ${(banana, #mycirc()), (#mycirc(), cookie), (banana,
    #myrect())}$ is a relation from #clb[$B$] to #clr[$A$].
  #v(6pt)
  - [ ] The element $(#mycirc(), #myrect())$ lies in $#clr[$A$] times
    #clr[$A$]$.
  #v(6pt)
  - [ ] There are *more* relations on #clb[$B$] than there are relations from
    #clr[$A$] to #clb[$B$].
  #v(6pt)
]
#block(width: 100%)[
  #points(25)
  A relation #clg[$F$] from #clr[$A$] to #clb[$B$] (#clr[$A$] and #clb[$B$] are
  the same as above) is called a *function* if every element #clr[$a in A$] is
  #clg[related] to *exactly one* element #clb[$b in B$]. Below, you see pictures
  of two relations from #clr[$A$] to #clb[$B$]. Are they functions? If not,
  *why*?
  #grid(
    columns: (1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), mycirc(), anchor: "mid", name: "circ")
      content((0, 1), myrect(), anchor: "mid", name: "rect")

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
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), mycirc(), anchor: "mid", name: "circ")
      content((0, 1), myrect(), anchor: "mid", name: "rect")

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
    })],
  )
]
=== #clb[Bonus Problem]
#block(width: 100%)[
  #points(10)
  The *composition* of relations $R$ from $A$ to $B$ and $S$ from $B$ to $C$ is
  the relation written as $R compose S$ from $A$ to $C$ that is defined by
  #math.equation(numbering: none, block: true)[
    $a(R compose S)c$ in case that $a R b$ and $b S c$
  ]
  for any elements $a in A, b in B, c in C$. Draw the picture for the relation
  $R compose S$ if the pictures of $R$ and $S$ are as below.
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 1pt,
    align: center,
    [#cetz.canvas({
      import cetz.draw: *
      content((0, 0), mycirc(fill: black), anchor: "mid", name: "circ")
      content((0, 1), myrect(fill: black), anchor: "mid", name: "rect")

      content((2, 0), banana, anchor: "mid", name: "ban")
      content((2, 1), blueberries, anchor: "mid", name: "blu")
      content((2, 2), cookie, anchor: "mid", name: "coo")

      content((1, 3), [#clg[$R$]], anchor: "mid")

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
      line("rect", "coo", stroke: raingreen + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: raingreen,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), banana, anchor: "mid", name: "ban")
      content((0, 1), blueberries, anchor: "mid", name: "blu")
      content((0, 2), cookie, anchor: "mid", name: "coo")

      content((2, 0), [$1$], anchor: "mid", name: "1")
      content((2, 1), [$2$], anchor: "mid", name: "2")
      content((2, 2), [$3$], anchor: "mid", name: "3")

      content((1, 3), [#clb[$S$]], anchor: "mid")

      line("coo", "1", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
      line("coo", "2", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
      line("blu", "3", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
      line("ban", "3", stroke: airblue + 1pt, mark: (
        offset: .1,
        end: ">",
        fill: airblue,
      ))
    })],
    [#cetz.canvas({
      import cetz.draw: *

      content((0, 0), mycirc(fill: black), anchor: "mid", name: "circ")
      content((0, 1), myrect(fill: black), anchor: "mid", name: "rect")

      content((2, 0), [$1$], anchor: "mid", name: "1")
      content((2, 1), [$2$], anchor: "mid", name: "2")
      content((2, 2), [$3$], anchor: "mid", name: "3")

      content((1, 3), [Draw $R compose S$ here.], anchor: "mid", name: "eagle")
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
    )[$R = {(1, 1), (2, 2), (4, 4), (3, 4), (4, 2)}$]
  ]
  is an equivalence on the set #text(crimson)[$A = {1, 2, 3, 4}$]. If not, add
  *as few pairs as possible* to make it into an equivalence. *Explain*.
]
#v(15%)
#block(width: 100%)[
  #points(25)
  Describe (as a set of pairs, by a picture, ...) an equivalence on the set
  #clr[$A = {1, 2, 3, 4}$] which has the following *classes of equivalence*:
  #list(indent: 1em)[
    ${1}$, ${2}$ and ${3, 4}$
  ][
    ${1, 2, 4}$ and ${3}$.
  ]
  You *don't need to* explain anything.
]
#v(15%)
=== #clb[Bonus Problem]
#block(width: 100%)[
  #points(10)
  *Prove* that if $R compose R subset.eq R$, then the relation $R$ is
  *transitive*. See previous page for the definition of the composition of
  relations. The expression $R compose R subset.eq R$ literally says that every
  pair in the composition of $R$ with $R$ also lies in $R$.
]
