#set page(
  margin: 0pt,
  height: auto,
  width: auto,
)

#table(
  columns: (auto, auto),
  inset: 10pt,
  align: horizon,
  stroke: none,
  fill: (x, y) => {
    if calc.even(y) and y > 0 {
      gray.lighten(90%)
    }
    else if y == 0 {
      gray.lighten(60%)
    }
  },
  table.header(
    [*English*], [*Česky*]
  ),
  table.hline(),
  [proposition], [výrok],
  [true], [pravdivý],
  [false], [lživý],
  [operator], [operátor],
  [negation ($not$)], [negace],
  [implication ($=>$)], [implikace],
  [equivalence ($<=>$)], [ekvivalence],
  table.hline(stroke: gray + 1pt),
  [set], [množina],
  [element], [prvek],
  [intersection ($inter$)], [průnik],
  [union ($union$)], [sjednocení],
  [difference ($without$)], [rozdíl],
  [subset ($subset.eq$)], [podmnožina],
)
