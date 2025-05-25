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
      Exam B
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
  #text(size: 18pt)[3.AB PreIB Maths -- Exam B]
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

    Connect together all the numbers which are equal modulo $p$.
    #v(30pt)
    #align(center)[
      #grid(
        columns: 3,
        gutter: 60pt,
        [$0$], [$1$], [$2p$], 
        [$p+2$], [$-1$], [2],
        [$8p+1$], [$10p$] , [$3p-1$]
      )
    ]


 ]
]
#v(30pt)
#enum(numbering: "a)", start: 2)[
    #block(width: 100%)[
    #points(35)
    After finishing a meal in a restaurant, the waitress brings your check. You
    realize that you can either pay with *eleven five-dollar bills* or with
    *twenty-eight four-dollar bills*, with the change in both scenarios being
    *smaller* then the *bill used for payment*.

    *Calculate the possible prices of the meal*.
        

  ]
]
#pagebreak()

// Second page
= Chinese Remainder Theorem
#v(6pt)
#block(width: 100%)[
  #points(40)
  Solve the following system of congruences.
  #align(center)[
   $x &eq.triple 1 pmod(5)\
    x &eq.triple 4 pmod(12)\
    x &eq.triple 2 pmod(7) $
  ]
  *Explain briefly* why there is only one solution smaller than $5 dot 12 dot 7$.
]

