// Package imports
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt
#import "@preview/icu-datetime:0.2.2" as icu

// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

// Set page and fonts
#let page-counter(cur, last) = {
  strfmt("Strana {} ze {}", cur, last)
}

// Set list properties
#set list(indent: 12pt)

#set text(lang: "cs")
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    set text(size: 12pt, font: "TeX Gyre Schola")
    if current-page > 1 [
      Test A
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #icu.fmt(datetime.today(), locale: "cs", length: "long")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  },
)
#show heading.where(
  level: 1,
): it => block(width: 100%)[
  #set text(font: "TeX Gyre Adventor", 14pt)
  #it.body
]
#show math.equation: set text(
  font: "TeX Gyre Schola Math",
  size: 12pt,
)
#show raw: set text(
  font: "TeX Gyre Cursor",
  size: 12pt,
)
#set par(
  justify: true,
)

// Points function
#let points(number) = {
  place(
    top + right,
    dx: 1in - 18pt,
  )[#text(airblue)[[#number %]]]
}

// Blank box
#let blank(width: 12pt) = {
  box(
    fill: ashgray.transparentize(50%),
    width: width,
    height: 12pt,
    baseline: 3pt,
  )
}

// Title
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt,
)
#align(center)[
  Výroková logika
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[1.C Matematika -- Test A]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

// Warning
#align(center)[
  #box(
    stroke: 1pt + airblue.transparentize(60%),
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: airblue.transparentize(90%),
  )[
    Není-li uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně) objasněte
    svůj myšlenkový pochod. I v uzavřených otázkách.\
    Hodnotí se především systematický přístup k řešení.\
    Při řešení #text(airblue)[*smíte*] používat své poznámky i online materiály.
    Umělou inteligenci používat #text(crimson)[*nesmíte*].
  ]
]
#v(12pt)

#block(width: 100%)[
  #points(25)
  Najděte výrok #math.bold(text(airblue)[$x$]) složený *pouze* z výroků $p, q,
  r$ a operátorů $not, and, or$, takový, aby
  #math.equation(numbering: none, block: true)[
    $((p or not q) => r) <=> bold(#text(airblue)[$x$])$
  ]
  byl *vždy lživý* bez ohledu na pravdivostní hodnoty $p, q$ a $r$. Svůj postup
  *objasněte*.
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Zlá královna se ptá kouzelného zrcadla: "Zrcadlo, zrcadlo, pověz, kdo je na
  světě nejkrásnější." Jelikož pohádková zrcadla jsou, jak známo, dokonale
  zběhlá ve výrokové logice, odpoví zrcadlo:
  #rect(inset: 8pt, stroke: (left: 1pt + ashgray))[
    Vy, má paní, jste na světě nejkrásnější anebo je nejkrásnější také Sněhurka,
    pokud ovšem ještě žije.
  ]
  Kdy mluví kouzelné zrcadlo *pravdu*? *Vysvětlete.*\
  #text(size: 10pt)[Pozn.: Věta: "Pokud ..., tak ..." je vyjádřením implikace.]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Použitím *obou* výroků $p, q$ a libovolných logických operátorů najděte
  výrok, který je
  - pravdivý, když $p$ je lež a $q$ je lež;
  - lživý, když $p$ je lež a $q$ je pravda;
  - pravdivý, když $p$ je pravda a $q$ je lež;
  - lživý, když $p$ je pravda a $q$ je pravda.
  Svoji *odpověď ověřte*.
]
#pagebreak()

#block(width: 100%)[
  #points(35)
  Bezpečnostní zámek trezoru má čtyři přepínače, jejichž poloha (vypnutý /
  zapnutý) rozhoduje, kdy se zámek otevře. Navrhněte zámek tak, aby
  #list[
    existovala aspoň jedna konfigurace přepínačů, která zámek otevře;
  ][
    existovala aspoň jedna konfigurace přepínačů, která zámek nechá zamčený;
  ][
    jakmile se zámek otevře, *přepnutí jednoho libovolného přepínače* jej nemůže
    zavřít.
  ]

  Lze takový zámek opravdu navrhnout? *Vysvětlete*.
]
#v(1fr)
#block(width: 100%)[
  #points(20)
  === #text(airblue)[Bonusová úloha -- Vězni s klobouky]
  Každý ze čtyř zajatců má na sobě modrý nebo červený klobouk a vidí všechny
  klobouky kromě svého vlastního. Hrají hru, při které všichni *najednou*
  zvolají "červená", "modrá" nebo "nevím". Vyhrají, když
  #list[
    aspoň jeden vězeň určí správně svoji vlastní barvu;
  ][
    žádný vězeň neurčí svoji barvu špatně (odpověď "nevím" se nebere jako špatná
    ani správná).
  ]
  Existuje strategie, která funguje pro *některá* rozložení barev klobouků?\
  Existuje strategie, která funguje pro *všechna* rozložení barev klobouků?\
  Co když přidáme podmínku, že *sudý počet klobouků je červený*?
]

