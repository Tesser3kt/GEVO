// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.3.1"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/cetz:0.3.2"
#import "@preview/cetz-venn:0.1.3"


// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")

// #let earthybrown = rgb("#000000")
// #let flowerpurple = rgb("#000000")
 #let flowerpurple = rgb("#7119a8")
 #let earthybrown = rgb("#b05705")
#let ashgray = rgb("#B2BEB5")

// Colored text definition
#let AA = {
  text(airblue)[$A$]
}
#let BB = {
  text(raingreen)[$B$]
}
#let RR = {
  text(crimson)[$R$]
}
#let CC = {
  text(earthybrown)[$C$]
}
#let SS = {
  text(flowerpurple)[$S$]
}


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
= Logic -- propositions and conjunctions.
#v(6pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width:100%)[
  Complete the truth table below.
  #align(center)[
   #table(
    align: center + horizon,
    columns: 3,
    table.header[$p$][$q$][$p and not q$],
    [1], [1], [#blank()],
    [1], [0], [#blank()],
    [0], [1], [0],
    [0], [0], [0]
      )
    ]
  ]
  In other words: evaluate the proposition $p and not q$ for the truth values of
  $p$ and $q$ corresponding to the first two lines of the truth table. You
  *don't* have to *explain anything*.
  #v(12pt)
][
  #points(10)
  Complete the blank square in proposition 
  #align(center)[
    $p #blank() not q$
  ]
  with some logical conjunction ($and, or, =>, <=>$) to make it _equivalent_ to
  $not (p => q)$. Two statements are _equivalent_ if their truth tables are the
  same. 

  For convenience, the truth table of implication is shown below.
  #align(center)[
    #table(
      columns: 3,
      align: center + horizon,
      table.header[$p$][$q$][$p => q$],
      [1], [1], [1],
      [1], [0], [0],
      [0], [1], [1],
      [0], [0], [1]
    )
  ]
  
  *Explain* your choice.

]
#pagebreak()

// Second page
= Basic set operations.
#v(12pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
  Given sets #text(airblue)[$A={c,c,c,b,b,a}$] and
  #text(raingreen)[$B={a,b,c}$], determine whether the statements

  #align(center)[
    $#text(airblue)[$A$] subset.eq #text(raingreen)[$B$]$ and
    $#text(raingreen)[$B$] subset.eq #text(airblue)[$A$]$.
  ]
  are true or false. *Explain* your method.

 // *Bonus* (+10%): if both the statements are true there is something to be concluded
 // about #text(airblue)[$A$] and  #text(raingreen)[$B$]. *Explain* what it is.
  ]
  #v(40%)
][
  #points(10)
  #block(width: 100%)[
    Write an expression (using set operations) for the shaded area in the
    diagram below.
    #align(center)[
    #cetz.canvas(
       length: 1.5cm,
       {
      cetz-venn.venn3(
        name: "venn",
        a-fill: gray,
        ab-fill: gray,
        ac-fill: gray,
        abc-fill: gray,
        bc-fill: gray,
        padding: 1em
  )
  import cetz.draw: * 
  content("venn.c", [#text(earthybrown)[$C$]])
  content("venn.b", [#BB])
  content("venn.a", [#AA])
})
      ]]
]
#pagebreak()

// Third page

= Cartesian product and relations.
#v(12pt)
#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
    Into the diagram below, draw the relation #RR (using *arrows*) from #AA to
    #BB if
    #align(center)[
      #text(airblue)[$A={1,3,5,7}$], #text(raingreen)[$B={0,2,4,6}$] and
      #text(crimson)[$R={(1,2),(3,6),(5,0)}$].
    ]
    #v(18pt)
    #align(center)[
    #cetz.canvas({
        import cetz.draw: *

        content((-.5, 1), text(airblue)[$1$], anchor: "mid")
        content((-.5, 2), text(airblue)[$3$], anchor: "mid")
        content((-.5, 3), text(airblue)[$5$], anchor: "mid")
        content((-.5, 4), text(airblue)[$7$], anchor: "mid")

        content((0, 0), AA, anchor: "mid")
        content((4, 0), BB, anchor: "mid")
          for y in range(1, 5) {
            circle((0, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }

        content((4.5, 1), text(raingreen)[$0$], anchor: "mid")
        content((4.5, 2), text(raingreen)[$2$], anchor: "mid")
        content((4.5, 3), text(raingreen)[$4$], anchor: "mid")
        content((4.5, 4), text(raingreen)[$6$], anchor: "mid")


          for y in range(1, 5) {
            circle((4, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }
      })
    ]
      ]
    #v(15%)
][
  #points(10)
  #block(width: 100%)[
    Draw again the relation #RR from the previous exercise together with the
    relation #text(flowerpurple)[$S={(0,a),(2,c),(4,d)}$] between
    sets #BB and #text(earthybrown)[$C={a,b,c,d}$].

#align(center)[
    #cetz.canvas({
        import cetz.draw: *

        content((-1, 1), text(airblue)[$1$], anchor: "mid")
        content((-1, 2), text(airblue)[$3$], anchor: "mid")
        content((-1, 3), text(airblue)[$5$], anchor: "mid")
        content((-1, 4), text(airblue)[$7$], anchor: "mid")

        content((0, 0), AA, anchor: "mid")
        content((3, 0), BB, anchor: "mid")
        content((6, 0), CC, anchor: "mid")
          for y in range(1, 5) {
            circle((0, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }

        content((3, 1.5), text(raingreen)[$0$], anchor: "mid")
        content((3, 2.5), text(raingreen)[$2$], anchor: "mid")
        content((3, 3.5), text(raingreen)[$4$], anchor: "mid")
        content((3, 4.5), text(raingreen)[$6$], anchor: "mid")


          for y in range(1, 5) {
            circle((3, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }
        content((7, 1), text(earthybrown)[$a$], anchor: "mid")
        content((7, 2), text(earthybrown)[$b$], anchor: "mid")
        content((7, 3), text(earthybrown)[$c$], anchor: "mid")
        content((7, 4), text(earthybrown)[$d$], anchor: "mid")


          for y in range(1, 5) {
            circle((6, y - 0.05), fill: black, stroke: 0pt, radius: 2pt)
          }
      })
      ]
      Now it is your task to compose the relations #RR and #SS into one relation
      $T$ that goes from #AA to #CC. This means that $T$ firstly applies #RR to
      get from #AA to #BB. Then, on all the results of #RR (end of every arrow
      from a)) applies #SS which gets it from #BB to #CC. At the end, $T$
      forgets the element from #BB and ends up only with the beginning and the
      ending of the journey. *Write down* the relation $T$.
      ]
]
#pagebreak()

// Fourth page
= Equivalence.
#v(12pt)

#enum(numbering: "a)")[
  #points(15)
  #block(width: 100%)[
    One of the examples of an equivalence is *'what flavor of ice cream'* each
    person likes the most.
    Verify that it is truly an equivalence. In other words: it has to satisfy 
    - *reflexivity*: every element is equivalent to itself;
    - *symmetry*: if $a$ is equivalent to $b$, then $b$ is equivalent to $a$;
    - *transitivity*: if $a$ is eq. to $b$ and $b$ is eq. to $c$, then $a$ is eq. to $c$.
  ]
    #v(35%)
][
  #points(10)
  #block(width: 100%)[
    Come up with at *least three* other equivalences on the set of all people.
    Try to estimate the number of equivalence classes they create. For the
    maximum credit there should be one that creates *over 100* partitions and
    also one that creates fewer than two.

    You *may not* use the equivalence from part a).
         ]
]
