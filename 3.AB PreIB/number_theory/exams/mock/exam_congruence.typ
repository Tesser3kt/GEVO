// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.3.1"
#import "@preview/oxifmt:0.2.1": strfmt

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Helpful shortcuts
#let rleq = text(crimson)[$<=$]
#let gcd = text(crimson)[#math.op("gcd")]
#let succ = text(raingreen)[#math.op("succ")]

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

// Congruence modulus
#let pmod(expr) = [
  #h(1em) (mod #expr)
]

// Title
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt
)
#align(center)[
  Congruences & CRT
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
= Congruences
#v(6pt)
#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(25)
    Does the congruence
    #align(center)[
    $3 dot x eq.triple 7 pmod(9)$
    ]
    have a solution? *Explain properly*.
  ]
]
#v(30%)
#enum(numbering: "a)", start: 2)[
    #block(width: 100%)[
    #points(25)
    A group of 13 pirates managed to steal a chest with golden coins. They tried
    to split the coins evenly into 13 piles but 10 coins remained. This provoked
    a fight and one of the pirates was stabbed dead. The 12 remaining pirates
    tried to split the coins evenly again but this time 3 coins remained. Yet
    another pirate died in the ensuing fight and the remaining 11 pirates
    finally managed to split the treasure evenly among themselves. At least how
    many coins did the chest contain?

    You only have to describe the *method* of solving this problem. You *don't
    need to* calculate the exact number.
  ]
]
#pagebreak()

// Second page
= Chinese Remainder Theorem
#v(6pt)
#block(width: 100%)[
  #points(50)
  Solve the following system of congruences.
  #align(center)[
   $x &eq.triple 3 pmod(9)\
    x &eq.triple 5 pmod(10)\
    x &eq.triple 2 pmod(11)$
  ]
  *Explain* why there is only one solution smaller than $9 dot 10 dot 11$.
]

