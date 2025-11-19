#import "../template.typ": *

== Řešení lineárních systémů

V této sekci formulujeme Gauβův-Jordanův algoritmus na řešení lineárních
systémů. S mírnými modifikacemi je tento algoritmus využíván počítači stále a je
zatím řádově nejrychlejším algoritmem na řešení lineárních systémů, jejž známe.

Nejprve však zavedeme pár základních definic a značení.

#definition("Lineární kombinace")[
  Ať $n$ je přirozené číslo, $x_1, x_2, ..., x_n$ jsou proměnné a $a_1, a_2,
  ..., a_n$ jsou čísla. Výraz typu
  #align(center)[
    $display(a_1 x_1 + a_2 x_2 + ... + a_n x_n)$
  ]
  nazveme _lineární kombinací_ proměnných $x_1, ..., x_n$.
] <def:lin-komb>

#definition("Lineární rovnice")[
  Jsou-li $x_1, ..., x_n$ proměnné a $a_1, ..., a_n, b$ čísla, pak rovnost
  #math.equation(block: true)[
    $display(a_1 x_1 + a_2 x_2 + ... + a_n x_n = b)$,
  ] <eq:lin-rce>

  kde levá strana je #link(<def:lin-komb>, "lineární kombinace")
  proměnných $x_1, ..., x_n$, nazveme _lineární rovnicí_ (v~proměnných $x_1,
  ..., x_n$). _Řešením_ lineární rovnice je jakákoli $n$-tice čísel $(s_1, s_2, ...,
    s_n)$, pro kterou platí rovnost @eq:lin-rce po dosazení za proměnné $x_1, ...,
  x_n$.
] <def:lin-rce>

#definition("Lineární systém")[
  Množinu #link(<def:lin-rce>, "lineárních rovnic")
  #math.equation(block: true)[
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, center, center, end, center, start),
      $a_(1,1) x_1$,
      $+$,
      $a_(1,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(1,n) x_n$,
      $=$,
      $b_1$,

      $a_(2,1) x_1$,
      $+$,
      $a_(2,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(2,n) x_n$,
      $=$,
      $b_2$,

      [], $dots.v$, [], $dots.v$, [], $dots.v$, [], $dots.v$, [],
      $a_(m,1) x_1$,
      $+$,
      $a_(m,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(m,n) x_n$,
      $=$,
      $b_m$,
    )] <eq:lin-sys>
  nazveme _lineárním systémem_. _Řešením_ lineárního systému @eq:lin-sys je
  jakákoli $n$-tice $(s_1, s_2, ..., s_n)$ řešící každou jeho rovnici.
] <def:lin-sys>

Při práci s lineárními rovnicemi budeme vždy předpokládat, že jsou zapsány jako
v @eq:lin-rce. Když lineární rovnice není v tomto tvaru, např. $3x_1 - 2x_2 - 5
= 3x_3$ můžeme ji totiž na tento tvar snadno upravit tak, že všechny proměnné
dáme nalevo a čísla napravo, tedy takto: $3x_1 - 2x_2 - 3x_3 = 5$.

=== Gauβův-Jordanův algoritmus

Ideu nalezení řešení #link(<def:lin-sys>, "lineárního systému") přes
Gauβův-Jordanův algoritmus nejprve ilustrujeme na příkladě.

#math.equation(block: true)[
  $
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, end, center, start),
      $x_1$, $+$, $2x_2$, $-$, $x_3$, $=$, $7$,
      $2x_1$, $+$, $2x_2$, [], [], $=$, $0$,
      $-x_1$, $+$, $4x_2$, $+$, $2x_3$, $=$, $7$,
    )
  $
] <eq:sys-exam-1>

Budeme postupovat tak, že nejprve z prvního sloupce a všech řádků _kromě_
prvního "vyeliminujeme" proměnnou $x_1$. Konkrétně, odečteme dvojnásobek první
rovnice od druhé a pak přičteme první rovnici ke třetí. Zatím nám věřte, že
takovéto úpravy nechávají řešení systému nedotčeno. Brzy si to rozmyslíme
pořádně.

Výsledkem bude systém
#math.equation(numbering: none, block: true)[
  $
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, end, center, start),
      $x_1$, $+$, $2x_2$, $-$, $x_3$, $=$, $7$,
      [], [], $-2x_2$, $+$, $2x_3$, $=$, $-14$,
      [], [], $6x_2$, $+$, $x_3$, $=$, $14$,
    )
  $
]

