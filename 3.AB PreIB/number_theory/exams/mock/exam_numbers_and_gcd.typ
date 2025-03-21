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
= Natural Numbers
#v(6pt)
#block(width:100%)[
  #points(30)
  We define the _ordering_ #text(crimson)[$<=$] on $NN$ by $n rleq m$ if $n
  subset.eq m$. Remember that natural numbers are just sets so we say that *a
  natural number $n$ is smaller than $m$ if it is a subset*.
  
  #enum(tight: false, numbering: "a)")[
    Show that $rleq$ is truly an _ordering_ on $NN$. This means that
    - it is *reflexive*: $n rleq n$ for every natural number $n in NN$;
    - it is *anti-symmetric*: if $n rleq m$ and also $m rleq n$, then
      necessarily $n = m$ for any two numbers $n,m in NN$.
  ][
    Show that if $n rleq m$, then also $succ(n) rleq succ(m)$.\
    *Hint*: use the formula for #text(raingreen)[successor].
  ][
    Remember that *addition* on $NN$ is defined using two rules:
    #enum(numbering: "(1)")[
      $n + 1 = succ(n)$
    ][
      $n + succ(m) = succ(n + m)$
    ]
    Part b) can be rewritten using rule (1) in the *definition of addition* as
    $n + 1 rleq m + 1$. Use this fact together with rule (2) of addition to
    prove that
    #align(center)[
      if $n rleq m$, then $n + 2 rleq m + 2$.
    ]
    *Hint*: Remember that $2 = succ(1)$ and make use of the result in part b).
  ]
]
#pagebreak()

// Second page
= Integers & Rationals
#v(6pt)
#block(width: 100%)[
  #enum(numbering: "a)")[
    #points(15)
    Check all pairs of natural numbers *that represent the integer* $-3$.
    #v(6pt)
    #show: checklist.with(fill: white, stroke: black, radius: 0pt)
    - [ ] $(1, 3)$
    #v(6pt)
    - [ ] $(-3, 0)$
    #v(6pt)
    - [ ] $(2, 5)$
    #v(6pt)
    - [ ] $(10 ,7)$
    #v(6pt)
    - [ ] $(5, 8)$
    You *don't have to explain* anything.
  ][
    #points(15)
    Assume that the pair $(a,b)$ represents a *positive* integer
    #text(airblue)[$y$], which is equal to $2 dot #text(raingreen)[$x$]$. Find a
    pair that represents $#text(raingreen)[$x$]$. Remember: the elements of the
    pair are *natural numbers*, you can't subtract or divide them. *Explain*.\
    *Hint*: The fact that $(a,b)$ represents $2 dot #text(raingreen)[$x$]$ can
    be informally expressed by the equation '$a - b = 2 dot
    #text(raingreen)[$x$]$'. Use this equation to express
    $#text(raingreen)[$x$]$ as a difference of two natural numbers.
  ]
]
#pagebreak()

// Third page
= Divisibility & GCD
#v(12pt)
#enum(numbering: "a)")[
  #points(20)
  #block(width: 100%)[
    Find a natural number *smaller than 40* with the *highest number of
    divisors*. Explain. Do *#text(crimson)[not]* proceed by trial and error
    (doing so will not yield any points).\
    *Hint*: What does the number of primes in a prime decomposition tell you
    about the number of divisors?
  ]
  #v(40%)
][
  #points(20)
  #block(width: 100%)[
    Compute $gcd(1968, 928)$. Write down performed calculations *in full
    detail*.
  ]
]

