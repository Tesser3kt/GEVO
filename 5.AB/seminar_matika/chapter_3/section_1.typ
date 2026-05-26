#import "../template.typ": *

== Soustavy souřadnic (aspoň trochu) prakticky

=== Krystaly

Krystaly jsou látky, jejichž atomová struktura je extrémně pravidelná,
uspořádaná do čtverců, obdélníků nebo mnohoúhelníků a jejich
vícedimensionálních variant. Vezměme například sůl, tj. chlorid sodný. Atomy
chloru a sodíku jsou zde uspořádány v krychlích, jejichž vrcholy a středy stěn
okupuje chlorid a středy hran sodík.

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Cube
    line((0, 0), (2, 0))
    line((0, 0), (0, 2))
    line((0, 0), (0.8, 0.8), stroke: (dash: "dashed"))
    line((2, 0), (2.8, 0.8))
    line((0, 2), (0.8, 2.8))
    line((0, 2), (2, 2))
    line((2, 0), (2, 2))
    line((2, 2), (2.8, 2.8))
    line((2.8, 0.8), (2.8, 2.8))
    line((0.8, 2.8), (2.8, 2.8))
    line((0.8, 0.8), (0.8, 2.8), stroke: (dash: "dashed"))
    line((0.8, 0.8), (2.8, 0.8), stroke: (dash: "dashed"))

    // Chloride
    circle(
      (0.8, 0.8),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.8, 1.8),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (0.4, 1.4),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.4, 0.4),
      radius: 6pt,
      fill: blue.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    for x in (0, 2) {
      for y in (0, 2) {
        circle((x, y), radius: 6pt, fill: blue)
        if (x, y) != (0, 0) {
          circle((x + 0.8, y + 0.8), radius: 6pt, fill: blue)
        }
      }
    }

    circle((1, 1), radius: 6pt, fill: blue)
    circle((1.4, 2.4), radius: 6pt, fill: blue)
    circle((2.4, 1.4), radius: 6pt, fill: blue)

    // Sodium
    circle(
      (0.4, 0.4),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (0.8, 1.8),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle(
      (1.8, 0.8),
      radius: 3pt,
      fill: yellow.transparentize(60%),
      stroke: black.transparentize(60%),
    )
    circle((0, 1), radius: 3pt, fill: yellow)
    circle((1, 0), radius: 3pt, fill: yellow)
    circle((1, 2), radius: 3pt, fill: yellow)
    circle((2, 1), radius: 3pt, fill: yellow)
    circle((0.4, 2.4), radius: 3pt, fill: yellow)
    circle((1.8, 2.8), radius: 3pt, fill: yellow)
    circle((2.4, 2.4), radius: 3pt, fill: yellow)
    circle((2.4, 2.4), radius: 3pt, fill: yellow)
    circle((2.4, 0.4), radius: 3pt, fill: yellow)
    circle((2.4, 0.4), radius: 3pt, fill: yellow)
    circle((2.8, 1.8), radius: 3pt, fill: yellow)
  }),
  caption: [Atomová struktura soli.],
)

Při práci s takovouto strukturou bychom rádi uměli vyjádřit pozice jednotlivých
atomů nějakým jednoduchým způsobem. Pro přehlednost se soustřeďme jenom na
přední stěnu krystalické struktury.

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Grid
    for x in (0, 2, 4, 6) {
      line((x, 0), (x, 4))
    }
    for y in (0, 2, 4) {
      line((0, y), (6, y))
    }

    for x in (0, 2, 4, 6) {
      for y in (0, 2, 4) {
        // Chloride
        circle((x, y), radius: 6pt, fill: blue)
        if (x <= 4 and y <= 2) {
          circle((x + 1, y + 1), radius: 6pt, fill: blue)
        }
        // Sodium
        if (x <= 4) {
          circle((x + 1, y), radius: 3pt, fill: yellow)
        }
        if (y <= 2) {
          circle((x, y + 1), radius: 3pt, fill: yellow)
        }
      }
    }
  }),
  caption: [Přední stěna atomové struktury soli.],
)

