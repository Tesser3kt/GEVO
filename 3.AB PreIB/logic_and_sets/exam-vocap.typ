#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: [
    _Set Theory and Logic Vocabulary Exam_
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
    In mathematical logic, a #mybox() is a sentence that is either _true_ of
    _false_. We can combine #mybox() using logical #mybox(), such as $and$, $or$
    or $=>$. The last one is called #mybox() and is typically read as 'If ...,
    then ...' 

    The building blocks of modern mathematics are #mybox(). They are basically
    collections of things. The 'things' #mybox() are made of are called their
    #mybox(). Given $A$ and $B$, the set that contains only the objects that $A$
    and $B$ have in common is denoted $A sect B$ and called their #mybox(). We
    can also create a set of all #mybox() $(a,b)$, basically ordered sets, with
    $a in A$ and $b in B$. Such a set is denoted $A times B$ and called the
    #mybox() of $A$ and $B$. Any subset of $A times B$ is then called a #mybox()
    from $A$ to $B$.
  ],
  [#upper[
    *set*\
    #v(1em)
    *implication*\
    #v(1em)
    *element*\
    #v(1em)
    *proposition*\
    #v(1em)
    *relation*
    #v(1em)
    *intersection*\
    #v(1em)
    *pair*\
    #v(1em)
    *product*\
    #v(1em)
    *conjunction*\
  ]]
)
