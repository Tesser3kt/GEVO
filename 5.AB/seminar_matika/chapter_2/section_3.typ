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
#math.equation(block: true)[
  $cos theta = (u_1 v_1 + u_2 v_2)/(||vc(u)|| ||vc(v)||)$
]<eq:uhel-mezi-vektory-2d>

Co ale úhel mezi vektory v libovolné dimensi? Snad překvapivě, dokonale stejný
vzoreček funguje i tam. Totiž, jakékoli dva vektory leží na nějaké
dvoudimensionální rovině, jak jsme si rozmysleli v úvodu do této kapitoly. Úhel
mezi nimi pak definujeme právě na této rovině, kde si můžeme dokreslit i onen
pomocný trojúhelník. Pak můžeme použít #link(<thm:cosinova-veta>)[cosinovou
  větu] a dostat úplně stejnou rovnost jako @eq:cosinova-veta-vektory. Akorát, v
tomto případě mají vektory $#clr[$vc(u)$], #clb[$vc(v)$] in RR^n$ přesně $n$
souřadnic, takže výsledný vzoreček vypadá takto:
#math.equation(block: true)[
  $cos theta = (u_1 v_1 + u_2 v_2 + u_3 v_3 + ... + u_n v_n)/(||vc(u)|| ||vc(v)||)$.
]<eq:uhel-mezi-vektory>

Má to však malý háček. Jak je vám nejspíš známo, funkce $cos$ nabývá hodnot
pouze z intervalu $[-1, 1]$. Aby byl úhel mezi vektory správně definován, musíme
si být naprosto jisti, že pravá strana ve vzorci @eq:uhel-mezi-vektory je vždy
mezí $-1$ a $1$. K tomu si pomůžeme dvěma tvrzeními. První z~nich formalisuje
naši geometrickou intuici, že jakákoli dvojice vektorů vždy určuje trojúhelník
v~rovině. Totiž, mám-li tři úsečky délek $a$, $b$ a $c$, pak tyto mohou tvořit
trojúhelník jedině v~případě, že součet libovolných dvou je větší, než ta třetí,
např. $a + b > c$. Ověříme, že toto platí, když oněmi úsečkami jsou právě
vektory v prostoru.

Ještě předtím si však zavedeme jednu zajímavou operaci na vektorech, která pro
nás zatím bude jen pohodlným značením. Povíme si pár jejích vlastností a časem
se dostaneme i ke geometrické interpretaci.

#definition("Skalární součin")[
  Pro libovolné dva vektory $vc(u), vc(v) in RR^n$ definujeme
  #math.equation(numbering: none, block: true)[
    $vc(u) dot vc(v) = u_1 v_1 + u_2 v_2 + ... + u_n v_n$,
  ]
  kde $u_i$, resp. $v_i$, jsou souřadnice vektoru $vc(u)$, resp. $vc(v)$.
]

Jistě vidíte souvislost s právě odvozeným vzorečkem @eq:uhel-mezi-vektory.
Pomocí skalárního součinu jej můžeme vyjádřit snadněji jako
#math.equation(numbering: none, block: true)[
  $cos theta = (vc(u) dot vc(v))/(||vc(u)|| ||vc(v)||)$.
]

Skalární součin má pár základních vlastností, které nyní shrneme a důkaz necháme
jako úlohu na závěr.

#lemma("Vlastnosti skalárního součinu")[
  Ať $vc(u), vc(v), vc(w) in RR^n$ jsou tři vektory.
  #enum[
    Skalární součin je _asociativní_, tj. $(vc(u) dot vc(v)) dot vc(w) = vc(u) dot
    (vc(v) dot vc(w))$.
  ][
    Skalární součin je _komutativní_, tj. $vc(u) dot vc(v) = vc(v) dot vc(u)$.
  ][
    Skalární součin je distributivní, tj. $vc(u) dot (vc(v) + vc(w)) = vc(u) dot
    vc(v) + vc(u) dot vc(w)$.
  ][
    Normu vektoru lze zapsat pomocí skalárního součinu jako $||vc(u)||^2 = vc(u)
    dot vc(u)$.
  ]
]<lem:vlastnosti-skalarniho-soucinu>
#proof[
  Ponechán jako úloha.
]

