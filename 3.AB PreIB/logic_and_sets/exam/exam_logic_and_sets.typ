#import "@preview/cheq:0.2.2": checklist

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let mintgreen = rgb("#98FB98")
#let ashgray = rgb("#B2BEB5")

// Set page and fonts
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Mock Exam
      #h(1fr)
      Page #current-page of 5
      #h(1fr)
      #datetime.today().display("[month repr:long] [day], [year]")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  },
  footer: [
    #line(length: 100%, stroke: .5pt + ashgray)
  ]
)
#show heading.where(
  level: 1
): it => block(width: 100%)[
  #set text(14pt)
  #it.body
]
#show math.equation: set text(
  font: "TeX Gyre Schola Math",
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
  #text(size: 18pt)[3.AB PreIB Maths -- Mock Exam]
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
  Supposing a proposition $p$ is false and another proposition $q$ is also
  false, is the proposition
  #align(center)[
    $(p => q) or q$
  ]
  true or false? *Explain*.
  #v(30%)
][
  #points(10)
  Fill the propositions $p$ and $q$ (you may not need both) in the blanks so
  that the proposition
  #align(center)[
    $(not p => #blank()) <=> (#blank() or q)$
  ]
  is *always* true independently of whether $p$ and $q$ are themselves true or
  false.
]
#pagebreak()

// Second page
= Basic set operations.
#v(12pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
    Given sets $A = {2, 3, 5}$, $B = {3, 4, 5}$ and $C = {1, 2, 3, 4}$,
    determine the set
    #align(center)[
      $(A union B) sect C$.
    ]
    You *don't* have to provide any *explanation*.
  ]
  #v(40%)
][
  #points(10)
  #block(width: 100%)[
    Show that
    #align(center)[
      $(A union B) union C = A union (B union C)$
    ]
    for any sets $A,B,C$. *Explain*.\
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
    Mark each of the following sets *if it's a relation* from $A$ to $B$, where
    #align(center)[
      $A = {1, 2} "and" B = {a, b, c}$.
    ]
    #v(12pt)
    #show: checklist.with(fill: white, stroke: black, radius: 0pt)
    - [ ] $R = {(1, a), (1, b), (2, c)}$
    - [ ] $R = {(a, 2), (b, 1)}$
    - [ ] $R = {(1, 2), (1, b), (2, 2)}$
    - [ ] $R = {(2, a), (2, b)}$
    - [ ] $R = {(a, b), (a, c)}$
    
    #v(40%)
  ]
][
  #points(10)
  #block(width: 100%)[

  ]
]

