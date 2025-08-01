#import "@preview/icu-datetime:0.1.2": fmt-date

#let template(
  img: none,
  title: none,
  authors: (),
  abstract: [],
  doc,
) = {
  // Global settings
  set page(
    paper: "a4",
    margin: 2cm,
  )
  set text(
    size: 12pt,
    lang: "cs",
  )
  show math.equation: set text(
    size: 12pt,
  )
  show link: set text(
    fill: blue,
  )

  // Title page
  //
  // Title
  set text(size: 20pt)
  set align(horizon + center)
  image(img, width: 80%)

  v(1em)
  [* #title *]
  v(1em)

  // Authors
  set text(size: 14pt)
  let count = authors.len()
  let ncols = calc.min(count, 3)

  grid(
    columns: (1fr,) * ncols,
    row-gutter: 24pt,
    ..authors.map(author => [
      #author.name \
      #author.affiliation \
      #link("mailto:" + author.email)
    ]),
  )

  v(1em)
  // Date
  let today = datetime.today()
  [#fmt-date(today, locale: "cs", length: "long")]

  v(1em)
  // Abstract
  set text(size: 12pt)
  set par(justify: true)
  [ #abstract ]

  doc
}
