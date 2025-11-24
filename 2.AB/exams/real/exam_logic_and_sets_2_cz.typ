// Import balíčků
#import "@preview/cheq:0.2.2": checklist
#import "@preview/cetz:0.4.2"
#import "@preview/cetz-venn:0.1.4"
#import "@preview/oxifmt:0.2.1": strfmt

// Definice vlastních barev
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

#set text(
  lang: "cs"
)
// Nastavení stránky a písem
#let page-counter(cur, last) = {
  strfmt("Strana {} z {}", cur, last)
}
#set page(
  paper: "a4",
  margin: (x: 1in, y: 1in),
  header: context {
    let current-page = counter(page).get().first()
    if current-page > 1 [
      Test B
      #h(1fr)
      #counter(page).display(
        page-counter,
        both: true,
      )
      #h(1fr)
      #datetime.today().display("[month repr:long] [day], [year]")
      #v(-8pt)
      #line(length: 100%, stroke: .5pt + ashgray)
    ]
  },
)
#show heading.where(
  level: 1,
): it => block(width: 100%)[
  #set text(14pt)
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

// Funkce pro body
#let points(number) = {
  place(
    top + right,
    dx: 1in - 18pt,
  )[#text(airblue)[[#number %]]]
}

// Prázdné políčko
#let blank(width: 12pt) = {
  box(
    fill: ashgray.transparentize(50%),
    width: width,
    height: 12pt,
    baseline: 3pt,
  )
}

// Titulek
#set text(
  font: "TeX Gyre Adventor",
  size: 24pt,
)
#align(center)[
  Logika a teorie množin
]
#v(-12pt)
#align(center)[
  #text(size: 18pt)[2.AB PreIB Maths -- Test B]
]
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

// Upozornění
#align(center)[
  #box(
    stroke: 1pt + ashgray,
    radius: 10%,
    width: 80%,
    inset: 12pt,
    fill: ashgray.transparentize(80%),
  )[
    Pokud není uvedeno jinak, #text(crimson)[*vždy*] (alespoň stručně)
    vysvětlete svůj myšlenkový pochod. I v uzavřených otázkách.
  ]
]
#v(12pt)

= Logika -- výroky a logické operátory
#v(6pt)
#block(width: 100%)[
  #points(25)
  Pro které pravdivostní hodnoty (pravda/lež) výroků $p,q,r,s$ je výrok
  #align(center)[
    $(p and q) and (r and s)$
  ]
]
pravdivý? #text(crimson)[*Podrobně vysvětlete*] svůj postup a ujistěte se, že jste získali
  #text(crimson)[*všechny*] možné čtveřice.
#v(30%)

#block(width: 100%)[
  === #text(airblue)[Bonusová úloha]
  #points(10)
  Určete negaci výroku z předchozí úlohy. Jinými
  slovy, zjednodušte
  #align(center)[
    $not ((p and q) and (r and s))$.
  ]
  *Nápověda*: Pamatujte, že $not (p and q) = not p or not q$. Nejprve negujte spojku $and$
  mezi oběma výroky v závorkách a potom znegujte i je samotné.
]
#pagebreak()

= Základní množinové operace

#block(width: 100%)[
  #points(35)
  Pro množiny $A = {1,2,3,4,5}$ a $B = {4,5}$ určete #text(crimson)[*všechny*]
  množiny $C$, které splňují #text(crimson)[*obě*] podmínky
  #align(center)[
    $C subset.eq A$
    #h(1em)
    a
    #h(1em)
    $C inter B = {}$.
  ]
  Nezapomeňte, že prázdná množina (${}$) je podmnožinou libovolné množiny.
]
#v(45%)

#block(width: 100%)[
  == #text(airblue)[Bonusová úloha]
  #points(10)
  Vezměte množinu $C$ z předchozí úlohy a definujte ji užitím
  #text(crimson)[pouze logických operátorů]. Tj. převeďte obě podmínky kladené
  na $C$ do jejich podoby zapsané logickými operátory.

  Řešení by mělo mít tvar $C = {x | p(x)}$, kde $p(x)$ je nějaký
  výrok obsahující $x in A$ a $x in B$.
]

#pagebreak()

= Vennovy diagramy

#enum(numbering: "a)")[
  #block(width: 100%)[
    #points(20)
    Určete množinu, kterou znázorňuje následující Vennův diagram. *Nemusíte*
    uvádět žádné *vysvětlení*.
    #align(center)[
      #cetz.canvas({
        cetz-venn.venn3(
          b-fill: raingreen,
          bc-fill: raingreen,
          c-fill: raingreen,
        )
      })
    ]
  ]
  #v(15%)
][
  #block(width: 100%)[
    #points(20)
    Nakreslete Vennův diagram pro výraz
    #math.equation(numbering: none, block: true)[
      $(A without B) inter (B union C)$.
    ]
    *Nemusíte* nic vysvětlovat.
  ]
]
#pagebreak()
#block(width: 100%)[
  #points(10)
  == #text(airblue)[Bonusová úloha]
  Velikost (*počet prvků*) množiny $A$ označujeme jako $|A|$. Například, pro
  množinu $S = {1,2,3}$ platí, že $|S|=3$. Výraz $|A| + |B| + |C|$ můžeme chápat
  jako #emph["počítání všech prvků ze všech množin"]. V každé z oblastí (je jich
  sedm) následujícího Vennova diagramu napište, *kolikrát* jsou prvky z dané
  oblasti započítány ve výrazu $|A| + |B| + |C|$. Například prvky z $A inter B$
  jsou započítány *dvakrát*, protože náleží zároveň do $A$ i do $B$.

  #align(center)[
    #cetz.canvas({
      import cetz.draw: *
      cetz-venn.venn3(name: "venn")
      content("venn.a", [A])
      content("venn.b", [B])
      content("venn.c", [C])
    })
  ]
]

