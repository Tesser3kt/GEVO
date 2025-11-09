// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let darkmagenta = rgb("#8B008B")
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
  Logic & Set Theory
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
= Logic -- propositions and operators
#v(6pt)
#block(width: 100%)[
  #points(25)
  Given the proposition
  #math.equation(numbering: none, block: true)[
    $(q and not p) <=>  p$,
  ]
  determine when it is true (for which truth values of $p$ and $q$) and when it
  is false. #text(crimson)[*Explain your answer.*]\
  *Hint:* You may use a truth table if you wish.
]
#v(30%)
#block(width: 100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Every logical proposition can be expressed using only the operators $not$,
  $and$ and $or$. Do this for the implication, that is, find a proposition which
  uses only the operators $not$, $and$ and $or$ and is equivalent to $p => q$.
  #text(crimson)[*Explain your answer*.]
]
#pagebreak()

// Second page
= Basic set operations
#v(12pt)
#block(width: 100%)[
  #points(35)
  #block(width: 100%)[
    Given sets #text(crimson)[$A = {b, c, e}$], #text(airblue)[$B = {a, c, d}$]
    and #text(raingreen)[$C = {a, b, c, d}$],
    determine the sets
    #math.equation(numbering: none, block: true)[
      $(#text(crimson)[$A$] without #text(airblue)[$B$]) union
      #text(raingreen)[$C$] #h(1em) "and" #h(1em) #text(crimson)[$A$] inter
      (#text(airblue)[$B$] inter #text(raingreen)[$C$])$.
    ]
    
    You *don't* have to provide any *explanation*.
  ]
]
#v(30%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonus Problem]
  #block(width: 100%)[
    For a set $A$, there exists a set that contains all the subsets of $A$ and
    it's denoted $2^A$. For example, if #text(crimson)[$A = {a, b}$], then
    #math.equation(numbering: none, block: true)[
      $2^(#text(crimson)[$A$]) = {{}, {a}, {b}, {a,b}}$.
    ]
    Try to explain *why* the set of all subsets is denoted $2^A$. How many
    elements does $2^A$ have if $A$ has $n$ elements? #text(crimson)[*Explain
    your reasoning.*]
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
          ab-fill: raingreen,
          bc-fill: raingreen,
        )
      })
    ]
  ]
  #v(10%)
][
  #block(width: 100%)[
    #points(20)
    Draw a Venn diagram for the following expression:
    #math.equation(numbering: none, block: true)[
      $(A inter C) without B$.
    ]
    You *don't* have to explain anything.
  ]
]
#v(20%)
#block(width: 100%)[
  #points(10)
  === #text(airblue)[Bonus Problem]
  Drawing a Venn diagram with four sets is quite hard and cannot be done using
  circles only. Indeed, consider the following picture for sets
  #text(crimson)[$A$], #text(airblue)[$B$], #text(raingreen)[$C$] and
  #text(darkmagenta)[$D$]:
  #align(center)[
    #cetz.canvas({
      import cetz.draw: *
      circle((0, 0), radius: 1cm, stroke: 1pt + crimson);
      circle((1cm, 0), radius: 1cm, stroke: 1pt + airblue);
      circle((0cm, -1cm), radius: 1cm, stroke: 1pt + raingreen);
      circle((1cm, -1cm), radius: 1cm, stroke: 1pt + darkmagenta);
    })
  ]
  Would you be able to find a combination of set operations on #text(crimson)[$A$],
  #text(airblue)[$B$], #text(raingreen)[$C$] and #text(darkmagenta)[$D$] which
  doesn't have a corresponding region in the diagram above? You *don't* have to 
  provide an *explanation*.
]