Konečně, z druhého sloupce a všech řádků pod druhým (tedy již pouze z třetího)
vyeliminujeme proměnnou $x_2$. Díky tomu, že již v žádném řádku kromě prvního
není přítomna proměnná $x_1$, zbavíme se takto z třetího řádku proměnné $x_2$,
aniž do něj "vrátíme" proměnnou $x_1$. Přičítáme proto trojnásobek druhé rovnice
ke třetí a dostáváme
#math.equation(numbering: none, block: true)[
  $
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, end, center, start),
      $x_1$, $+$, $2x_2$, $-$, $x_3$, $=$, $7$,
      [], [], $-2x_2$, $+$, $2x_3$, $=$, $-14$,
      [], [], [], [], $7x_3$, $=$, $-28$,
    )
  $
]

Teď je systém ve stavu, kdy můžeme zpětnou substitucí (nejprve spočítáme $x_3$,
s jeho pomocí $x_2$ atd.) systém dopočítat. Z poslední rovnice víme, že $x_3 =
-4$. Dosazením do druhé rovnice dostaneme
#math.equation(numbering: none, block: true)[
  $-2x_2 + 2 dot (-4) = -14$
]
a tím pádem $x_2 = 3$. Konečně, z první rovnice
#math.equation(numbering: none, block: true)[
  $x_1 + 2 dot 3 - (-4) = 7$,
]
takže $x_1 = -3$. Našli jsme řešení @eq:sys-exam-1 v podobě $(-3, 3, -4)$.

V právě spočteném příkladě jsme upravovali #link(<def:lin-sys>, "lineární systém")
tak, že jsme přičítali (či odečítali) násobky rovnic od rovnic jiných. Že je
tato úprava *ekvivalentní* ve smyslu, že nemění množinu řešení systému, si záhy
rozmyslíme. Navíc k této úpravě můžeme též prohazovat rovnice a násobit rovnice
nenulovými čísly. Tyto tři úpravy lineárních systémů se souhrnně nazývají
"elementární řádkové úpravy" z důvodů, jež ještě objasníme.

#definition("Elementární řádkové úpravy")[
  Následující tři úpravy lineárních systémů:
  + prohození dvou rovnic,
  + vynásobení rovnice nenulovým číslem,
  + přičtení násobku jedné rovnice k jiné,
  nazveme _elementárními řádkovými úpravami_.
] <def:el-upravy>

#proposition[
  #link(<def:el-upravy>, "Elementární řádkové úpravy") nemění množinu řešení
  lineárního systému.
]

#proof[
  Že úpravy (1) a (2) nemění množinu řešení lineárního systému, je zřejmé,
  protože jsou ihned zvratné prohozením týchž rovnic či zpětným vydělením
  vynásobené rovnice.

  Spočítáme si pořádně, že úprava (3) nemění množinu řešení lineárního systému
  #math.equation(block: true)[
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, center, center, end, center, start),
      $a_(1,1) x_1$,
      $+$,
      $a_(1,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(1,n) x_n$,
      $=$,
      $b_1$,

      $a_(2,1) x_1$,
      $+$,
      $a_(2,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(2,n) x_n$,
      $=$,
      $b_2$,

      [], $dots.v$, [], $dots.v$, [], $dots.v$, [], $dots.v$, [],
      $a_(m,1) x_1$,
      $+$,
      $a_(m,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(m,n) x_n$,
      $=$,
      $b_m.$,
    )
  ] <eq:lin-sys-prf-1>
  Řekněme, že jsme provedli přičtení $c$-násobku $#clb[i]$-té rovnice k $j$-té.
  Pak místo $j$-té rovnice v~systému vznikne rovnice
  #math.equation(block: true)[
    $a_(j,1) x_1 + a_(j,2) x_2 + ... + a_(j,n) x_n + c dot (#clb[$a_(i,1) x_1 +
      a_(i,2) x_2 + ... + a_(i,n) x_n$]) = b_j + c dot #clb[$b_i$]$.
  ] <eq:i-j-eq>
  Abychom ověřili, že množina řešení systému zůstala i po této změně stejná,
  vezměme nějaké řešení $(s_1, s_2, ..., s_n)$ systému @eq:lin-sys-prf-1.
  Protože $j$-tá rovnice je ta jediná změněná, dosadíme do ní řešení
  $(s_1,...,s_n)$ a ověříme, že je jejím řešením stále. Dostaneme
  #math.equation(numbering: none, block: true)[
    $a_(j,1)s_1 + a_(j,2)s_2 + ... + a_(j,n)s_n + c dot (#clb[$a_(i,1) s_1 +
      a_(i,2) s_2 + ... + a_(i,n)s_n$]) = b_j + c dot #clb[$b_i$]$.
  ]
  Jelikož ale $(s_1,...,s_n)$ řeší jak #clb[$i$]-tou, tak $j$-tou rovnici, platí
  #math.equation(numbering: none, block: true)[
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, center, center, end, center, start),
      clb[$a_(i,1) s_1$],
      clb[$+$],
      clb[$a_(i,2) s_2$],
      clb[$+$],
      clb[$...$],
      clb[$+$],
      clb[$a_(i,n) s_n$],
      clb[$=$],
      [#clb[$b_i$],],

      $a_(j,1) s_1$,
      $+$,
      $a_(j,2) s_2$,
      $+$,
      $...$,
      $+$,
      $a_(j,n) s_n$,
      $=$,
      $b_j$,
    )
  ]
  Dosazením do @eq:i-j-eq vznikne
  #math.equation(numbering: none, block: true)[
    $b_j + c dot (#clb[$b_i$]) = b_j + c dot #clb[$b_i$]$,
  ]
  kterážto rovnice zřejmě platí. Tím máme hotovo, protože jsme ověřili, že
  jakékoli řešení původního systému je stále řešením modifikovaného systému.
]

