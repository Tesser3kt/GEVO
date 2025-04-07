
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
#let AA =  text(crimson)[A]
#let BB = text(crimson)[B]


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
  Number Sets & GCD
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
= Natural Numbers
#v(6pt)
#block(width:100%)[
  #enum(numbering: "a)")[
    #points(20)
    Remember that we defined *addition* and *multiplication* as:
    #align(center)[
      #grid(
        columns:2,
        gutter: 1cm,

        [$succ(n) &= n+1\ succ(n+m) &= n+succ(m)$],
        [$n dot 0 &= 0\ succ(n dot m) &= n dot m+m$]
      )
    ]
    Using *only* those axioms calculate:

    #v(5pt)
    #list(tight: false)[
      $2 dot 3$
    ][
      $1 + (2 dot 2)$
    ]
    #v(20%)
  ][
    #points(10)
    Assuming $x+y=y+x$, show that $x+succ(y)=succ(y)+x$. In your proof use only
    the *axioms* that *define addition*.
  ]
]
#pagebreak()

// Second page
= Integers & Rationals
#v(6pt)
#block(width: 100%)[
  #enum(numbering: "a)")[
    #points(20)
    Connect the pairs of *integers* that correspond to the *same equivalence
    class* and write down the value of the represented *rational number*.
    #v(6pt)
    #align(center)[
      #grid(
        columns: 3,
        gutter: 60pt,
        [$(2,20)$], [$(5,50)$], [$(35,7)$], 
        [$(-15,-3)$], [$(10,2)$], [$(-50,-2)$],
        [$(-2,2)$], [$(-4,4)$] , [$(100,4)$]
      )
    ]
    #v(10%)
  ][
    #points(10)
    Integers and rationals share some similarities in their definition. They are
    defined as *equivalence classes* on $NN times NN$ and $ZZ times ZZ$,
    respectively. Define *at least one* additional equivalence on $NN times NN$
    and one on $ZZ times ZZ$. Comment on the equivalence classes, *how many are
    there*? Do they have a specific shape?
    
    The two trivial equivalences are equality ($a$ is equivalent to $b$ if $a =
    b$) and the equivalence where all pairs of natural numbers (or integers)
    belong to the same equivalence class. *These won't count* as valid
    solutions.
  ]
]
#pagebreak()

// Third page
= Divisibility & GCD
#v(12pt)
#enum(numbering: "a)")[
  #points(20)
  #block(width: 100%)[
    Some *natural number* $n$ can be decomposed into primes as $n=p_1 dot p_2
    dot ... dot p_k$.
    *Describe a method* how to use the primes $p_1,p_2,...,p_k$ to find *all the
    divisors* of $n$.
  ]
  #v(40%)
  ][
  #points(20)
  #block(width: 100%)[
    Compute $gcd(1029, 1617 )$. Write down performed calculations *in full
    detail*.
  ]
]