#proposition("Trojúhelníková nerovnost")[
  Pro libovolné dva vektory $vc(u), vc(v) in RR^n$ platí nerovnost
  #math.equation(block: true)[
    $||vc(u) + vc(v)|| <= ||vc(u)|| + ||vc(v)||$,
  ]<eq:trojuhelnikova-nerovnost>
  přičemž rovnost nastává jedině v případě, že $vc(u)$ je násobek $vc(v)$, čili
  $vc(u) = c dot vc(v)$ pro nějaké $c in RR$. To znamená, že leží $vc(u)$ i
  $vc(v)$ leží na jedné přímce.

  Důvod přízviska "trojúhelníková" vysvětluje
  #ref(<fig:trojuhelnikova-nerovnost>, supplement: "obrázek").
]<thm:trojuhelnikova-nerovnost>

#figure(
  cetz.canvas({
    import cetz.draw: *
    import cetz.angle: *

    line(
      (0, 0),
      (3, -1),
      mark: (end: ">", fill: red),
      stroke: red + 2pt,
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "north-east",
      padding: .1,
      clr[$vc(u)$],
    )

    line(
      (3, -1),
      (6, 1),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "north-west",
      padding: .1,
      clb[$vc(v)$],
    )

    line(
      (0, 0),
      (6, 1),
      mark: (end: ">", fill: purple),
      stroke: purple + 2pt,
      name: "w",
    )
    content(
      ("w.start", 60%, "w.end"),
      anchor: "south-east",
      padding: .1,
      clp[$vc(u) + vc(v)$],
    )
  }),
  caption: [Trojúhelníková nerovnost],
)<fig:trojuhelnikova-nerovnost>

#proof(ref(<thm:trojuhelnikova-nerovnost>, supplement: "tvrzení"))[
  Protože jsou obě strany rovnosti kladná čísla, můžeme je umocnit na druhou a
  dokazovat, že
  #math.equation(numbering: none, block: true)[
    $||vc(u) + vc(v)||^2 <= (||vc(u)|| + ||vc(v)||)^2$.
  ]
  Díky #link(<lem:vlastnosti-skalarniho-soucinu>)[vlastnostem skalárního
    součinu] můžeme tuto nerovnost přepsat jako
  #math.equation(numbering: none, block: true)[
    $(vc(u) + vc(v)) dot (vc(u) + vc(v)) &<= ||vc(u)||^2 + 2 ||vc(u)|| ||vc(v)||
    + ||vc(v)||^2\
    vc(u) dot vc(u) + vc(u) dot vc(v) + vc(v) dot vc(u) + vc(v) dot vc(v) &<=
    vc(u) dot vc(u) + 2 ||vc(u)|| ||vc(v)|| + vc(v) dot vc(v)$.
  ]
  Po zkrácení $vc(u) dot vc(u)$ a $vc(v) dot vc(v)$ a použití rovnosti $vc(u)
  dot vc(v) = vc(v) dot vc(u)$ nám zůstane
  #math.equation(numbering: none, block: true)[
    $2 (vc(u) dot vc(v)) <= 2 ||vc(u)|| ||vc(v)||$.
  ]
  Vynásobíme obě strany nerovnosti kladnými čísly $||vc(u)||$ a $||vc(v)||$ a
  mírně upravíme, abychom dostali
  #math.equation(numbering: none, block: true)[
    $2(||vc(v)|| vc(u)) dot (||vc(u)|| vc(v)||) <= 2 ||vc(u)||^2 ||vc(v)||^2$.
  ]
  Přesuneme vše na jednu stranu a dále upravíme
  #math.equation(numbering: none, block: true)[
    $0 &<= ||vc(u)||^2 ||vc(v)||^2 - 2 (||vc(v)|| vc(u)) dot (||vc(u)|| vc(v)) +
    ||vc(u)||^2 ||vc(v)||^2\
    0 &<= (||vc(v)|| vc(u) - ||vc(u)|| vc(v)) dot (||vc(v)|| vc(u) - ||vc(u)||
      vc(v))\
    0 &<= || ||vc(v)|| vc(u) - ||vc(u)|| vc(v) ||^2$.
  ]
  Číslo napravo je druhá mocnina, tedy jistě kladné. Tím jsme dokázali, že
  nerovnost opravdu vždy platí. Důkaz faktu, že rovnost v
  @eq:trojuhelnikova-nerovnost nastane, když $vc(u)$ je násobek $vc(v)$, necháme
  jako úlohu na závěr.
]