Na #link(<def:el-upravy>, "elementárních řádkových úpravách") je postaven právě
Gauβův-Jordanův algoritmus, jak jste měli možnost vidět už na příkladu výše.
Formulujeme jej nyní formálně, ale doporučujeme při jeho čtení mít stále na
mysli příklad ze začátku podsekce. Jediný případ, který tento příklad nepokrývá
a může nastat, je, že například v druhém sloupci a druhém řádku proměnná $x_2$
není (její koeficient je $0$). V tomto případě prohodíme druhý řádek s nějakým
nižším, ve kterém proměnná $x_2$ je a pokračujeme s eliminací. Pokud v žádném
řádku pod druhým proměnná $x_2$ není, nebudeme ji eliminovat (není odkud) a
pokračujeme s proměnnou $x_3$.

#no-strips-algo[
  #algo(
    header: "Gauβův-Jordanův algoritmus",
    fill: gray.transparentize(90%),
    line-numbers: false,
    stroke: 1pt + mainlight,
    breakable: true,
  )[
    *INPUT*: lineární systém @eq:lin-sys #h(1fr)\
    *OUTPUT*: tentýž lineární systém ve tvaru připraveném na zpětnou substituci (tzv. _odstupňovaný_ tvar)\
    \
    V $i$-tém sloupci dělej následující.
    #enum[
      Najdi $k >= i$ takové, že $a_(k,i) != 0$ (tj. v $k$-té rovnici "je"
      proměnná $x_i$).
      - Pokud takové $k$ neexistuje, nic nedělej a pokračuj dalším sloupcem.
    ][
      Prohoď $i$-tý a $k$-tý řádek.
    ][
      Pro každé $j > i$ (tedy pro každý řádek pod $i$-tým):\
      #enum[
        Spočti $c = -a_(j,i) slash a_(i,i)$ (tedy čím musím vynásobit řádek $i$,
        aby měl u $x_i$ -koeficient u $x_i$ v řádku $j$).
      ][
        Přičti $c$-násobek $i$-tého řádku k $j$-tému (tím se zbavím $x_i$ v $j$-tém řádku).
      ]
    ][
      Pokračuj dalším sloupcem.
    ]
  ]<alg:gauss-jordan>
]

Po skončení #link(<alg:gauss-jordan>, "Gauβova-Jordanova algoritmu") je lineární
systém v tzv. _odstupňovaném tvaru_, což znamená, že každý řádek má méně
proměnných než řádek přímo nad ním. Systém v tomto tvaru je připraven na zpětnou
substituci, kdy spočteme řešení systému tak, že hodnoty proměnných spočtené v
nižších řádcích dosazujeme do řádků vyšších.