Délka jedné hrany sítě je 3.34 Ångstromů (jednotek značících $10^(-10)$ metrů).
Není výpočetně praktické, abychom při representaci takovéto mříže v počítači
museli neustále počítat s násobky desetinných čísel. Přirozenou "soustavou
souřadnic" je v tomto případě zřejmě dvojice kolmých os, kde jednotková
vzdálenost na obou osách odpovídá přesně délce hrany krychle. Označíme-li levý
dolní atom chloru jako počátek této soustavy, pak atom v prostředním řádku a
třetím sloupci má v této soustavě souřadnice $(2, 1)$ místo neohrabaných 6.68
Ångstromů doprava a 3.34 Ångstromů nahoru. Jak si brzy vysvětlíme, volbu
soustavy souřadnic v prostoru můžeme provést výběrem vhodných vektorů, které
určují právě směr i jednotkovou vzdálenost všech os. V tomto případě by
rozumnou volbou byla dvojice vektorů
#math.equation(numbering: none, block: true)[
  $(vec(3.34, 0), vec(0, 3.34))$.
]

Krychlová struktura soli nám při volbě soustavy souřadnic byla velmi nápomocná.
Mohli jsme vyjít z běžné kartézské soustavy souřadnic a akorát vynásobit
jednotkovou vzdálenost obou os vhodnou konstantou (číslem $3.34$). Příroda není
vždy tak shovívavá.

Uvažme krystal zvaný _tuha_, tvořený atomy uhlíku uspořádanými do
šestiúhelníkové mříže. Jeho jedna atomová vrstva (též zvaná _grafen_) je
znázorněna na @fig:grafen[obrázku].

#figure(
  cetz.canvas({
    import cetz.draw: *

    // Lattice
    let sq3 = 1.73
    for x in (0, 3, 6) {
      for y in (0, sq3) {
        line((x, y), (x + 1, y))
        line((x, y), (x - 0.5, y + sq3 / 2))
        line((x + 1, y), (x + 1.5, y + sq3 / 2))
        line((x - 0.5, y + sq3 / 2), (x, y + sq3))
        line((x, y + sq3), (x + 1, y + sq3))
        line((x + 1, y + sq3), (x + 1.5, y + sq3 / 2))

        let x = x + 1.5
        let y = y + sq3 / 2
        line((x, y), (x + 1, y))
        line((x, y), (x - 0.5, y + sq3 / 2))
        line((x + 1, y), (x + 1.5, y + sq3 / 2))
        line((x - 0.5, y + sq3 / 2), (x, y + sq3))
        line((x, y + sq3), (x + 1, y + sq3))
        line((x + 1, y + sq3), (x + 1.5, y + sq3 / 2))
      }
    }

    // Carbon
    let carbon(x, y) = circle((x, y), radius: 4pt, fill: green)
    for x in (0, 3, 6) {
      for y in (0, sq3) {
        carbon(x, y)
        carbon(x + 1, y)
        carbon(x - 0.5, y + sq3 / 2)
        carbon(x, y + sq3)
        carbon(x + 1, y + sq3)
        carbon(x + 1.5, y + sq3 / 2)

        let x = x + 1.5
        let y = y + sq3 / 2
        carbon(x, y)
        carbon(x + 1, y)
        carbon(x - 0.5, y + sq3 / 2)
        carbon(x, y + sq3)
        carbon(x + 1, y + sq3)
        carbon(x + 1.5, y + sq3 / 2)
      }
    }
  }),
  caption: [Atomová struktura grafenu.],
) <fig:grafen>

Možná vás napadá, že hrany hexagonu opět určují ty pravé ořechové vektory pro
soustavu souřadnic. Je tomu tak. Totiž, pravidelný hexagon má sice hrany ve
třech různých směrech, ale je záhodno si všimnout, že do hrany vedoucí "doleva
nahoru" se dostaneme přes hranu vedoucí doprava a hranu vedoucí "doprava
nahoru". Vizte @fig:baze-grafen[obrázek].

