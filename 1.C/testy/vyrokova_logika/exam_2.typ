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
      Test B
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
  #text(size: 18pt)[1.C Matematika -- Test B]
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
  Xerxes, Yvetta, Zachariáš, Willy a Věnceslav vedou bouřlivou debatu o extrémně
  negativních vlivech domácích květin na psychické zdraví. Debata eskaluje do
  osobních útoků, někteří se spolčují a útočí na výroky ostatních.
  #list[
    Xerxes říká: "Já se Zachariášem máme pravdu a Willy mele nesmysly."
  ][
    Yvetta říká: "Když má Věnceslav pravdu, tak se Zachariáš určitě plete."
  ][
    Zachariáš říká: "Xerxes nebo Willy kecají."
  ][
    Willy říká: "Pravdu má buď Yvetta nebo Věnceslav, ale určitě ne oba."
  ]
  Věnceslav je ale mírumilovný a chce vyhovět co nejvíce lidem. Rád by řekl, že
  *všichni* čtyři ostatní mohou mít *pravdu*. Je to tak? Pokud ne, co aspoň *tři
  ze čtyř* ostatních? Pořádně *vysvětlete*.
]
#text(size: 10pt)[Zkuste k řešení nepoužívat pravdivostní tabulku (jsou to čtyři
výroky, takže šestnáct řádků).]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Na vynechaná místa ve výroku
  #math.equation(numbering: none, block: true)[
    $(p or #rect(fill: ashgray)[]) => (q <=> #rect(fill: ashgray)[])$
  ]
  doplňte *libovolné výroky*, které ale *obsahují* výrok $r$, tak, aby byl
  zadaný výrok pravdivý *přesně ve třech případech* (z osmi).\ Ještě jednou: na
  prázdná místa patří dva (klidně různé) výroky a každý z nich *může* obsahovat
  libovolné logické operátory ($not$, $and$, $or$, $=>$, $<=>$) a výroky $p,q$ a
  *musí* obsahovat výrok $r$.\
  #text(size: 10pt)[Tady se naopak pravdivostní tabulka může hodit.]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Napište výrok ekvivalentní výroku $p <=> q$ použitím jenom logických operátorů
  $not, and$ a $or$.
]
#pagebreak()

#block(width: 100%)[
  #points(35)
  Počítačová síť obsahuje pět komponent: $A, B, C, D, E$ (které mohou být
  vypnuté nebo zapnuté), a funguje přesně ve chvíli, když je výrok
  #math.equation(numbering: none, block: true)[
    $(A and B) or (C and D) or (B and E)$
  ]
  pravdivý (pod výrokem $A$ si představujeme "Komponenta $A$ je zapnutá."). Jste
  najatý sabotér, který chce *síť vyhodit* zničením *co nejméně komponent*.
  Opravář stihne včas *opravit maximálně jednu komponentu*.\
  Jaký je nejmenší počet komponent (a které to jsou), jež musíte jako sabotér
  zničit, aby *síť zůstala nefunkční i po opravě jedné komponenty opravářem*?
  *Proč*?
]
#v(1fr)
#block(width: 100%)[
  #points(20)
  === #text(airblue)[Bonusová úloha -- Vězni s klobouky]
  Každý z výroků $p,q$ může být nezávisle na druhém pravdivý nebo lživý. O
  každém výroku, který *obsahuje oba výroky $p$ i $q$* a *není ekvivalentní ani
  $p$, ani $q$ ani jejich negacím*, vám řeknu, zda je pravdivý, či ne. Kolik
  nejméně výroků (a jakých) mi musíte předložit, abyste zjistili, zda jsou $p$ a
  $q$ pravda či lež?\
  Že výrok není ekvivalentní ani $p$ ani $q$ ani jejich negacím, znamená, že se
  nemůžete ptát třeba na pravdivost výroku $not p and (q or not q)$, který je
  ekvivalentní $not p$.
]