Princip #link(<alg:gauss-jordan>, "Gauβova-Jordanova algoritmu") ilustrujeme na
ještě jednom příkladě. Spočteme řešení systému
#math.equation(block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    [], [], $-x_2$, $+$, $x_3$, $+$, $x_4$, $=$, $1$,
    $2x_1$, [], [], $+$, $x_3$, [], [], $=$, $0$,
    [], [], $x_2$, $+$, $3x_3$, $-$, $2x_4$, $=$, $8$,
    $x_1$, $+$, $x_2$, $+$, $2x_3$, $+$, $x_4$, $=$, $2$,
  )
] <eq:lin-sys-gauss-1>

Na začátku algoritmu je $i = 1$, začínáme tedy prvním sloupcem. Najdeme $k >= 1$
takové, že $a_(k,1) != 0$. Jedna možnost je například $k = 4$, tj. čtvrtý řádek
má v prvním sloupci něco jiného než $0$. Prohodíme první a čtvrtý řádek.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $x_1$, $+$, $x_2$, $+$, $2x_3$, $+$, $x_4$, $=$, $2$,
    $2x_1$, [], [], $+$, $x_3$, [], [], $=$, $0$,
    [], [], $x_2$, $+$, $3x_3$, $-$, $2x_4$, $=$, $8$,
    [], [], $-x_2$, $+$, $x_3$, $+$, $x_4$, $=$, $1$,
  )
]
Nyní budeme pro každé $j > 1$ odčítat $(a_(j,1) slash a_(1,1))$-násobek prvního
řádku od $j$-tého. Pro $j = 2$ je $a_(2,1) slash a_(1,1) = 2$, takže odečteme
dvojnásobek prvního řádku od druhého. Pro $j = 3$ a $j = 4$ vychází $a_(j,1)
slash a_(1,1) = 0$, takže nemusíme dělat nic.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $x_1$, $+$, $x_2$, $+$, $2x_3$, $+$, $x_4$, $=$, $2$,
    [], [], $-2x_2$, $-$, $3x_3$, $-$, $2x_4$, $=$, $-4$,
    [], [], $x_2$, $+$, $3x_3$, $-$, $2x_4$, $=$, $8$,
    [], [], $-x_2$, $+$, $x_3$, $+$, $x_4$, $=$, $1$,
  )
]
Pokračujeme druhým sloupcem, tedy $i = 2$. Tentokrát je v druhém řádku a druhém
sloupci nenulové číslo, takže nemusíme prohazovat nic. Spočteme, že $a_(3,2)
slash a_(2,2) = -1 slash 2$ a $a_(4,2) slash a_(2,2) = 1 slash 2$, takže
přičítáme polovinu druhého řádku ke třetímu a odečítáme polovinu druhého řádku
od čtvrtého.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $x_1$, $+$, $x_2$, $+$, $2x_3$, $+$, $x_4$, $=$, $2$,
    [], [], $-2x_2$, $-$, $3x_3$, $-$, $2x_4$, $=$, $-4$,
    [], [], [], [], $3/2 x_3$, $-$, $3x_4$, $=$, $6$,
    [], [], [], [], $5/2 x_3$, $+$, $2x_4$, $=$, $3$,
  )
]
Konečně, pokračujeme třetím sloupcem. Máme $a_(3,3) != 0$, takže nemusíme
prohazovat. Spočteme $a_(4,3) slash a_(3,3) = 5 slash 3$. Odečteme pročež $(5
  slash 3)$-násobek třetího řádku od čtvrtého.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $x_1$, $+$, $x_2$, $+$, $2x_3$, $+$, $x_4$, $=$, $2$,
    [], [], $-2x_2$, $-$, $3x_3$, $-$, $2x_4$, $=$, $-4$,
    [], [], [], [], $3/2 x_3$, $-$, $3x_4$, $=$, $6$,
    [], [], [], [], [], [], $7x_4$, $=$, $-7$,
  )
]
Nyní je systém v odstupňovaném tvaru a provedeme zpětnou substituci. Z
posledního řádku plyne, že $x_4 = -1$. Tuto hodnotu dosadíme za $x_4$ do řádku
$3$ a spočteme rovnici
#math.equation(numbering: none, block: true)[
  $3/2 x_3 - 3 dot (-1) = 6$,
]
jejímž řešením je $x_3 = 2$. Spočtené hodnoty pro $x_3$ a $x_4$ dosadíme do
řádku druhého a vyřešíme rovnici
#math.equation(numbering: none, block: true)[
  $-2x_2 -3 dot 2 - 2 dot (-1) = -4$.
]
Dostaneme $x_2 = 0$. Konečně, dosazením $x_2$, $x_3$ a $x_4$ do prvního řádku
dopočítáme
#math.equation(numbering: none, block: true)[
  $x_1 + 0 + 2 dot 2 + (-1) = 2$,
]
čili $x_1 = -1$. Řešením systému je čtveřice $(-1, 0, 2, -1)$.