#figure(
  cetz.canvas({
    import cetz.draw: *

    polygon((0, 0), 6, radius: 2)

    let sq3 = 1.73

    // First vec
    line(
      (-1, -sq3),
      (1, -sq3),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "u",
    )
    content(
      ("u.start", 50%, "u.end"),
      anchor: "south",
      padding: .2,
      clb[$vc(u)$],
    )

    // Second vec
    line(
      (1, -sq3),
      (2, 0),
      mark: (end: ">", fill: red),
      stroke: red + 2pt,
      name: "v",
    )
    content(
      ("v.start", 50%, "v.end"),
      anchor: "south-east",
      padding: .1,
      clr[$vc(v)$],
    )

    line(
      (2, 0),
      (-2, 0),
      mark: (end: ">", fill: blue),
      stroke: blue + 2pt,
      name: "-2u",
    )
    content(
      ("-2u.start", 50%, "-2u.end"),
      anchor: "south",
      padding: .2,
      clb[$-2 dot.c vc(u)$],
    )

    line(
      (-1, -sq3),
      (-2, 0),
      mark: (end: ">", fill: purple),
      stroke: purple + 2pt,
      name: "w",
    )
    content(
      ("w.start", 50%, "w.end"),
      anchor: "north-east",
      padding: .1,
      $#clb[$-vc(u)$] + #clr[$vc(v)$]$,
    )
  }),
  caption: [Soustava souřadnic pro strukturu grafenu.],
) <fig:baze-grafen>

Délka jedné hrany je 1.42 Ångstromů, položme tedy
#math.equation(numbering: none, block: true)[
  $#clb[$vc(u)$] = vec(1.42, 0)$
]
a spočítejme, čemu se musí rovnat #clr[$vc(v)$]. Protože vnitřní úhel
pravidelného hexagonu má velikost $120 degree$, vektor #clr[$vc(v)$] svírá s
vektorem #clb[$vc(u)$] úhel $180 degree - 120 degree = 60 degree$. Zároveň,
velikost vektoru #clr[$vc(v)$] musí být rovna velikosti vektoru #clb[$vc(v)$],
tj. číslu $1.42$.

Podle @def:uhel-mezi-vektory[definice] musí platit
#math.equation(numbering: none, block: true)[
  $cos 60 degree = (#clb[$vc(u)$] dot.c #clr[$vc(v)$]) / (||#clb[$vc(u)$]||
  ||#clr[$vc(v)$]||) = (1.42 #clr[$v_1$]) / 1.42^2 = #clr[$v_1$] / 1.42$,
]
z čehož
#math.equation(numbering: none, block: true)[
  $#clr[$v_1$] = 1.42 dot.c cos 60 degree = 0.71$.
]
Z podmínky velikosti vektoru #clr[$vc(v)$] dopočteme jeho druhou složku, #clr[$v_2$]. Musí platit
#math.equation(numbering: none, block: true)[
  $1.42 = ||#clr[$vc(v)$]|| = sqrt(#clr[$v_1^2$] + #clr[$v_2^2$])$,
]
takže
#math.equation(numbering: none, block: true)[
  $#clr[$v_2$] = sqrt(1.42^2 - #clr[$v_1^2$]) = sqrt(1.42^2 - 0.71^2) = 1.23$.
]
Tím jsme hotovi. Zvolíme-li za soustavu souřadnic dvojici vektorů
#math.equation(numbering: none, block: true)[
  $(vec(1.42, 0), vec(0.71, 1.23))$,
]
pak pozici každého atomu uhlíku ve struktuře grafenu umíme vyjádřit
celočíselnými souřadnicemi. Například, atom uhlíku v pravém horním rohu
@fig:grafen[obrázku] má v naší soustavě souřadnic polohu $(6, 5)$ (je-li levým
dolním rohem bod $(0, 0)$) namísto odporného čísla, které jsem líný
dopočítávat.

=== Volební systémy

V mnoha státech na planetě se používá tzv. "preferenční" volební systém, kde
jeden hlas sestává z uspořádání kandidujících stran od nejvíce preferované po
nejméně preferovanou. Jak si právě ukážeme, takovýto volební systém trpí jistým
paradoxem. Uvažme tři kandidující strany: $A$, $B$ a $C$. Existuje šest různých
způsobů, jak za sebe seřadit tyto tři strany, a tedy i šest různých způsobů
preferenční volby. V @fig:volby[tabulce] je najdete vypsané spolu s víceméně
náhodným rozdělením hlasů.

