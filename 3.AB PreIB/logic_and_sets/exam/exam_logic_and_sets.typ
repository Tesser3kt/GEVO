// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.3.1"
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
  false. *Check that your answer is correct.*
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
    Mark each of the following sets *that is a relation* from $A$ to $B$, where
    #align(center)[
      $A = {1, 2} "and" B = {a, b, c}$.
    ]
    You *don't* need to *explain anything*.
    #v(12pt)
    #show: checklist.with(fill: white, stroke: black, radius: 0pt)
    - [ ] $R = {(1, a), (1, b), (2, c)}$
    #v(6pt)
    - [ ] $R = {(a, 2), (b, 1)}$
    #v(6pt)
    - [ ] $R = {(1, 2), (1, b), (2, 2)}$
    #v(6pt)
    - [ ] $R = {(2, a), (2, b)}$
    #v(6pt)
    - [ ] $R = {(a, b), (a, c)}$
    #v(12pt)
  ]
][
  #points(10)
  #block(width: 100%)[
    A relation $#text(raingreen)[R]$ is called a _function_ if every
    element #text(airblue)[$b in B$] is related to *at most one* element
    #text(crimson)[$a in A$]. That is, if
    $#text(crimson)[a]#text(raingreen)[R]#text(airblue)[b]$, then
    $#text(crimson)[a]$ is *not* related to any other element
    #text(airblue)[$hat(b) in B$].\
    Below, you see a picture of a relation $#text(raingreen)[R]$ from the set
    $#text(crimson)[A = {#circle(radius: 4pt, stroke: 1pt + crimson),
    #square(size: 7.5pt, stroke: 1pt + crimson), #polygon.regular(stroke: 1pt +
    crimson, size: 9.5pt, vertices: 3)}]$ to the set $#text(airblue)[B = {1, 2,
    3, 4}]$. Is #text(raingreen)[$R$] a _function_? *Why*?
    #v(12pt)
    #align(center)[
      #cetz.canvas({
        import cetz.draw: *
        circle((0, 0), stroke: 1pt + crimson, radius: 4pt)
        rect((-3.75pt + 1cm, -3.75pt), (3.75pt + 1cm, 3.75pt), stroke: 1pt +
        crimson)
        line((-3.75pt + 2cm, -3.75pt), (2cm, 3.75pt), (
        3.75pt + 2cm, -3.75pt), stroke: 1pt + crimson, close: true)
        content((-1, 1), text(airblue)[$1$], anchor: "mid")
        content((-1, 2), text(airblue)[$2$], anchor: "mid")
        content((-1, 3), text(airblue)[$3$], anchor: "mid")
        content((-1, 4), text(airblue)[$4$], anchor: "mid")

        for x in range(0, 3) {
          for y in range(1, 5) {
            circle((x, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }
        }
        circle((0, 1 - 0.05), stroke: 1.5pt + raingreen, radius: 5pt)
        circle((2, 1 - 0.05), stroke: 1.5pt + raingreen, radius: 5pt)
        circle((1, 3 - 0.05), stroke: 1.5pt + raingreen, radius: 5pt)
        circle((1, 4 - 0.05), stroke: 1.5pt + raingreen, radius: 5pt)
      })
    ]
  ]
]
#pagebreak()

// Fourth page
= Equivalence.
#v(12pt)

#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
  Is the relation
    #text(raingreen)[
      #math.equation(block: true)[
        $E = {(a, a), (b, b), (c, c), (c, d), (d, c), (b, d)}$
      ]
    ]
  ]
  an *equivalence* on the set $A = {a, b, c, d}$? If not, add as few pairs to it
  as necessary to make it into an equivalence. *Explain*.
  #v(40%)
][
  #points(10)
  #block(width: 100%)[
    *How many different* equivalences are there on the set $B = {1, 2, 3, 4, 5}$
    that partition it into *exactly* 3 distinct classes of equivalence?
    *Explain*.
  ]
]
