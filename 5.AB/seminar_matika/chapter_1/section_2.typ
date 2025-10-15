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
  ]
]