=== Tvar řešení lineárních systémů

V této sekci se nebudeme zabývat tím, jak lineární systémy řešit, ale spíše, jak
množiny jejich řešení mohou vypadat. Konkrétně, rádi bychom uměli zobecnit
situaci, kterou ilustruje následující systém.
#math.equation(block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $2x_1$, $-$, $x_2$, $+$, $3x_3$, $-$, $x_4$, $=$, $2$,
    [], [], [], [], $-x_3$, $+$, $3x_4$, $=$, $5$,
  )
]<eq:lin-sys-par-1>
Tento systém *je* v odstupňovaném tvaru, protože druhý řádek "začíná víc
napravo" než první. Ovšem, určitě se nedobereme jednoho konkrétního řešení,
neboť z druhého řádku můžeme nanejvýš hodnotu proměnné $x_3$ vyjádřit pomocí
proměnné $x_4$ nebo naopak. My budeme takovéto systému vždy řešit tak, že tu
proměnnou, *která je nejvíc nalevo* v daném řádku nazveme #clr[pivotem] a zbytek
proměnných v řádku (které *nejsou pivoty z nižších řádků*) nazveme #clb[volnými
  proměnnými] nebo #clb[parametry].

Rozdělení na #clr[pivoty] a #clb[volné proměnné] v systému @eq:lin-sys-par-1
vypadá takto:
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    clr[$2x_1$], $-$, clb[$x_2$], $+$, clr[$3x_3$], $-$, clb[$x_4$], $=$, $2$,
    [], [], [], [], clr[$-x_3$], $+$, clb[$3x_4$], $=$, $5$,
  )
]
Řešení takových systémů budeme vždy zapisovat tím způsobem, že hodnoty všech
#clr[pivotů] vyjádříme pomocí #clb[volných proměnných]. #clb[Volné proměnné]
budeme obvykle přeznačovat písmeny $t_1$, $t_2$ atd., abychom je odlišili od
#clr[pivotů].

Z druhé rovnice systému @eq:lin-sys-par-1 můžeme vyjádřit #clr[$x_3$] pomocí
#clb[$x_4$] jako $#clr[$x_3$] = 3#clb[$x_4$] - 5$. Jak jsme zmiňovali, pro
přehlednost označíme volnou proměnnou #clb[$x_4$] jako #clb[$t_1$]. Máme tedy
rovnost $#clr[$x_3$] = 3#clb[$t_1$] - 5$. Proměnná #clb[$x_2$] je též volná,
označíme ji jako #clb[$t_2$]. Dosazením za #clr[$x_3$] a #clb[$x_4$] do první
rovnice dostaneme
#math.equation(numbering: none, block: true)[
  $2 #clr[$x_1$] - #clb[$t_2$] + 3 dot (3#clb[$t_1$] - 5) - #clb[$t_1$] = 2$.
]
Odtud spočteme, že
#math.equation(numbering: none, block: true)[
  $#clr[$x_1$] = -4#clb[$t_1$] + 1/2#clb[$t_2$] + 17/2$.
]
Řešením systému jsou pročež všechny čtveřice $(-4#clb[$t_1$] + (1 slash 2)
  #clb[$t_2$] + 17 slash 2, clb(t_2), 3#clb[$t_1$] - 5, #clb[$t_1$])$, kde
#clb[$t_1$] a #clb[$t_2$] jsou libovolná čísla.

Abychom řešení takových systémů uměli zapsat přehledněji, zavedeme si pojmy
_vektoru_ a _matice_. V příští kapitole se rozhovoříme o jejich geometrickém
významu. Zatím pro nás budou pouze představovat pohodlný způsob zápisu.

#definition("Matice")[
  _Maticí_ $A$ velikosti $m times n$ nazveme tabulku čísel s $m$ řádky a $n$
  sloupci, čili tabulku
  #math.equation(numbering: none, block: true)[
    $A = mat(
      a_(1,1), a_(1,2), dots.c, a_(1,n);
      a_(2,1), a_(2,2), dots.c, a_(2,n);
      dots.v, dots.v, dots.down, dots.v;
      a_(m,1), a_(m,2), dots.c, a_(m,n);
    )$.
  ]
  Často budeme tabulku výše zapisovat zkráceným způsobem $A =
  (a_(i,j))_(i,j=1)^(m,n)$. Číslům $a_(i,j)$ budeme říkat různě, většinou
  _vstupy_, _složky_ či _souřadnice_ matice $A$.
]
#definition("Vektor")[
  Matici s *pouze jedním sloupcem* nazveme _sloupcovým vektorem_. Matici s
  *pouze jedním řádkem* zase _řádkovým vektorem_. Sloupcové i řádkové vektory
  budeme značit malými písmeny s šipkou. Například
  #math.equation(numbering: none, block: true)[
    $vc(v) = vec(v_1, v_2, dots.v, v_n)$
  ]
  je sloupcový vektor s $n$ složkami.
]
#definition("Operace s vektory")[
  Sloupcové i řádkové vektory můžeme spolu sčítat (mají-li stejně složek) a
  násobit čísly. Ať
  #math.equation(numbering: none, block: true)[
    $vc(u) = vec(u_1, u_2, dots.v, u_n) " a " vc(v) = vec(v_1, v_2, dots.v, v_n)$
  ]
  jsou dva vektory a $r$ je číslo. Pak definujeme
  #math.equation(numbering: none, block: true)[
    $vc(u) + vc(v) = vec(u_1 + v_1, u_2 + v_2, dots.v, u_n + v_n)$
  ]
  a také
  #math.equation(numbering: none, block: true)[
    $r dot vc(v) = vec(r v_1, r v_2, dots.v, r v_n)$.
  ]
]
#remark[
  Násobení vektorů číslem budeme vždy značit symbolem $dot$ jako v případě $r
  dot vc(v)$, zatímco běžné násobení čísel vyjádříme absencí symbolu, jako v
  případě $r v_1$. Časem bude toto rozlišení důležité.
]

