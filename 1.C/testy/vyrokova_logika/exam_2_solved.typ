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
      Test B *s řešením*
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
  #text(size: 18pt)[1.C Matematika -- Test B *s řešením*]
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
#block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
  *Možné řešení*\
  Budeme místo celých jmen psát zkratky $X$, $Y$, $Z$, $W$ a $V$. Jistě nemohou
  všichni čtyři $X, Y, Z$ a $W$ mluvit pravdu, neboť $Z$ říká, že $X$ nebo $W$
  lžou, a $X$ přímo říká, že $W$ lže. Takže $V$ nemůže říci, že všichni ostatní
  mluví pravdu.

  Obecně je vidět, že $X$ i $W$ nemohou mluvit pravdu zároveň kvůli výroku $X$.
  Uvažme nejprve, že $X$, $Y$ a $Z$ mluví pravdu, $W$ lže a $V$ říká: "Tři lidé
  ze čtyř mají pravdu". Pak ale musí $V$ rovněž lhát kvůli výroku $Y$. Pokud $Y$
  mluví pravdu a $V$ taky, pak $Z$ lže. My jsme ale předpokládali, že $Z$ mluví
  pravdu, takže $V$ v tomto případě musí lhát.

  Druhá možnost je, že $Y, Z$ a $W$ mluví pravdu (protože $X$ musí lhát, když
  $W$ mluví pravdu). Pak ale opět $V$ musí lhát, třeba kvůli výroku $W$, který
  říká, že nemohou mít pravdu oba $Y$ a $V$.

  Celkově, $V$ nemůže říci, že tři ze čtyř lidí mají pravdu, aniž lže.
]
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
  #block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
    *Možné řešení*\
    Tahle úloha potřebuje k řešení trochu "náhodného" zkoušení, ale lze
    postupovat i téměř zcela systematicky.

    Představme si výrok ve tvaru $(p or x) => (q <=> y)$. Když za $x$ dáme něco,
    co je pravda v polovině případů -- třeba samotný výrok $r$ -- pak $p or r$
    bude pravda ve třech čtvrtinách případů, a tedy $(p or r) => (q <=> y)$
    bude taky pravda ve třech čtvrtinách případů (protože implikace je pravdivá
    ve třech ze čtyř případů). Za normálních okolností je ekvivalence $q <=> y$
    pravdivá v polovině případů, takže potřebujeme vymyslet výrok $y$ tak, aby
    byla pravdivá jenom v jednom případě ze čtyř. Jako první nás může napadnout
    $q <=> not q$, která není pravdivá nikdy. Stačí tedy $not q$ rozšířit
    spojkou, která je pravdivá jen v jednom případě: konjunkcí $and$. Tím
    dostáváme $q <=> (not q and r)$, která je pravdivá v jednom případě ze čtyř,
    čímž je celý výrok
    #math.equation(numbering: none, block: true)[
      $(p or r) => (q <=> (not q and r))$
    ]
    pravdivý ve třech případech z osmi.

    Ještě jednou: důvod pro toto je ten, že implikace $(p or r) => ?$ je
    pravdivá v šesti případech z osmi, když je výrok $?$ pravdivý přesně v
    polovině případů. Bude-li výrok $?$ pravdivý jen ve čtvrtině (polovině z
    poloviny) případů, pak bude i $(p or r) => ?$ pravdivý jen ve třech
    (polovině z šesti) případů.
  ]
]
#pagebreak()

#block(width: 100%)[
  #points(25)
  Napište výrok ekvivalentní výroku $p <=> q$ použitím jenom logických operátorů
  $not, and$ a $or$. Svůj *postup popište*.
  #block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
    *Možné řešení*\
    Tady šlo postupovat tabulkou (která má v tomto případě jen čtyři řádky)
    anebo si uvědomit, že $p <=> q$ je ekvivalentní $(p => q) and (q => p)$.

    Obecnou implikaci $x => y$ můžu napsat jako $not x or y$. K tomu se lze
    dostat třeba tak, že $not (x => y)$ je ekvivalentní $x and not y$, takže
    $not (x and not y)$ je ekvivalentní $x => y$. Výrok $not (x and not y)$ si
    můžu přepsat na $not x or y$.

    Takže, z $p => q$ se stane $not p or q$ a z $q => p$ se stane $not q or p$.
    Dohromady dostaneme, že $p <=> q$ je ekvivalentní
    #math.equation(numbering: none, block: true)[
      $(not p or q) and (not q or p)$.
    ]
  ]
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
  #block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
    *Možné řešení*\
    Na začátek je dobré si uvědomit, že jediná "speciální" komponenta je $B$,
    která je ve dvou závorkách. Zbytek komponent mezi sebou můžu ve výrazu
    libovolně proházet a nic nezměním.

    Kdybych tedy jako sabotér chtěl síť co nejrychleji vyhodit, začal bych
    komponentou $B$ právě pro to, že je na dvou místech. Když teď navíc vyhodím
    ještě $C$ nebo $D$, tak jsem vyhodil celou síť.

    Jenomže, opravář může komponentu $B$ opravit. Pak díky komponentám $A$ a $E$
    síť zase poběží. To ale znamená, že musím vyhodit $A$ i $E$. Konečně, když
    vyhodím třeba $C$, ale ne $D$, tak opravář může opravit $C$ a síť zase
    poběží. Tudíž musím vyhodit $C$ i $D$.

    Celkově, abych měl jistotu, že opravář síť nenahodí, musím nezbytně vyřadit
    všechny komponenty z provozu.
  ]
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
  nesmíte ptát třeba na pravdivost výroku $not p and (q or not q)$, který je
  ekvivalentní $not p$.
  #block(width: 100%, stroke: 1pt + ashgray, inset: 8pt)[
    *Možné řešení*\
    Stačí mi dvě otázky: začnu $p <=> q$. Když je $p <=> q$ pravda, tak $p$ a
    $q$ mají stejnou hodnotu, a když je lež, tak mají hodnotu opačnou.

    V prvním případě budu pokračovat otázkou $p or q$. Když je pravda, tak jsou
    $p$ i $q$ pravda, a když je lež, tak jsou $p$ i $q$ lži.

    V druhém případě se zeptám na pravdivost $p => q$. Když je $p => q$, tak je
    $p$ lež a $q$ pravda. Když je $p => q$ lež, tak je $p$ pravda a $q$ lež.
  ]
]

