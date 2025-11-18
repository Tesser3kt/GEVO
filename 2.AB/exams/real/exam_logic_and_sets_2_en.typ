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
  Logic & Set Theory
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

= Logic -- propositions and operators
#v(6pt)
#block(width: 100%)[
  #points(25)
  For which truth values of the propositions $p,q,r,s$ is the proposition
  #align(center)[
    $(p and q) and (r and s)$
  ]
]
true? #text(crimson)[*Elaborate*] your process and be sure that you got
#text(crimson)[*all*] the possible quadruplets.
#v(30%)

#block(width: 100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Determine the negation of the proposition from the previous exercise. In other
  words, simplify
  #align(center)[
    $not ((p and q) and (r and s))$.
  ]
  *Hint*: Remember that $not (p and q) = not p or not q$. First negate the $and$
  between the two propositions in parentheses and then negate them as well.
]
#pagebreak()

= Basic set operations

#block(width: 100%)[
  #points(35)
  Given sets $A = {1,2,3,4,5}$ and $B = {4,5}$, find #text(crimson)[*all*] the
  sets $C$ that satisfy #text(crimson)[*both*] of the conditions
  #align(center)[
    $C subset.eq A$
    #h(1em)
    and
    #h(1em)
    $C inter B = {}$.
  ]
  Don't forget that empty set (${}$) is a subset of any set.
]
#v(45%)

#block(width: 100%)[
  == #text(airblue)[Bonus Problem]
  #points(10)
  Take the set $C$ from the previous question and define it using
  #text(crimson)[logical operators only]. This means converting the two
  conditions forced upon $C$ to their logical operator form.

  The solution should be in the form $C = {x | p(x)}$ where $p(x)$ is some
  proposition using $x in A$ and $x in B$.
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
          bc-fill: raingreen,
          c-fill: raingreen,
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
      $(A without B) inter (B union C)$.
    ]
    You *don't* have to explain anything.
  ]
]
#pagebreak()
#block(width: 100%)[
  #points(10)
  == #text(airblue)[Bonus Problem]
  We denote the *size* (the number of elements) of a set $A$ as $|A|$. So, for
  a set $S = {1,2,3}$ it is true that $|S|=3$. The expression $|A| + |B| + |C|$
  can be interpreted as #emph["counting all the elements from all the sets"]. In
  each of the sectors of the following Venn diagram write *how many times* are
  the elements from that section counted in the expression $|A| + |B| + |C|$.
  For example, the elements from $A inter B$ are counted *twice* because they
  are both part of $A$ and of $B$.

  #align(center)[
    #cetz.canvas({
      import cetz.draw: *
      cetz-venn.venn3(name: "venn")
      content("venn.a", [A])
      content("venn.b", [B])
      content("venn.c", [C])
    })
  ]
]