Přeformulujeme pár pojmů z teorie lineárních systémů do maticové podoby. Pro
lineární systém
#math.equation(block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, end, center, start),
    $a_(1,1) x_1$,
    $+$,
    $a_(1,2) x_2$,
    $+$,
    $...$,
    $+$,
    $a_(1,n) x_n$,
    $=$,
    $b_1$,

    $a_(2,1) x_1$,
    $+$,
    $a_(2,2) x_2$,
    $+$,
    $...$,
    $+$,
    $a_(2,n) x_n$,
    $=$,
    $b_2$,

    [], $dots.v$, [], $dots.v$, [], $dots.v$, [], $dots.v$, [],
    $a_(m,1) x_1$,
    $+$,
    $a_(m,2) x_2$,
    $+$,
    $...$,
    $+$,
    $a_(m,n) x_n$,
    $=$,
    $b_m$,
  )]<eq:lin-sys-2>
označíme
#math.equation(numbering: none, block: true)[
  $A = mat(
    a_(1,1), a_(1,2), dots.c, a_(1,n);
    a_(2,1), a_(2,2), dots.c, a_(2,n);
    dots.v, dots.v, dots.down, dots.v;
    a_(m,1), a_(m,2), dots.c, a_(m,n);
  )", "vc(b) = vec(b_1, b_2, dots.v, b_m) " a "
  vc(x) = vec(x_1, x_2, dots.v, x_n)$.
]
Řekneme, že @eq:lin-sys-2 je lineární systém s maticí $A$ a vektorem pravé
strany $vc(b)$. Často jej budeme zkráceně zapisovat jako
#math.equation(numbering: none, block: true)[
  $A vc(x) = vc(b)$.
]
Smysluplnost tohoto značení vysvětlíme později.

Dále, řekneme, že vektor
#math.equation(numbering: none, block: true)[
  $vc(s) = vec(s_1, s_2, dots.v, s_n)$
]
je řešením systému @eq:lin-sys-2, když je n-tice $(s_1,s_2,...,s_n)$ jeho
řešením ve smyslu @def:lin-sys.

