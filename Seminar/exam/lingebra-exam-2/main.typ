#import "@preview/g-exam:0.4.2": *
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
)
#set text(
  font: "TeX Gyre Schola"
)
#set par(
  justify: true
)
#show math.equation: set text(
  font: "TeX Gyre Schola Math"
)
#set math.mat(align: right)

// Math operators
#let span = math.upright("span")
#let Hom = math.upright("Hom")

#show: exam.with(
  language: "en",
  school: (
    name: "Gymnázium Evolution",
    logo: read("./logo.png", encoding: none),
  ),
  exam-info: (
    academic-period: "Academic year 2024/2025",
    academic-level: "Maths Seminar, 6.AB/4.C",
    academic-subject: "Linear Algebra",
    number: "Second Written Exam",
    content: "Vector Spaces & Homomorphisms",
  ),
  
  show-student-data: (
    given-name: "first-page",
    family-name: false,
    group: false,
    date: false
  ),
  show-grade-table: true,
  clarifications: "Throughout the exam, you're allowed to use any tools at your disposal. Write your answers thoroughly.",
)

#question(points:4, points-position: right)[
  In each of the following groups, answer *YES* next to each statement if the
  statement is *always* true. Otherwise answer *NO*. Each group is worth 1
  point if all statements in that group are evaluated correctly.
  
  #set table(
    stroke: none,
    column-gutter: 2em,
    align: horizon,
    inset: (y: .75em),
  )
  #table(
    columns: 2,
    table.hline(),
    [
      Representation of a vector with respect to a linearly independent set is
      *always* unique.
    ], [*YES*#h(2em)*NO*],
    [
      Representation of a vector with respect to a spanning set is *always*
      unique.
    ], [*YES*#h(2em)*NO*],
    [
      Representation of a vector with respect to a basis is *always* unique.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      The maximum number of linearly independent columns of a matrix of rank $n$
      is $n$.
    ], [*YES*#h(2em)*NO*],
    [
      If a matrix $A in RR^(m times n)$ has rank $n$, then every linear system
      with left side $A$ has a *unique* solution.
    ], [*YES*#h(2em)*NO*],
    [
      If the row space of a matrix $A in RR^(m times n)$ has dimension $n$ and
      $m >= n$, then any linear system with left side $A$ has $m - n$ free
      variables.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      The matrix $mat(1, a; a, 1)$ can have rank $1$ or $2$ depending on the
      choice of $a$.
    ], [*YES*#h(2em)*NO*],
    [
      For every $A in RR^(m times n)$ and $bold(v) in RR^n$, the vector $A dot
      bold(v)$ lies in the row space of $A$.
    ], [*YES*#h(2em)*NO*],
    [
      If $A in RR^(3 times 3)$ has rank $2$, then $(A dot bold(e)_1, A dot
      bold(e)_2)$ is a basis of the column space of $A$.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      In $RR^2$, the reflection over any line is a homomorphism $RR^2 -> RR^2$.
    ], [*YES*#h(2em)*NO*],
    [
      If $f,g in Hom(RR^n,RR^m)$ and $f(bold(e)_i) = g(bold(e_i))$ for every $i
      <= n$, then $f = g$.
    ], [*YES*#h(2em)*NO*],
    [
      Given $f in Hom(V,W)$ and any subspace $U <= V$, the image $f(U)$ is a
      subspace of $W$.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
  )
]
#pagebreak()

#question[
  Solve the following problems. Include important steps of your calculations.

  #subquestion(points:2, points-position:right)[
    Compute some basis of the row space of the matrix
    #align(center)[
     $mat(
       1, 1, 2;
       2, -2, 3;
       1, 3, 2
     )$
    ]
    #h(8pt) in $RR^(3 times 3)$ and determine the matrix's rank.
  ]
  #v(1fr)
  #subquestion(points:2, points-position:right)[
    Verify (by definition or using any of the proven statements) that the map
    #box[$f: cal(P)_2 -> RR^2$] given by
    #align(center)[
     $f(a x^2 + b x + c) = vec(a + b, a + c)$
    ]
    #h(8pt) is a homomorphism.
  ]
  #v(1fr)
  #subquestion(points:3, points-position:right)[
    The homomorphism $f: (ZZ slash 7)^3 -> (ZZ slash 7)^3$ satisfies
    #align(center)[
     $f (vec(1, 0, 0)) = vec(1, 0, 2), #h(1em) f (vec(0, 1, 0)) = vec(2, 1,
     0), #h(1em) f (vec(0, 0, 1)) = vec(6, 6, 1).$
    ]
    #h(8pt) Determine $[f]^(cal(E)_3)_B$, that is, the matrix of $f$ with
    respect to the standard basis $cal(E)_3$ of $(ZZ slash 7)^3$ and the basis
    $B$, where
    #align(center)[
     $B = (vec(2, 1, 4), vec(1, 1, 1), vec(0, 0, 1))$.
    ]
  ]
  #v(1fr)
]
#pagebreak()

#question[
  Prove the following statements. If you base your proof upon another result,
  refer to the latter as precisely as you can. Of course, you may not refer to
  the given statement directly, or to propositions whose proofs use the
  statement.

  #subquestion(points:3, points-position:right)[
    Assume that $f$ is an endomorphism of $V$ (a vector space over $RR$) with
    basis $B = (bold(b)_1, bold(b)_2, ..., bold(b)_n)$. Prove the following:
    #list(indent: 16pt)[
      If $f(bold(b)_i) = bold(0)$ for every $i$, then $f(bold(v)) = bold(0)$ for
      every $bold(v) in V$.
    ][
      If $f(bold(b)_i) = bold(b)_i$ for every $i$, then $f(bold(v)) = bold(v)$
      for every $bold(v) in V$.
    ][
      If $f(bold(b)_i) = r dot bold(b)_i$ for some $r in RR$ and every $i$, then
      $f(bold(v)) = r dot bold(v)$ for every $bold(v) in V$.
    ]
  ]
  #v(1fr)
  #subquestion(points:3, points-position:right)[
    Show that the _transpose_ operation is linear, that is,
    #align(center)[
     $(r dot A + s dot B)^T = r dot A^T + s dot B^T$
    ]
    #h(7pt) for every $r,s in RR$ and $A,B in RR^(m times n)$.
  ]
  #v(1fr)
  #subquestion(points:4, points-position:right)[
    Assume that $f$ is an *injective* homomorphism $V -> W$. This implies that
    $f(B)$ is a basis of $f(V)$ for a given basis $B = (bold(b)_1, bold(b)_2,
    ..., bold(b)_n)$ of $V$.
    #list(indent: 16pt)[
      Determine $[f]_(f(B))^B$, the matrix of $f$ with respect to the bases $B$
      and $f(B)$.
    ][
      Given $bold(v) in V$ with
      #align(center)[
       $[bold(v)]_B = vec(r_1, r_2, dots.v, r_n)$,
      ]
      determine $[f(bold(v))]_(f(B))$, the representation of $f(bold(v))$ with
      respect to the basis $f(B)$.
    ]
  ]
  #v(1fr)
]

