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
  strfmt("Strana {} of {}", cur, last)
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
      Mock test
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
  #text(size: 18pt)[1.C Matematika -- Mock test]
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
  Květoslav Sněhulák je člověk, kterého pravidelně *bolívají záda*, ale *hlava ho
  nikdy nebolí*. Bydlí v malém bytě *bez balkónu*. Květoslav Sněhulák jednoho
  dne pronesl:
  #rect(inset: 8pt, stroke: (left: 2pt + ashgray))[
    Když mě bolí hlava nebo záda, jdu se vydýchat doma na balkón.
  ]
  Mohl mluvit pravdu, nebo ne? *Vysvětlete*.\
  #text(
    size: 10pt,
  )[Pozn.: Tohle je _logická úloha_. Nesnažte se ji obejít přidáváním kontextu
    jako: "Třeba má ještě druhý domov, kde balkón má," apod.]
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Ze zadání víme, že Květoslava nikdy hlava nebolí, ale záda občas ano, tedy
  první věta může být pravdivá, ale i lživá. Naopak, druhá věta je vždycky lež,
  protože Květoslav nemá balkón, na který by se šel vydýchat.

  Celá věta může tedy být pravdivá jedině v případě, kdy Květoslava záda nebolí
  a na balkón nejde. Pravdu mluvit mohl.

  Celý problém můžeme taky formalisovat tak, že si větu přepíšeme jako
  #box[$(p or q) => r$], kde $p$ je výrok: "Bolí mě hlava," $q$ je výrok:
  "Bolí mě záda," a $r$ je výrok: "Jdu se vydýchat na balkón." Je-li $p$ vždy
  lež a $r$ je také vždy lež, celý výrok $(p or q) => r$ může být pravda jedině
  v případě, že $q$ je také lež, protože "lež $=>$ lež" je pravda.
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Doplňte výroky $p$ a $q$ (nemusíte nutně použít oba) do prázdných míst tak,
  aby výrok
  #align(center)[
    $(not p => #blank()) <=> (#blank() or q)$
  ]
  byl *vždy* pravdivý nezávisle na tom, zda jsou samy $p$ a $q$ pravdivé nebo
  lživé. *Ověřte, že je vaše odpověď správná.*
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Tohle lze řešit metodou pokus/omyl, žádná převratně chytrá myšlenka vedoucí k
  řešení přímo mě nenapadá. Rozmyslíme si, že $p or q$ je lež jenom v případě,
  že $p$ i $q$ jsou lži. Zároveň $not p => q$ je též lež jedině v případě, že
  $p$ lež (a tedy $not p$ pravda) a $q$ je lež. Čili, správné doplnění je toto:
  #math.equation(numbering: none, block: true)[
    $(not p => #text(crimson)[$q$]) <=> (#text(crimson)[$p$] or q)$.
  ]
  Správnost ověříme tabulkou.
  #align(center)[
    #table(
      columns: (auto,) * 6,
      align: horizon + center,
      inset: 8pt,
      fill: (x, y) => {
        if calc.odd(y) { airblue.transparentize(95%) }
      },
      stroke: (x, y) => {
        if y == 0 { (bottom: 1pt + gray) }
        if x < 5 { (right: 1pt + gray) }
      },
      table.header(
        [$p$],
        [$q$],
        [$not p$],
        [$not p => q$],
        [$p or q$],
        [$(not p => q) <=> (p
          or q)$],
      ),
      [$T$], [$T$], [$F$], [$T$], [$T$], [$T$],
      [$T$], [$F$], [$F$], [$T$], [$T$], [$T$],
      [$F$], [$T$], [$T$], [$T$], [$T$], [$T$],
      [$F$], [$F$], [$T$], [$F$], [$F$], [$T$],
    )

  ]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  #block(width: 100%)[
    Čtyři svědci -- Anna, Boris, Cyril a Daniela -- svědčili vzájemně u soudu a
    posléze tvrdí o svých výpovědích následující:
    - Anna: "Boris lže."
    - Boris: "Cyril a Dana buď oba mluví pravdu, nebo oba lžou."
    - Cyril: "Anna a Boris oba mluví pravdu."
    - Dana: "Pravdu říká buď Anna, nebo Cyril, ale ne oba."
  ]
  Kteří ze svědků mluví pravdu? *Vysvětlete*.
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Budeme postupovat rozborem případů. Označíme si písmeny $a, b, c, d$ výroky:
  "Anna / Boris / Cyril / Dana mluví pravdu."

  Začneme předpokladem, že všechny výroky $a, b, c, d$ jsou pravda. Tím okamžitě
  narazíme na problém, protože pravdivost $a$ znamená lživost $b$. Ať je tedy
  $b$ lež a $a$ stále pravda. Pak musí být rovněž $c$ lež, protože $b$ je lež.
  Výrok $d$ je tedy pravda, protože $a$ je pravda a $c$ je lež. Tato situace
  je v souladu s tím, že $b$ je lež, jelikož $c$ je pravda a $d$ je lež.

  Docházíme k sexistickému závěru, že Anna a Dana mluví pravdu, zatímco Boris a
  Cyril lžou.
]
#pagebreak()

#block(width: 100%)[
  #points(35)
  Přepište výrok $(p => q) or r$ použitím *pouze* negace $not$ a konjunkce
  $and$.
]
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Zde se hodí znát negace logických spojek. Budeme výrok přepisovat postupně.
  Pomocně si označíme výrok $p => q$ písmenem $x$. Přepíšeme nejprve výrok
  #box[$x or r$] pomocí $not$ a $and$. Víme, že $not (x or r)$ je $not x and not
  r$, takže $x or r$ je ekvivalentní #box[$not(not x and not r)$].

  Teď přepíšeme $p => q$ pomocí $not$ a $and$. Tady platí, že negace $p => q$ je
  $p and not q$, takže $p => q$ je ekvivalentní $not(p and not q)$. Stačí
  dosadit $not(p and not q)$ za $x$ do $not (not x and not r)$ (dvě negace
  vedle sebe se vyruší) a dostaneme, že výrok $(p => q) or r$ je ekvivalentní
  #math.equation(numbering: none, block: true)[
    $not(p and not q and not r)$.
  ]
]

#block(width: 100%)[
  #points(20)
  === #text(airblue)[Bonusová úloha]
  Označme písmenem $x$ výrok
  #math.equation(numbering: none, block: true)[
    $(a or b) and (b or c) and (c or d) and (d or a)$.
  ]
  Najděte výrok $y$, který je složen z výroků $a, b, c, d$ (ne nutně ze všech)
  pouze použitím $not$ a $or$ takový, že $x and y$ je *vždy lež*.\
  Předchozí věta znamená, že výrok $y$ může být třeba $not a or c or not d$ (to
  není správné řešení, jen příklad).
]