Zapíšeme řešení příkladného systému @eq:lin-sys-par-1 ve "vektorové podobě".
Sepíšeme-li jednotlivé proměnné do řádků, dostaneme
#math.equation(numbering: none, block: true)[
  $x_1 &= 17/2 - 4t_1 + 1/2 t_2\
  x_2 &= t_2\
  x_3 &= -5 + 3t_1\
  x_4 &= t_1$.
]
Navíc zápis upravíme tak, aby každá volná proměnná byla ve svém vlastním
sloupci.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, center, center, start),
    $x_1$, $=$, $display(17 / 2)$, $-$, $4t_1$, $+$, $display(1/2 t_2)$,
    $x_2$, $=$, [], [], [], [], $t_2$,
    $x_3$, $=$, $-5$, $+$, $3t_1$, [], [],
    $x_4$, $=$, [], [], $t_1$, [], [],
  )
]
Abychom viděli, kde se v takovém zápisu schovávají ony vektory, doplníme prázdná
místa nulami a zvýrazníme koeficienty.
#math.equation(numbering: none, block: true)[
  #grid(
    columns: (auto, auto, auto, auto, auto, auto, auto),
    column-gutter: 0.3em,
    row-gutter: 1em,
    align: (end, center, end, center, end, center, start),
    $x_1$,
    $=$,
    $clr(display(17 / 2))$,
    $+$,
    $clb(-4)t_1$,
    $+$,
    $display(clg(1/2) t_2)$,

    $x_2$, $=$, $clr(0)$, $+$, $clb(0)t_1$, $+$, $clg(1)t_2$,
    $x_3$, $=$, $clr(-5)$, $+$, $clb(3)t_1$, $+$, $clg(0)t_2$,
    $x_4$, $=$, $clr(0)$, $+$, $clb(1)t_1$, $+$, $clg(0)t_2$,
  )
]
Položíme
#math.equation(numbering: none, block: true)[
  $vc(x) = vec(x_1, x_2, x_3, x_4)", "clr(vc(p)) = vec(
    clr(17/2), clr(0),
    clr(-5), clr(0)
  )", "clb(vc(v_1)) = vec(clb(-4), clb(0), clb(3), clb(1))" a "clg(vc(v_2)) =
  vec(clg(1/2), clg(1), clg(0), clg(0))$.
]
Teď můžeme napsat řešení systému @eq:lin-sys-par-1 jako
#math.equation(numbering: none, block: true)[
  $vc(x) = clr(vc(p)) + t_1 dot clb(vc(v_1)) + t_2 dot clg(vc(v_2))$.
]
Tvrdíme, že množinu řešení *každého* lineárního systému lze vyjádřit tímto
způsobem.

#theorem("Tvar řešení lineárního systému")[
  Množina řešení systému @eq:lin-sys má tvar
  #math.equation(numbering: none, block: true)[
    ${vc(p) + t_1 dot vc(v_1) + t_2 dot vc(v_2) + ... + t_k dot vc(v_k)$},
  ]
  kde $vc(p)$ je jedno konkrétní řešení a $t_1,t_2,...,t_k$ jsou volné proměnné.
]<thm:tvar-reseni>

K důkazu @thm:tvar-reseni[věty] si pomůžeme malým obchvatem. Totiž, budeme se
nejprve soustředit na lineární systémy, které mají na pravé straně samé nuly.
Tvar množiny řešení takových systémů je jednodušší popsat z toho důvodu, že
n-tice $(0,0,...,0)$ je *vždy* jedním konkrétním řešením. Tyto systémy nazveme
_homogenní_.

#definition("Homogenní systém")[
  Lineární systém $A vc(x) = vc(b)$ nazveme _homogenním_, když
  #math.equation(numbering: none, block: true)[
    $vc(b) = vc(0) = vec(0, 0, dots.v, 0)$,
  ]
  čili jeho pravou stranou je vektor samých nul.
]<def:homogenni-system>

