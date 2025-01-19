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
  }
)
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
#enum(numbering: "1.")[
  Logic -- propositions and conjunctions.
  #v(6pt)
  #enum(numbering: "a)", enum.item(1)[
    #points(10)
    Supposing a proposition $p$ is false and another proposition $q$ is also
    false, is the proposition
    #align(center)[
      $(p => q) or q$
    ]
    true or false? *Explain*.
    #v(30%)
  ],
  enum.item(2)[
    #points(10)
    Fill the propositions $p$ and $q$ (you may not need both) in the blanks so
    that the proposition
    #align(center)[
      $(not p => #blank()) <=> (#blank() or q)$
    ]
    is *always* true independently of whether $p$ and $q$ are themselves true or
    false.
  ]
)]
#pagebreak()