#figure(
  table(
    columns: (auto, auto),
    inset: 10pt,
    align: horizon + center,
    stroke: (x, y) => if y == 0 { (bottom: 0.7pt + maindark) },
    table.header([*Volba*], [*Počet hlasů*]),
    $A > B > C$, $5$,
    $A > C > B$, $4$,
    $B > A > C$, $2$,
    $B > C > A$, $8$,
    $C > A > B$, $8$,
    $C > B > A$, $2$,
  ),
  caption: [Výsledky preferenčních voleb.],
) <fig:volby>

Zmíněný paradox spočívá v absenci jasného vítěze těchto voleb. Totiž, počet
voličů, kteří preferovali $A$ proti $B$, je $17$ a počet voličů, kteří zase
volili pro $B$ proti $A$ je $12$. To znamená, že soutěžily-li by tyto dvě
strany proti sobě, vyhrála by strana $A$ proti straně $B$ o $5$ hlasů. Podobně,
strana $B$ by vyhrála v soutěži proti $C$ o $1$ hlas. Ovšem, strana $C$ by
_vyhrála_ proti straně $A$ v přímé konfrontaci o $7$ hlasů. Která strana tedy
zvítězila, když $A$ vítězí nad $B$, $B$ vítězí nad $C$ a $C$ vítězí nad $A$?
Jak tušíte, tato otázka nemá jednoznačnou odpověď. Existují různé vesměs
neuspokojivé způsoby, jak tento volební paradox řešit. O ty se zde zajímat
nebudeme. My si pouze rozmyslíme, proč k~němu dochází.

Totiž, volba každého jednoho voliče je dokonale "neparadoxní"; zkrátka uspořádá
strany za sebe podle svých preferencí. A přesto jejich sloučení dá vzniknout
uspořádání $A > B > C > A$, které je zřejmě problematické.

Přeneseme problém do jazyka lineární algebry. Strany si nakreslíme do kruhu a
přidáme mezi ně šipky tímto způsobem:
#align(center)[
  #cetz.canvas(pref_circle($5$, $1$, $7$))
]
Kruh vyjadřuje, že $A$ vede nad $B$ o pět hlasů, $B$ nad $C$ o jeden hlas a $C$
nad $A$ o hlasů sedm. Když by třeba $B$ naopak vedla nad $A$ o $x$ hlasů, pak
by u šipky z $A$ do $B$ bylo číslo $-x$. Tento způsob visualisace nás rovnou
vede k důležité myšlence: stane-li se, že součet hlasů dá kruh se všemi čísly
kladnými nebo všemi zápornými, nutně nastává paradox. První případ odpovídá
uspořádání $A > B > C > A$ a ten druhý uspořádání $C > B > A > C$. Řekneme, že
taková uspořádání jsou _cyklická_.

Ovšem, voliči hlasují zřejmě _acyklicky_. Přeci, uspořádání stran $A > B > C$
si můžeme napsat jako $A > B > C < A$ a vidíme, že k žádnému paradoxu
nedochází. Jeden hlas s takovouto preferencí si můžeme zakreslit kruhem jako
#align(center)[
  #cetz.canvas(pref_circle($1$, $1$, $-1$))
]
protože $A$ vyhrává nad $B$ o jeden hlas, $B$ nad $C$ taky o jeden hlas a $C$
_prohrává_ proti $A$ o jeden hlas. Jak se tedy může stát, že součtem
acyklických uspořádání je uspořádání cyklické. @fig:hlasy-kruhem[Tabulka]
ukazuje zakreslení každé z možných voleb kruhem.

