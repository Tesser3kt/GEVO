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
    } else if y == 0 {
      gray.lighten(60%)
    }
  },
  table.header([*English*], [*Česky*]),
  table.hline(),
  [Natural Numbers], [Přirozená čísla],
  [Integers], [Celá čísla],
  [Rational Numbers], [Racionální čísla],
  [fraction], [zlomek],
  [Real Numbers], [Reálná čísla],
  [addition], [sčítání],
  [sum], [součet],
  [subtraction], [odčítání],
  [difference], [rozdíl],
  [multiplication], [násobení],
  [product], [součin],
  [division], [dělení],
  [quotient], [podíl],
  [remainder], [zbytek],
  [exponentiation], [mocnění],
  [power], [mocnina],
  [base], [základ],
  [root], [odmocnina],
)
