#import "@preview/bananote:0.1.2": *
#import "@preview/pergamon:0.7.1": *
#import "@preview/ctheorems:1.1.3": *
#import "@preview/cetz:0.5.1"
#import "@preview/fletcher:0.5.8" as fletcher: diagram, edge, node
#import "@preview/diagraph:0.3.7": raw-render, render

// Theorems setup
#show: thmrules.with(qed-symbol: $square$)
#let definition = thmbox(
  "definition",
  "Definition",
  inset: (
    x: 1em,
    top: 1em,
    bottom: 1em,
  ),
  padding: (top: 0em, bottom: 0em),
  fill: color.oklch(80%, 30%, 270deg, 30%),
)
#let example = thmplain("example", "Example", inset: (x: 0em, top: 0em)).with(
  numbering: none,
)

// Figure setup
#show figure: set block(breakable: true)

// List setup
#set list(indent: 1em)

#set text(
  lang: "en",
)

#show: note.with(
  title: [Introduction to Graph Theory],
  authors: (([Adam Klepáč], []),),
)

= Basic stuff about graphs


#definition("Undirected graph")[
  An (undirected) _graph_ is a pair $G = (V, E)$ where
  #list[
    $V$ is the set of _vertices_;
  ][
    $E$ is the set of _edges_, i.e. sets ${v_1, v_2}$ where $v_1$ and $v_2$ are
    vertices.
  ]
]

#example[
  #ref(<graph-example-1>) shows a graph $G = (V, E)$ with
  #list[
    $V = {a, b, c, d, e, f, g}$,
  ][
    $E = {
      {a, b}, {a, c}, {b, c}, {c, d}, {c, e}, {c, h}, {e, f}, {e, g}, {e, h},
      {f, g}
    }$.
  ]
]

#figure(
  placement: none,
  raw-render(```
    graph {
      layout=sfdp
      beautify=true
      node [shape=circle, width=0.1, color=black, margin=0.05];

      a -- b;
      b -- c;
      a -- c;
      c -- d;
      c -- e;
      e -- f;
      f -- g;
      e -- g;
      e -- h;
      c -- h;
    }
  ```),
  caption: [Example of a random graph.],
) <graph-example-1>
