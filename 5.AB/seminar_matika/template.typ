#import "@preview/icu-datetime:0.2.0": fmt
#import "@preview/hydra:0.6.2": hydra
#import "@preview/thmbox:0.3.0": *
#import "@preview/equate:0.3.2": equate
#import "@preview/headcount:0.1.0": *
#import "@preview/zap:0.4.0"
#import "@preview/cetz:0.4.2"
#import "@preview/ctheorems:1.1.3": *
#import "@preview/itemize:0.2.0" as el
#import "@preview/algo:0.3.6": algo, code, comment, d, i

// Colors
#let maindark = rgb("#243642")
#let maindef = rgb("#387478")
#let mainlight = rgb("#629584")
#let mainlighter = rgb("#E2F1E7")
#let red = rgb("#D94B5A")
#let green = rgb("#2EBDB6")
#let blue = rgb("#2CC4EF")
#let purple = rgb("#695BAA")

// Define theorem envs
#let definition = thmbox(
  "definition",
  "Definice",
  fill: blue.transparentize(90%),
  breakable: true,
  inset: 0.8em,
  padding: (top: 0em, bottom: 0em),
  radius: 0em,
)
#let proposition = thmbox(
  "proposition",
  "Tvrzení",
  fill: mainlight.transparentize(80%),
  breakable: true,
  inset: 0.8em,
  padding: (top: 0em, bottom: 0em),
  radius: 0em,
)
#let proof = thmproof("proof", "Důkaz")

// Coloring
#let clr(body) = {
  text(fill: red.darken(30%))[#body]
}
#let clb(body) = {
  text(fill: blue.darken(30%))[#body]
}
#let clg(body) = {
  text(fill: green.darken(30%))[#body]
}
#let clp(body) = {
  text(fill: purple.darken(30%))[#body]
}

// No strips for algorithm
#let no-strips-algo(body) = {
  set table(fill: none)
  body
}

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
    size: 11pt,
    lang: "cs",
    font: "TeX Gyre Schola",
  )
  show math.equation: set text(
    size: 11pt,
    font: "TeX Gyre Schola Math",
  )
  show link: set text(
    fill: maindef,
  )
  // Title page

  // Title
  set text(size: 20pt)
  set align(horizon + center)
  image(img, width: 80%)

  v(1em)
  text(font: "TeX Gyre Adventor")[#title]
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
  [#fmt(today, locale: "cs", length: "long")]

  v(1em)
  // Abstract
  set text(size: 11pt)
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
  set text(size: 11pt)
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
    font: "TeX Gyre Adventor",
  )

  // Headings settings
  show heading.where(level: 1): it => {
    pagebreak()
    block(
      below: 1em,
      text(size: 18pt, maindark)[#it],
    )
  }

  show heading.where(level: 2): it => {
    block(
      above: 1.5em,
      below: 1em,
      text(size: 15pt, maindef)[#it],
    )
  }

  show heading.where(level: 3): it => {
    block(
      above: 1.5em,
      below: 1em,
      text(size: 13pt, mainlight)[#it],
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

  // Enum-list
  show: el.default-list.with(
    indent: 8pt,
    line-indent: 27pt,
    enum-spacing: (above: 8pt, below: 8pt),
  )
  show: el.default-enum-list.with(
    indent: 8pt,
    line-indent: 27pt,
    enum-spacing: (above: 8pt, below: 8pt),
  )
  set enum(numbering: "(1).(a).(i)", full: false)

  doc
}
