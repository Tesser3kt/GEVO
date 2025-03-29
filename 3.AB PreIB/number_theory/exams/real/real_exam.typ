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
#let exp = text(crimson)[#sym.hat]
#let aa = text(crimson)[$a$]
#let aaa = text(crimson)[$a #sym.prime$]
#let cc = text(airblue)[$c$]
#let bb = text(crimson)[$b$]
#let bbb = text(crimson)[$b #sym.prime$]
#let dd = text(airblue)[$d$]
#let ee = text(raingreen)[$E$]

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
  Number Sets & GCD
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[3.AB PreIB Maths -- Exam A]
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
= Natural Numbers
#v(6pt)
#block(width:100%)[
  #enum(numbering: "a)")[
    #points(20)
    Thus far the addition and multiplication of natural numbers have been
    defined. Now the *exponentiation* is presented in two rules:
    #v(5pt)
    #align(center)[
      #table(
        columns: (auto, auto),
        align: left,
        fill: none,
        stroke: none,
        [1)], [$a^0 = 1$],
        [2)], [$a^(succ(b)) = a^b dot a$]
      )
    ]
    #v(5pt)
    Using *only these two rules* (and all your other knowledge about
    multiplication and addition), evaluate the following expressions.
    #v(5pt)
    #list(tight: false)[
        $3^4$
      ][
        $2^6$
      ]
      #v(15%)
    ][
    #points(10)
    *Generalise* your method from part a) to calculate $a^b$ for *any* $a,b in
    NN$.
  ]
]
#pagebreak()

// Second page
= Integers & Rationals
#v(5pt)
#block(width: 100%)[
  #enum(numbering: "a)")[
    #points(20)
    Connect all pairs belonging to the *same equivalence class* and write down
    the value of the *represented integer* for each class.
    #v(5pt)
  #align(center)[
    #grid(
      columns: 3,
      gutter: 60pt,
        [$(1,3)$],[$(2,3)$],[$(0,2)$],
        [$(9,6)$],[$(10,12)$],[$(122,123)$],
        [$(4,1)$],[$(7,4)$],[$(7,8)$]
      )
  ]
  #v(25pt)
  ][
    #points(10)
    You are given two pairs of natural numbers: $(aaa,bbb)$ and $(aa,bb)$ from
    the *same equivalence class* (they represent the same integer value). Show
    that their respective *sums* with some pair $(cc,dd)$ also belong to the
    *same equivalence class*.

    In other words, show that if $[(aa,bb)]_ee = [(aaa,bbb)]_ee$, then
    #align(center)[
      $[(aa,bb)]_ee + [(cc,dd)]_ee = [(aaa,bbb)]_ee + [(cc,dd)]_ee$
    ]
    *Hint:* The pairs $(aa,bb)$ and $(aaa,bbb)$ represent the same integer if
    (informally) '$aa - bb = aaa - bbb$'.
  ]
]
#pagebreak()

// Third page
= Divisibility & GCD
#v(12pt)
#enum(numbering: "a)")[
  #points(20)
  #block(width: 100%)[
    Find all numbers smaller than $100$ that have *exactly 3 divisors*. Do *not*
    proceed by trial and error (this method would result in #text(crimson)[0
    %]).
  ]
  #v(40%)
][
  #points(20)
  #block(width: 100%)[
    Compute $gcd(467569, 17279)$. Write down performed calculations *in full
    detail*.
  ]
]

