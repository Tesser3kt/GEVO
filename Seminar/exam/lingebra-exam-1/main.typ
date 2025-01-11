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
    number: "First Written Exam",
    content: "Linear Systems, Linear Geometry & Vector Spaces",
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
      Multiplying an equation of a linear system by a non-zero number doesn't
      change its solution set.
    ], [*YES*#h(2em)*NO*],
    [
      A system of $n$ variables and $m$ equations *can* have a unique solution
      only if $n <= m$.
    ], [*YES*#h(2em)*NO*],
    [
      Every column of a linear system contains *exactly one* pivot.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      A linear system has infinitely many solutions if and only if so does the
      corresponding homogeneous system.
    ], [*YES*#h(2em)*NO*],
    [
      The angle between $bold(u)$ and $bold(v)$ is defined for *every* two vectors
      $bold(u), bold(v) in RR^n$, where $n >= 1$. 
    ], [*YES*#h(2em)*NO*],
    [
      For any $bold(u), bold(v) in RR^n$, where $n >= 1$, if $||bold(u)|| +
      ||bold(v)|| = ||bold(u) + bold(v)||$, then $bold(u)$ and $bold(v)$ are
      linearly dependent.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      The solution set of any linear system forms a vector space.
    ], [*YES*#h(2em)*NO*],
    [
      If $V$ is a vector space with zero vector $bold(0) in V$, then ${bold(0)}
      <= V$.
    ], [*YES*#h(2em)*NO*],
    [
      $span lr((
        mat(1, 0; 0, 1), mat(0, 1; 1, 0))) = lr({mat(a, b; b, a) | a, b in
        RR})$.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
    [
      Let $V$ be a vector space and $S,T subset.eq V$. If $span S <= span T$,
      then *necessarily* $S subset.eq T$.
    ], [*YES*#h(2em)*NO*],
    [
      If a set $S subset.eq V$, where $V$ is a vector space, is linearly
      independent, then it *necessarily* has number of elements less or equal to
      $dim V$.
    ], [*YES*#h(2em)*NO*],
    [
      If $B = (bold(b)_1, bold(b)_2, dots.h, bold(b)_n)$ is a basis of $V$ and
      $bold(v) = 2 dot.c bold(b)_3 - 7 dot.c bold(b)_5$, then $(bold(b)_1,
      bold(b)_2, bold(v), bold(b)_4, dots.h, bold(b)_n)$ is also a basis of $V$.
    ], [*YES*#h(2em)*NO*],
    table.hline(),
  )
]
#pagebreak()

#question[
  Solve the following problems. Include important steps of your calculations.
  Each problem is worth 2 points.

  #subquestion(points:2, points-position:right)[
    Write the solution set (in any form you wish) of the following linear
    system.
    $ -3x & + & 3y & + &  z & = & 1 \
        x &   &    & + & 2z & = & 2 \
        x & + &  y & + & 3z & = & 3 $
  ]
  #v(1fr)
  #subquestion(points:2, points-position:right)[
    Given the set $S = lr({ vec(1, 1, 3), vec(0, 1, 2), vec(1, 3, 7), vec(0, 2,
    4), vec(2, 2, 6) }) subset.eq RR^3$, find a *linearly independent* set $T
    subset.eq S$ with $span T = span S$.
  ]
  #v(1fr)
  #subquestion(points:2, points-position:right)[
    Prove that the quadruple $B = lr((
      mat(1, -1; 2, 3), mat(2, 0; 2, 0), mat(1, 1; 4, 1), mat(1, 2; -2, 2)
    ))$ is a basis of $RR^(2 times 2)$, the vector space of $2 times 2$ real
    matrices.
  ]
  #v(1fr)
]
#pagebreak()

#question[
  Prove the following statements. If you base your proof upon another result,
  refer to the latter as precisely as you can. Of course, you may not refer to
  the given statement directly, or to propositions whose proofs use the
  statement.

  #subquestion(points:2, points-position:right)[
    Prove that the linear system
    $ a x & + &  y & = & & a^2 \
       x & + & a y & = & & 1 $
    has a unique solution as long as $a in.not {-1, 1}$.
  ]
  #v(1fr)
  #subquestion(points:3, points-position:right)[
    The _generalised triangle inequality_ states that
    #align(center)[
      $||bold(v)_1 + bold(v)_2 + dots.h + bold(v)_k|| <= ||bold(v)_1|| +
      ||bold(v)_2|| + dots.h + ||bold(v)_k||$
    ]
    for all $bold(v)_1, bold(v)_2, dots.h, bold(v)_k in RR^n$ and $k,n >= 1$.
    Prove it by induction on the number of vectors, $k$.
  ]
  #v(1fr)
  #subquestion(points:4,points-position:right)[
    Let $V,W <= RR^n$. Prove that if $dim V + dim W > n$, then $dim (V sect W) >
    0$.
  ]
  #v(1fr)
]

