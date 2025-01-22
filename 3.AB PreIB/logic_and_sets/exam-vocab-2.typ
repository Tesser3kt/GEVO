#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: [
    _Set Theory and Logic Vocabulary Exam \#2_
    #h(1fr)
    3.AB PreIB Maths
    #v(-6pt)
    #line(length: 100%, stroke: .5pt)
  ]
)
#set text(
  font: "TeX Gyre Schola",
  size: 11pt
)
#show math.equation: set text(
  font: "TeX Gyre Schola Math",
  size: 11pt
)
#set par(
  justify: true,
  leading: 1em
)
#let mybox(width: 7em) = {
  box(width: width, height: 16pt, fill: rgb(220, 220, 220), baseline: 5pt)[]
}

#grid(
  columns: (3fr, 1fr),
  align: (left, center),
  column-gutter: 2em,
  [
    A statement that is either true or false is called a logical #mybox().
    Symbols such as $and$, $or$ or $<=>$ are called #mybox() and are used to
    combine two #mybox(). Given statements $p$ and $q$, the expression $p <=> q$
    is an #mybox() of $p$ and $q$ and is read '$p$ *if and only if* $q$'.

    In set theory, we write $a in A$ to express that $a$ is #mybox() of the set
    $A$. Taking all #mybox() that lie in the set $A$, the set $B$ or in both
    creates the set $A union B$, called the #mybox() of $A$ and $B$. It's
    important to realise that there are actually no duplicates in $A union B$
    because there is no notion of #mybox() in set theory. That is, there is no
    'repetition' in sets, either an object does lie inside a set, or it
    doesn't. Of course, both $A$ and $B$ also form a part of $A union B$, we
    write, e.g., $A subset.eq A union B$ and say that $A$ is a #mybox() of $A
    union B$. This last concept is crucial for the study of relations which are
    really just #mybox() of $A times B$. The last set is formed by all #mybox()
    $(a,b)$ with $a in A$ and $b in B$ and called the #mybox() of $A$ and $B$.
  ],
  [#upper[
    *subset*\
    #v(1em)
    *conjunction*\
    #v(1em)
    *equivalence*\
    #v(1em)
    *product*\
    #v(1em)
    *element*\
    #v(1em)
    *pair*\
    #v(1em)
    *union*\
    #v(1em)
    *proposition*\
    #v(1em)
    *frequency*\
    #v(1em)
  ]]
)
