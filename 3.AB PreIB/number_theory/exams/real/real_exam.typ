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
#let exp = text(crimson)[#math.hat]
#let aa = text(crimson)[a]
#let aaa = text(crimson)[$a #sym.prime$]
#let cc = text(airblue)[c]
#let bb = text(crimson)[b]
#let bbb = text(crimson)[$b #sym.prime$]
#let dd = text(airblue)[d]
#let ee = text(raingreen)[E]

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
      Real Exam
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
  #text(size: 18pt)[3.AB PreIB Maths -- Real Exam]
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
  #points(15)
  So far the addition and multiplication of natural numbers were defined. Now
  the *exponentiation* is presented in two axioms :
  #v(5pt)
  #align(center)[
  #enum(numbering:"1)")[
    $a exp 0 = 1$
  ][
     $a exp succ(b) = a #exp b dot b$
  ]]
  #v(5pt)
  Using *only those two axioms* (and all your other knowledge about
  multiplication) evaluate the following expressions. You can denote
  exponentiation in the traditional form as $a^b$.
  #v(5pt)
  #list(tight:false)[
    $2 exp 5$
  ][
    $5 exp 3$
  ]

  #v(10%)
  ][
  #points(15)
  *Generalise* your method from part a) to calculate $a exp b$ for *any* $a,b in
  NN$.
  ]
]
#pagebreak()

// Second page
= Integers & Rationals
#v(6pt)
#block(width: 100%)[
  #enum(numbering: "a)")[
    #points(20)
    Connect the pairs that correspond to the *same equivalence classes* and write
    down the value of *represented integer*.
    #v(6pt)
#align(center)[
#grid(
  columns: 3,
  gutter: 60pt,
[$(2,3)$],[$(3,2)$],[$(5,3)$],[$(8,6)$],[$(9,10)$],[$(122,123)$],[$(2,0)$],[$(5,4)$],[$(7,8)$]
)]
    #v(25pt)

  ][
    #points(10)
    You are given two elements: $[(aaa,bbb)]_ee$ and $[(aa,bb)]_ee$ from the *same
    equivalence class* (they represent the same integer value). Show that their
    respective *sum* with some element $[(cc,dd)]_ee$ is always the *same*. In other
    words show that #align(center)[
      $[(aa,bb)]_ee + [(cc,dd)]_ee = [(aaa,bbb)]_ee + [(cc,dd)]_ee$
    ]
    *Hint:* Two elements are equivalent under $ee$ if they have
    the *same difference*.

  ]
]
#pagebreak()

// Third page
= Divisibility & GCD
#v(12pt)
#enum(numbering: "a)")[
  #points(20)
  #block(width: 100%)[
  Find a number that has *exactly 3 prime divisors* or show that such a number
  can not exist.
  ]
  #v(40%)
][
  #points(20)
  #block(width: 100%)[
    Compute $gcd(410, 240)$. Write down performed calculations *in full
    detail*.
  ]
]

