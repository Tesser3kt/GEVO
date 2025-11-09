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

= Logic -- propositions and operators
#v(6pt)
#block(width: 100%)[
#points(25)
  For which truth values of the propositions $p,q,l,k$ is the proposition
  #align(center)[
    $(p and q) and (l and k)$
  ]
]
true? #text(crimson)[*Elaborate*] your process and be sure that you got 
#text(crimson)[*all*] the possible quadruplets.
#v(30%)

#block(width:100%)[
  === #text(airblue)[Bonus Problem]
  #points(10)
  Come up with the negation of the proposition from the previous exercise. In
  other words, simplify 
  #align(center)[
    $not ((p and q) and (l and k))$.
  ]
  *Hint*: try treating both parentheses as some propositions $x,y$ and negate the
  proposition between them. Then proceed with negation of $x$ and $y$. 
]
#pagebreak()

= Basic set operations

#block(width:100%)[
  #points(25)
  Given sets $A = {1,2,3,4,5}, B = {4,5}$ find #text(crimson)[*all*] the sets $C$ that satisfy
  #text(crimson)[*both*] of the conditions
  #align(center)[
    $C subset A$ 
    #h(1em)
    and
    #h(1em)
    $C inter B = emptyset$.
  ]
Don't forget that empty set ($emptyset$) is subset of any set.
]
#v(45%)

#block(width:100%)[
  == #text(airblue)[Bonus Problem]
  #points(10)
  Take the set $C$ from the previous question and define it using
  #text(crimson)[logical operators only]. This means converting the two
  conditions forced upon $C$ to their logic operator form. 

  The solution should be in the form $C = {x | p(x)}$ where $p(x)$ is some
  proposition using $x in A, x in B$ which defines $C$.
]

#pagebreak()

= Venn diagrams

We denote the *size* of a set $A$ as $|A|$. This means how many
elements are in the set. So for set $S = {1,2,3}$ it is true that $|S|=3$.
#enum(numbering:"a)")[
  #block(width:100%)[
    #points(15)
    The expression $|A| + |B| + |C|$ can be interpreted as #emph["counting all the
    elements from all the sets"]. In each of the sectors of the
    following Venn diagram write *how many times* are the elements from that section
    counted in the previous expression.

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
  #v(10pt)
][

  #block(width:100%)[
    #points(25)
    Given this Venn diagram which represents two sets (one color-coded in
    #text(airblue)[blue] the other in #text(crimson)[red]), express them in terms
    of $A,B,C$. Use #text(crimson)[*only*] basic set operations.
    #align(center)[
      #cetz.canvas({  
        import cetz.draw: *
        cetz-venn.venn3(name: "venn",
        ab-fill: airblue,
        ac-fill: airblue,
        bc-fill: airblue,
        abc-fill: crimson,)
        content("venn.a", [A])
        content("venn.b", [B])
        content("venn.c", [C])

      })
    ]
  ]
  #v(10pt)
][
  #block(width:100%)[
    #points(10)
    Express $|A union B|$ (size of an union of $A,B$) in terms of $|A|,|B|$
    using any set operation #text(crimson)[*except*] for union. You may use the
    following diagram to visualize your process.
    
    #align(center)[
      #cetz.canvas({
        import cetz.draw: *
        cetz-venn.venn2(name:"venn")
        content("venn.a", [A])
        content("venn.b", [B])
      })
    ]
  ]
]


#block(width: 100%)[
  #points(20)
  == #text(airblue)[Bonus Problem]
  Express $|A union B union C|$ in terms of $|A|,|B|,|C|$ and their
  intersections. Use the result from *a)* to count every part of the diagram
  just once together with part *b)* so you know how to count every part
  individually.
]