#figure(
  table(
    columns: (auto, auto, auto, auto),
    inset: 10pt,
    align: horizon + center,
    stroke: (x, y) => {
      if y == 0 { (bottom: 0.7pt + maindark) }
      if x == 1 { (right: 0.7pt + maindark) }
    },
    table.header([*Volba*], [*Zakreslení*], [*Volba*], [*Zakreslení*]),
    [$A > B > C$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($1$, $1$, $-1$)
      })
    ],
    [$C > B > A$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($-1$, $-1$, $1$)
      })
    ],

    [$C > A > B$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($1$, $-1$, $1$)
      })
    ],
    [$B > A > C$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($-1$, $1$, $-1$)
      })
    ],

    [$B > C > A$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($-1$, $1$, $1$)
      })
    ],
    [$A > C > B$],
    [
      #cetz.canvas({
        import cetz.draw: scale
        scale(x: 75%, y: 75%)
        pref_circle($1$, $-1$, $-1$)
      })
    ],
  ),
  caption: [Voličské preference zakreslené kruhem.],
)<fig:hlasy-kruhem>

Jak celé tohle souvisí s lineární algebrou? Přímočaře. Každý kruh je vlastně
jenom trojice čísel -- vektor o třech souřadnicích. Například kruh
#math.equation(numbering: none, block: true)[
  $#cetz.canvas(baseline: (0, 0), {
    import cetz.draw: scale
    scale(x: .75, y: .75)
    pref_circle($1$, $1$, $-1$)
  }) "můžeme napsat jako vektor " vec(1, 1, -1)$.
]

Výsledek voleb je pak jenom součtem vektorů jednotlivých hlasů vynásobených
jejich počtem. Pro naši úvodní @fig:volby[tabulku] se jedná o součet
#math.equation(numbering: none, block: true)[
  $5 dot.c vec(1, 1, -1) + 4 dot.c vec(1, -1, -1) + 2 dot.c vec(-1, 1, -1) + 8
  dot.c vec(-1, 1, 1) + 8 dot.c vec(1, -1, 1) + 2 dot.c vec(-1, -1, 1) = vec(5, 1, 7)$.
]

Nyní když uvažujeme o hlasech jako o třídimensionálních vektorech, můžeme si
pro ně zvolit vhodnou _soustavu souřadnic_. Totiž, kartézská soustava souřadnic
je zde jistě zcela nevhodná, neboť _vzdálenosti_ nebo _směry_ hlasů (cokoli
tyto mají znamenat) jsou irelevantními údaji. Při svém zpytování volebních
paradoxů upneme pozornost na _cykličnost_ a _acykličnost_ jednotlivých
uspořádání. Rozdělíme si tedy 3D prostor na dva podprostory -- podprostor
cyklických vektorů a podprostor vektorů acyklických. Ukážeme, že i zdánlivě
acyklické hlasy mají jistou "cyklickou část".

Výše jsme si všimli, že kruh, jehož šipky jsou buď všechny kladné nebo všechny
záporné, představuje "nesmyslné" uspořádání kandidujících stran. Takovým
uspořádáním by odpovídaly hlasy $vec(1, 1, 1)$ a $vec(-1, -1, -1)$, které
pochopitelně v @fig:hlasy-kruhem[tabulce] nenajdeme, neboť nejsou validní. To
však neznamená, že nejsou _teoreticky_ důležité. Totiž, tato dvě uspořádání
stran jsou právě ta _čistě cyklická_, ze kterých nelze získat žádné smysluplné
uspořádání. Dává smysl, že tyto vektory (a jejich násobky) označíme za onu
_cyklickou_ část třídimensionálního prostoru.

Formálněji, označíme
#math.equation(numbering: none, block: true)[
  $C = {vec(r, r, r) | r in R}$
]
množinu všech násobků vektoru $vec(1, 1, 1)$ a vektorům v této množině budeme
říkat _čistě cyklické_. Pro acyklickou část prostoru zvolíme osy tak, aby byly
obě kolmé na vektor $vec(1, 1, 1)$. Tím budeme mít zaručeno, že každý vektor z
této části prostoru opravdu nemá žádnou cyklickou část (podobně jako třeba
vektory ležící na ose $x$ v kartézské soustavě souřadnic míří doprava nebo
doleva ale nikdy nahoru nebo dolu). Protože kolmé vektory svírají $90 degree$ a
$cos 90 degree = 0$, musíme podle @def:uhel-mezi-vektory[definice] volit zbylé
dva vektory tak, aby jejich skalární součin s vektorem $vec(1, 1, 1)$ byl
nulový. To vede na rovnici
#math.equation(numbering: none, block: true)[
  $vc(u) dot.c vec(1, 1, 1) = u_1 + u_2 + u_3 = 0$.
]
Této rovnici zřejmě vyhovuje mnoho vektorů, my si vybereme třeba
#math.equation(numbering: none, block: true)[
  $vec(1, 0, -1) " a " vec(0, 1, -1)$.
]
Jejich volba nemůže být zcela náhodná, ale tím se nyní zdržovat nebudeme.
Dostali jsme soustavu souřadnic
#math.equation(numbering: none, block: true)[
  $(vec(1, 1, 1), vec(1, 0, -1), vec(0, -1, 1))$,
]
kde na první ose leží všechny čistě cyklické vektory a na rovině určené zbylými
dvěma osami vektory čistě acyklické.

