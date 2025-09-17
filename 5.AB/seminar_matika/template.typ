#import "@preview/icu-datetime:0.1.2": fmt-date
#import "@preview/hydra:0.6.2": hydra
#import "@preview/thmbox:0.3.0": *
#import "@preview/equate:0.3.2": equate
#import "@preview/headcount:0.1.0": *
#import "@preview/zap:0.4.0"

// Colors
#let maindark = rgb("#243642")
#let maindef = rgb("#387478")
#let mainlight = rgb("#629584")
#let mainlighter = rgb("#E2F1E7")
#let blue = rgb("#2CC4EF")
#let green = rgb("#2EBDB6")
#let purple = rgb("#695BAA")

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
    font: "EB Garamond",
  )
  show math.equation: set text(
    size: 12pt,
    font: "Garamond-Math",
  )
  show link: set text(
    fill: green,
  )

  // Title page

  // Title
  set text(size: 20pt)
  set align(horizon + center)
  image(img, width: 80%)

  v(1em)
  text(font: "Prenton")[#title]
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

  set page(
    numbering: "1",
    header: context {
      // Query the document for all level-1 headings
      let chapter_headings = query(heading.where(level: 1))

      // Check if any of the chapter headings are on the current page
      let is_chapter_page = chapter_headings.any(it => (
        it.location().page() == here().page()
      ))

      // If it's not a chapter page, display the header
      if not is_chapter_page {
        if calc.odd(here().page()) {
          [#hydra(2) #h(1fr) #emph(hydra(1))]
        } else {
          [#emph(hydra(1)) #h(1fr) #hydra(2)]
        }
        v(-8pt)
        line(length: 100%)
      }
    },
  )
  set align(top + left)
  set text(size: 12pt)
  set par(justify: true)

  // Bold also colorises
  show strong: it => {
    text(
      fill: maindark,
      weight: "bold",
      it,
    )
  }

  // Headings format
  set heading(numbering: "I.1.1")
  show heading: set text(
    font: "Prenton",
  )

  // Headings settings
  show heading.where(level: 1): it => {
    pagebreak()
    block(
      below: 1em,
      text(maindark)[#it],
    )
  }

  show heading.where(level: 2): it => {
    block(
      above: 1.5em,
      below: 1em,
      text(maindef)[#it],
    )
  }

  show heading.where(level: 3): it => {
    block(
      above: 1.5em,
      below: 1em,
      text(mainlight)[#it],
    )
  }

  // Table settings
  set table(
    stroke: none,
    fill: (x, y) => {
      if (calc.rem(y, 2) == 1) {
        return mainlight.transparentize(90%)
      }
    },
  )

  // Equation numbering
  set math.equation(numbering: dependent-numbering("(1.1)"), supplement: [])

  // Thmbox
  show: thmbox-init()

  doc
}
