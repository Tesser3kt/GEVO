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
  Logic & Set Theory
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

= Logic -- propositions and operators
#v(6pt)
#block(width: 100%)[
  #points(25)
  Is the proposition
  #align(center)[
    $(p => q) or not q$
  ]
]
a *tautology*? Meaning, is it #text(crimson)[*always true*] regardless of $p$
and $q$ being true or false? *Explain*.
#v(30%)

#block(width: 100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Consider a new logical operator $plus.o$ given by the following truth table:
  #align(center)[
    #table(
      columns: (auto, auto, auto),
      inset: 8pt,
      align: horizon,
      stroke: (x, y) => {
        if 0 <= y and y < 4 {
          (bottom: 1pt + ashgray)
        }
        if (0 <= x and x < 2) {
          (right: 1pt + ashgray)
        }
      },
      table.header([$p$], [$q$], [$p plus.o q$]),
      [$T$], [$T$], [$F$],
      [$T$], [$F$], [$T$],
      [$F$], [$T$], [$T$],
      [$F$], [$F$], [$F$],
    )
  ]
  Write the proposition $p plus.o q$ using only the standard logical operators
  $not$, $and$ and $or$.
]
#pagebreak()

= Basic set operations

#block(width: 100%)[
  #points(35)
  Given sets $A = {a, b, c, d, e}$, $B = {b, e}$ and $C = {a, d, f}$, use set
  operations  (whichever you wish) on $A$, $B$ and $C$ to create the sets
  #math.equation(numbering: none, block: true)[
    ${b, e, f}$ #h(1em) and #h(1em) ${a, d}$.
  ]
]
You *don't* have to *explain* your method.
#v(45%)

#block(width: 100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Consider the logical operator $plus.o$ from the previous bonus problem.
  Determine the set $A triangle C = {x | x in A plus.o x in C}$ where $A$ and
  $C$ are defined above. Give some *comments* on the method you used to obtain
  the set.
]

#pagebreak()

= Venn diagrams

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Given the Venn diagram below, determine the set which it represents. You
    *don't* have to provide an *explanation*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          a-fill: raingreen,
          b-fill: raingreen,
          ab-fill: raingreen,
          ac-fill: raingreen,
        )
      })
    ]
  ]
  #v(15%)
][
  #block(width: 100%)[
    #points(20)
    Draw a Venn diagram for the following expression:
    #math.equation(numbering: none, block: true)[
      $(A inter B inter C) union (B without C)$
    ]
    You *don't* have to *explain* anything.
  ]
]
#v(35%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonus Problem]
  The *complement* of a set $X$ inside a set $Y$ is defined as $Y without X$.
  Draw a Venn diagram of the *complement* of the set $(A without B) inter C$
  inside $A union B union C$.
]

