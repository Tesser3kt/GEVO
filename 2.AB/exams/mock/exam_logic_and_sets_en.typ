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
  Logic & Set Theory
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
= Logic -- propositions and operators
#v(6pt)
#block(width: 100%)[
  #points(25)
  Supposing a proposition $p$ is false and another proposition $q$ is also
  false, is the proposition
  #align(center)[
    $(p => q) or q$
  ]
  true or false? #text(crimson)[*Elaborate*].
]
#v(30%)
#block(width: 100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Fill the propositions $p$ and $q$ (you may not need both) in the blanks so
  that the proposition
  #align(center)[
    $(not p => #blank()) <=> (#blank() or q)$
  ]
  is *always* true independently of whether $p$ and $q$ are themselves true or
  false. #text(crimson)[*Check that your answer is correct.*]
]
#pagebreak()

// Second page
= Basic set operations
#v(12pt)
#block(width: 100%)[
  #points(35)
  #block(width: 100%)[
    Given sets $A = {2, 3, 5}$, $B = {3, 4, 5}$ and $C = {1, 2, 3, 4}$,
    determine the sets
    #align(center)[
      $(A union B) inter C$ #h(1em) and #h(1em) $C without (A inter B)$.
    ]
    You *don't* have to provide any *explanation*.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonus Problem]
  #block(width: 100%)[
    There is a set operation called *symmetric difference* of $A$ and $B$ and
    written as $A triangle.stroked.t B$. It can be defined like this:
    #align(center)[
      $A triangle.stroked.t B = (A without B) union (B without A)$.
    ]
    Define this set using #text(crimson)[*logical operators only*]. That is,
    find a proposition $p(x)$ (consisting of the propositions $x in A$ and $x in
    B$) such that $A triangle.stroked.t B = {x | p(x)}$.
  ]
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
          b-fill: raingreen,
          c-fill: raingreen,
          bc-fill: raingreen,
          abc-fill: raingreen,
          ac-fill: raingreen,
        )
      })
    ]
  ]
  #v(20%)
][
  #block(width: 100%)[
    #points(20)
    Draw a Venn diagram for the following expression:
    #align(center)[
      $(A inter B) union (A without C)$.
    ]
    You *don't* have to explain anything.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonus Problem]
  Prove (using Venn diagrams, logic or anything else) that
  #align(center)[
    $(A inter C) without (A inter B) subset.eq C without B$
  ]
  for any three sets $A, B$ and $C$.
]
