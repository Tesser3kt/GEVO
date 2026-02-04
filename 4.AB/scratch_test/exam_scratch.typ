// Define custom colors
#let crimson = rgb("#B80F0A")
#let airblue = rgb("#00308F")
#let raingreen = rgb("#00755E")
#let ashgray = rgb("#B2BEB5")

#show math.equation: set text(
  font: "TeX Gyre Schola Math",
  size: 12pt,
)
#show raw: set text(
  font: "TeX Gyre Cursor",
  size: 13pt,
)
#set par(
  justify: true,
)
#set text(
  font: "TeX Gyre Schola",
  size: 12pt,
)

= Test ze Scratche
#v(1em)

#enum[
  [1 bod] Přidejte do `Stage` podmínku, která způsobí konec hry, když proměnná
  `player hp` klesne na $0$.
  #align(center)[
    #image("figs/uloha1.png")
  ]
][
  [2 body] Zařiďte, aby při kliknutí na věž dostala tato upgrade tím, že se jí
  zvýší `range` a `fire rate`. Upgrade smí nastat jedině, když má hráč dostatek
  `gold`. Základní strukturu už máte připravenou. Nezapomeňte odečíst z `gold`
  cenu upgradu.
  #align(center)[
    #image("figs/uloha2.png")
  ]
]
#pagebreak()
#enum(start: 3)[
  [3 body] Zařiďte, aby (ve `Stage`) každých 100 jednotek herního času (proměnná
  `game time`) došlo ke zvýšení hodnot `enemy spawn rate`, `enemy speed` a
  `enemy hp`. *Pozor*, `enemy hp` musí být celé číslo. Zkuste hodnoty volit tak,
  aby hra byla hratelná.

  *Hint*: Operátor `mod` značí zbytek po dělení.
  #align(center)[
    #image("figs/uloha3.png")
  ]
][
  [1 bod] Přidejte do spritu `Enemy` podmínku, která způsobí, že mu klesne
  hodnota `hp` o $1$, kdykoli se dotkne spritu `Projectile`.
  #align(center)[
    #image("figs/uloha4.png")
  ]
]
