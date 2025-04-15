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
  Each problem is worth 2 points.

  #subquestion(points:2, points-position:right)[
    Compute some basis of the row space of the matrix
    #align(center)[
     $mat(
       1, 1, 2;
       2, -2, 3;
       1, 3, 2
     )$
    ]
    and determine the matrix's rank.
  ]
  #v(1fr)
  #subquestion(points:2, points-position:right)[

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