Teď konečně můžeme formalisovat ideu, že i validní uspořádání stran mají jistou
cyklickou část. Vezměme třeba uspořádání $A > B > C$ představené vektorem
$vec(1, 1, -1)$. Napíšeme-li si tento vektor ve své nové soustavě souřadnic,
dostaneme
#math.equation(numbering: none, block: true)[
  $vec(1, 1, -1) = #clr[$1/3 dot.c vec(1, 1, 1)$] + 2/3 dot.c vec(1, 0, -1) -
  2/3 dot.c vec(0, -1, 1)$.
]
Cyklickou část vektoru jsme označili #clr[červeně]. Jak vidíme, i vektor
representující výsledně acyklické uspořádání přispívá částečně k výslednému
zacyklení.

Je na čase dovršit úvahu o tom, kdy vlastně k zacyklení dojde. Upřete pohled na
@fig:hlasy-kruhem[tabulku]. Vektory / kruhy representující hlasy jsme rozdělili
do sloupců tak, že v prvním sloupci jsou vektory se dvěma kladnými složkami a v
druhém vektory se dvěma zápornými. Navíc, v každém řádku stojí proti sobě
hlasy, které se při sčítání vzájemně vyruší. Totiž, volí-li například jeden
volič pro uspořádání $A > C > B$, pak jeho hlas neutralizuje volič, který volí
pro $B > C > A$. To je přímo vidět z faktu, že součet odpovídajících vektorů
$vec(1, -1, -1)$ a $vec(-1, 1, 1)$ je vektor $vec(0, 0, 0)$, který výslednému
součtu ničím nepřispívá.

Tvrdíme, že k zacyklení dojde přesně ve chvíli, kdy po vykrácení všech
protichůdných hlasů jsou zůstavší hlasy buď všechny z levého sloupce nebo
všechny ze sloupce pravého. Toto tvrzení si dokážeme.

Předpokládejme tedy, že po vykrácení hlasů zůstaly pouze hlasy z levého sloupce
(argument pro pravý sloupec je totožný). To znamená, že součet všech hlasů je tvaru
#math.equation(numbering: none, block: true)[
  $n_1 dot.c vec(1, 1, -1) + n_2 dot.c vec(1, -1, 1) + n_3 dot.c vec(-1, 1, 1)
  = vec(n_1 + n_2 - n_3, n_1 - n_2 + n_3, -n_1 + n_2 + n_3)$
]
pro nějaká přirozená čísla $n_1, n_2, n_3 in NN$. Víme, že vektor napravo
představuje cyklické uspořádání, když jsou jeho složky všechny kladné nebo
všechny záporné. Ukážeme, že když jsou dvě složky tohoto vektoru kladné, resp.
záporné, pak i ta třetí musí být kladná, resp. záporná. To už nutně znamená, že
mají všechny složky stejné znaménko. Ať jsou tedy třeba první a druhá složka
obě kladné (kdyby byly záporné, tak prostě otočíme všechny nerovnosti, a kdyby
měly opačné znaménko, tak vezmeme jiné dvě složky). To znamená, že
#math.equation(numbering: none, block: true)[
  $
    n_1 + n_2 - n_3 & >= 0, \
    n_1 - n_2 + n_3 & >= 0.
  $
]
Odečtením těchto nerovností dostaneme $2n_2 - 2n_3 >= 0$, takže $n_2 >= n_3$.