#proposition("Tvar řešení homogenního systému")[
  Každý homogenní systém $A vc(x) = vc(0)$ má množinu řešení ve tvaru
  #math.equation(numbering: none, block: true)[
    ${t_1 dot vc(v_1) + t_2 dot vc(v_2) + ... + t_k dot vc(v_k)}$,
  ]
  kde $t_1,...,t_k$ jsou volné proměnné a $vc(v_1),...,vc(v_k)$ jsou vhodné
  vektory koeficientů.
]
#proof[
  Tvrzení dokážeme podobným způsobem, jako bychom homogenní systém řešili.
  Totiž, nejprve použijeme #link(<alg:gauss-jordan>, [Gauβův-Jordanův
    algoritmus]), a dostaneme homogenní systém
  #math.equation(numbering: none, block: true)[
    #grid(
      columns: (auto, auto, auto, auto, auto, auto, auto, auto, auto),
      column-gutter: 0.3em,
      row-gutter: 1em,
      align: (end, center, end, center, center, center, end, center, start),
      $a_(1,1) x_1$,
      $+$,
      $a_(1,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(1,n) x_n$,
      $=$,
      $0$,

      $a_(2,1) x_1$,
      $+$,
      $a_(2,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(2,n) x_n$,
      $=$,
      $0$,

      [], $dots.v$, [], $dots.v$, [], $dots.v$, [], $dots.v$, [],
      $a_(m,1) x_1$,
      $+$,
      $a_(m,2) x_2$,
      $+$,
      $...$,
      $+$,
      $a_(m,n) x_n$,
      $=$,
      $0$,
    )]
  do odstupňovaného tvaru. Z odstupňovaného tvaru dokážeme totiž přesně vyčíst,
  které proměnné jsou volné a které jsou pivoty. Konkrétně, připomínáme, že
  pivoty jsou vždy proměnné s prvním nenulovým koeficientem v každém řádku anebo
  pivoty z řádků pod ním. Všechny ostatní proměnné jsou volné. Pro představu
  vizte @fig:lin-sys-odstupnovany[obrázek].

  V tomto tvaru provedeme zpětnou substituci. To znamená, že vyjádříme pivota z
  posledního řádku (tam je jen jeden) pomocí volných proměnných z posledního
  řádku. Dosadíme z téhož pivota v řádku výše. Tím získáme rovnici, v níž
  vystupují pouze volné proměnné a nejlevější pivot v tomto řádku. Opět jej
  vyjádříme pomocí volných proměnných. Takhle postupujeme dále, dokud
  nevyjádříme pivota v prvním řádku.

  Že takový postup je formální, zajišťuje princip matematické indukce (vizte
  @chap:matematicka-indukce[kapitolu]). Totiž, v prvním indukčním kroku zkrátka
  vyjádříme pivot v posledním řádku pomocí volných proměnných. To jistě lze, jak
  jsme si již rozmysleli, neb je v posledním řádku pivot pouze jeden.

  V druhém indukčním kroku předpokládejme, že se nacházíme v $i$-tém řádku
  zespoda a všechny pivoty v nižších řádcích jsou již vyjádřeny pomocí volných
  proměnných. Dosazením do tohoto řádku způsobí, že všechny pivoty kromě
  nejlevějšího "zmizí", neboť jsou vyjádřeny pomocí volných proměnných. Tudíž, i
  tento jeden pivot můžeme vyjádřit pomocí volných proměnných a jsme hotovi.
]

#figure(
  cetz.canvas({
    import cetz.draw: *

    for coor in ((0, 0), (3, 0), (4, 0), (6, 0)) {
      circle(coor, fill: red, stroke: 0pt, radius: 0.2)
    }
    for (x, y) in ((1, 0), (2, 0), (5, 0), (7, 0)) {
      rect((x - 0.2, y - 0.2), (x + 0.2, y + 0.2), fill: blue, stroke: 0pt)
    }

    for coor in ((3, -1), (4, -1), (6, -1)) {
      circle(coor, fill: red, stroke: 0pt, radius: 0.2)
    }
    for (x, y) in ((5, -1), (7, -1)) {
      rect((x - 0.2, y - 0.2), (x + 0.2, y + 0.2), fill: blue, stroke: 0pt)
    }

    for coor in ((4, -2), (6, -2)) {
      circle(coor, fill: red, stroke: 0pt, radius: 0.2)
    }
    for (x, y) in ((5, -2), (7, -2)) {
      rect((x - 0.2, y - 0.2), (x + 0.2, y + 0.2), fill: blue, stroke: 0pt)
    }

    circle((6, -3), fill: red, stroke: 0pt, radius: 0.2)
    rect((7 - 0.2, -3 - 0.2), (7 + 0.2, -3 + 0.2), fill: blue, stroke: 0pt)
  }),
  caption: [Levá strana lineárního systému v odstupňovaném tvaru. Symboly
    #box(baseline: 0.1em, rect(
      width: 8pt,
      height: 8pt,
      fill: blue,
      stroke: none,
    ))
    značí volné proměnné a symboly #box(baseline: 0.1em, circle(radius: 4pt, fill: red, stroke: none)) pivoty.],
)<fig:lin-sys-odstupnovany>


