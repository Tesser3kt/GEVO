#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: [
    _Set Theory and Logic Vocabulary Exam_
    #h(1fr)
    3.AB PreIB Maths
    #v(-6pt)
    #line(length: 100%)
  ]
)
#set text(
  font: "TeX Gyre Schola",
  size: 11pt
)
#set par(
  justify: true
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
    or $=>$. The last conjunction is called #mybox() and is typically read as
    'If ..., then ...' 

    The building blocks of modern mathematics are #mybox(). They are basically
    collections of things. The 'things' #mybox() are made of are called their
    #mybox(). 
  ],
  [#upper[
    *proposition*\
    #v(1em)
    *conjunction*\
    #v(1em)
    *implication*\
    #v(1em)
    *set*
  ]]
)
