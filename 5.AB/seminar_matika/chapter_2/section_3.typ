#import "../template.typ": *

== Směr vektoru

Na rozdíl od velikosti vektoru, nelze směr vektoru určit absolutně. Důvod je
jednoduchý: když stojím před vámi a upažím pravou ruku, z vašeho pohledu ukazuji
_doleva_, zatímco ze svého _doprava_. Kam nějaká šipka vede můžeme určit pouze
relativně k jiným bodům či vektorům. Umíme vlastně říci jen, "jak moc vede druhá
šipka jinam než první".

Toto zjištění vede přirozeně na pojem _úhlu mezi vektory_. Podobně jako
velikost, i k definici úhlu mezi vektory nám pomůže visualisace. Začneme v
dimensích dvou. Spočítat úhel mezi dvěma šipkami můžeme pomocí cosinové věty.
Bez důkazu si ji připomeneme.

#theorem("Cosinová věta")[
  V trojúhelníku se stranami $a, b, c$ a úhly $alpha, beta, gamma$ platí rovnost
  #math.equation(numbering: none, block: true)[
    $c^2 = a^2 + b^2 - 2 a b cos gamma$.
  ]
  #align(center)[
    #cetz.canvas({
      import cetz.draw: *
      import cetz.angle: *

      line((0, 0), (1, 2), stroke: red + 1pt, name: "a")
      content(
        ("a.start", 60%, "a.end"),
        anchor: "north-west",
        padding: .1,
        clr[$a$],
      )
      line((0, 0), (-5, 1), stroke: blue + 1pt, name: "b")
      content(
        ("b.start", 50%, "b.end"),
        anchor: "north-east",
        padding: .1,
        clb[$b$],
      )
      line((1, 2), (-5, 1), stroke: purple + 1pt, name: "c")
      content(
        ("c.start", 50%, "c.end"),
        anchor: "south",
        padding: .2,
        clp[$c$],
      )

      angle(
        "a.start",
        "a.end",
        "b.end",
        label: clp[$gamma$],
        stroke: purple,
        radius: .7,
        label-radius: .4,
      )
      angle(
        "b.end",
        "b.start",
        "c.start",
        label: clr[$alpha$],
        stroke: red,
        radius: 2,
        label-radius: 1.5,
      )
      angle(
        "c.start",
        "c.end",
        "a.start",
        label: clb[$beta$],
        stroke: blue,
        radius: 1.2,
        label-radius: 0.8,
      )
    })
  ]
]<thm:cosinova-veta>

Uvažme nyní dva vektory #clr[$vc(u)$] a #clb[$vc(v)$]. Spojíme-li konce těchto
vektorů úsečkou, dostaneme trojúhelník jako na
#ref(<fig:uhel-mezi-vektory>, supplement: "obrázku").

#figure(
  cetz.canvas({
    import cetz.draw: *
    import cetz.angle: *

    line(
      (0, 0),
      (3, 2),
      mark: (end: ">", fill: red),
      stroke: red + 2pt,
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "north-west",
      padding: .1,
      clr[$vc(u)$],
    )

    line(
      (0, 0),
      (-1, 4),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "north-east",
      padding: .1,
      clb[$vc(v)$],
    )

    line((-1, 4), (3, 2), stroke: (dash: "dashed"))
    angle(
      "u.start",
      "u.end",
      "v.end",
      radius: 1,
      label: [$theta$],
      label-radius: 60%,
    )
  }),
  caption: [Úhel mezi vektory.],
)<fig:uhel-mezi-vektory>

Tečkovaná strana na #ref(<fig:uhel-mezi-vektory>, supplement: "obrázku") má
stejný směr a velikost jako vektor $#clb[$vc(v)$] - #clr[$vc(u)$]$ (akorát
posunutý na konec vektoru #clr[$vc(u)$]), protože $(#clb[$vc(v)$] -
  #clr[$vc(u)$]) + #clr[$vc(u)$] = #clb[$vc(v)$]$. Podle
#link(<thm:cosinova-veta>)[cosinové věty] platí
#math.equation(block: true)[
  $||vc(v) - vc(u)||^2 = ||vc(u)||^2 + ||vc(v)||^2 - 2 ||vc(u)|| ||vc(v)|| cos
  theta$.
]<eq:cosinova-veta-vektory>
Tuto rovnost upravíme do příjemnější podoby. Označíme si souřadnice vektorů
#clr[$vc(u)$] a #clb[$vc(v)$] jako $u_1, u_2$ a $v_1, v_2$. Máme
#math.equation(numbering: none, block: true)[
  $||vc(v) - vc(u)||^2 - ||vc(u)||^2 - ||vc(v)||^2 &= (v_1 - u_1)^2 + (v_2 -
    u_2)^2 - u_1^2 - u_2^2 - v_1^2 - v_2^2\
  &= v_1^2 - 2 u_1 v_1 + u_1^2 + v_2^2 - 2 u_2 v_2 + u_2^2 - u_1^2 - u_2^2 -
  v_1^2 - v_2^2\
  &= -2 u_1 v_1 - 2 u_2 v_2$.
]
Dosazením do rovnosti @eq:cosinova-veta-vektory pak vyjde
#math.equation(numbering: none, block: true)[
  $-2 u_1 v_1 - 2 u_2 v_2 &= -2 ||vc(u)|| ||vc(v)|| cos theta\
  u_1 v_1 + u_2 v_2 &= ||vc(u)|| ||vc(v)|| cos theta$.
]
Tím získáváme vyjádření úhlu mezi vektory ve 2D jako
#math.equation(numbering: none, block: true)[
  $cos theta = (u_1 v_1 + u_2 v_2)/(||vc(u)|| ||vc(v)||)$.
]

Co ale úhel mezi vektory v libovolné dimensi? Snad překvapivě, dokonale stejný
vzoreček funguje i tam. Totiž, jakékoli dva vektory leží na nějaké
dvoudimensionální rovině, jak jsme si rozmysleli v úvodu do této kapitoly. Úhel
mezi nimi pak definujeme právě na této rovině, kde si můžeme dokreslit i onen
pomocný trojúhelník. Pak můžeme použít #link(<thm:cosinova-veta>)[cosinovou
  větu] a dostat úplně stejnou rovnost jako @eq:cosinova-veta-vektory. Akorát, v
tomto případě mají vektory $#clr[$vc(u)$], #clb[$vc(v)$] in RR^n$ přesně $n$
souřadnic, takže výsledný vzoreček vypadá takto:
#math.equation(numbering: none, block: true)[
  $cos theta = (u_1 v_1 + u_2 v_2 + u_3 v_3 + ... + u_n v_n)/(||vc(u)|| ||vc(v)||)$.
]
