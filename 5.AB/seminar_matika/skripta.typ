#import "template.typ": *
#show: template.with(
  img: "imgs/title.png",
  title: [Skripta k matematickému semináři],
  authors: (
    (
      name: "Adam Klepáč",
      affiliation: "Gymnázium Evolution Jižní Město",
      email: "adam.klepac@gevo.cz",
    ),
  ),
  abstract: [
    Tato skripta jsou určena studentům nepovinného předmaturitního semináře z
    matematiky. Ve *stručné* podobě pokrývají probrané učivo a mají sloužit jako
    zdroj příkladů, obrázků a (většinou formální) shrnutí základních ideí.
  ],
)

= Lineární systémy

Lineární systémy modelují skutečnosti (ve fyzice, ekonomie, informatice, ...),
kdy veličiny na sobě závisejí _přímo úměrně_. Běžným příkladem z fyziky je
závislost dráhy na čase při konstantní rychlosti: jedeme-li rychlostí 50 km/h,
pak ujetá vzdálenost (v km) je vždy přesně 50x větší, než uplynuvší čas (v
hodinách).

Jednoduše řečeno jsou lineární systémy množiny #emph[lineárních rovnic] (tedy
rovnic vyjadřujících ony vztahy přímé úměrnosti mezi veličinami). #emph[Řešením]
lineárního systému pak myslíme množinu všech čísel, která lze (v daném pořadí)
dosadit za proměnné, aby byly všechny rovnice splněny.

== Pár aplikací lineárních systémů

V této úvodní sekci si ukážeme různé aplikace lineárních systémů a nadneseme
několik otázek o povaze jejich množin řešení, jež budeme chtít umět zodpovědět.

=== Vstupy a výstupy průmyslů

Ekonomie je složitý systém vzájemně provázaných průmyslů. Vstupy (řekněme
"materiál nutný na výrobu") jednotlivých průmyslů jsou většinou svázány lineárně
(přímo úměrně) s výstupy (řekněme "výrobky") jiných průmyslů. Je tomu tak pro
to, že daný výrobek má konstantní výrobní náklady -- k výrobě tužky je potřeba
tolik a tolik tuhy, tolik a tolik dřeva atd. Neboli, výroba $t$ tužek vyžaduje
(řekněme) $5t$ gramů tuhy. Dokud by výroba plynula pouze jedním směrem (tedy od
tuhy a dřeva k tužkám), nebyla by teorie lineárních systémů v ekonomii mnoho
užitečná. Situace je však málokdy tak jednoduchá. Ona _vzájemná provázanost_
vzniká v~moment, kdy například dřevní průmysl potřebuje vést různé záznamy o
nákupu a prodeji a tyto bude psát tužkou na papír. Nyní je výstup dřevního
průmyslu vstupem tužkového a tužky jsou zase vstupem dřevního průmyslu.
Spočítat, jak přirozené fluktuace v nabídce a poptávce ovlivní takový systém
není triviální. Podívejme se blíže na jiný (leč zjednodušený) příklad z praxe.

Omezíme se na dva konkrétní hráče na volném trhu -- automobilový průmysl a
průmysl ocelový. Pochopitelně, automobilový průmysl vyžaduje ocel k výrobě
vozidel, a naopak, ocelový průmysl vyžaduje nákladní auta k převozu oceli z
továren ke kupcům. Zároveň, automobilový průmysl používá svá vlastní nákladní
auta například k převozu osobních automobilů a ocelový průmysl též svou vlastní
ocel k výstavbě továren. Konečně, výše výstupu obou průmyslů musí uspokojit
poptávku všech ostatních průmyslů i fyzických osob na trhu.

Situaci shrňme následující tabulkou, kde jsou u obou průmyslů uvedeny hodnoty
výstupů (v milionech dolarů za rok 1958 v USA) využívaných automobilovým
průmyslem, ocelovým průmyslem a pak všemi ostatními.

#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  inset: 10pt,
  align: end,
  table.header(
    [], [*užívá ocel*], [*užívá auto*], [*užívá zbytek*], [*celkem*]
  ),
  table.hline(start: 1, stroke: 0.5pt + maindef),
  table.vline(x: 1, start: 1, stroke: 0.5pt + maindef),
  [*hodnota oceli*], [$5395$], [$2664$], [$17389$], [$25448$],
  [*hodnota auta*], [$48$], [$9030$], [$21268$], [$30346$],
)

Celkem přirozeně, hodnoty v prvních dvou sloupcích zůstanou konstantní, dokud se
nezmění hodnoty ve sloupci třetím. Ani jeden z průmyslů nemá důvod upravovat
nabídku, nezmění-li se poptávka. Ovšem, hodnota v třetím sloupci kolísá s
poptávkou _fyzických osob_, jež je notoricky obtížně předpovídatelná. Chtěli
bychom umět určit hodnotu obou průmyslů v příštím roce na základě dané fluktuace
hodnoty ve třetím sloupci tabulky.

Tomu poslouží lineární systém o těchto dvou rovnicích:
#align(center)[
  $
    "hodnota oceli v příštím roce" & = "užitá ocel ocelí v příštím roce" \
                                   & + "užitá ocel autem v příštím roce" \
                                   & + "užitá ocel ostatními v příštím roce" \
     "hodnota auta v příštím roce" & = "užité auto ocelí v příštím roce" \
                                   & + "užité auto autem v příštím roce" \
                                   & + "užité auto ostatními v příštím roce" \
  $ <eq:economy>
]

Pro jednoduchost vyjádření označíme písmenem $o$ hodnotu oceli v příštím roce a
písmenem $a$ hodnotu auta v příštím roce.

Předpokládejme, že hodnota užité oceli ostatními v příštím roce vzroste na 17589
milionu dolarů a hodnota užitého auta ostatními v příštím roce klesne na 21243.
Budeme též předpokládat, že podíl celkové hodnoty ocelového i automobilového
průmyslu využitý ocelovým průmyslem zůstane nezměněn a stejně tak i pro průmysl
automobilový. Čili, ocelový průmysl použil v tomto roce přesně $5395 slash
25448$ hodnoty svého vlastního výstupu a $2664 slash 30346$ hodnoty výstupu
automobilového průmyslu. Dále, automobilový průmysl použil $9030 slash 30346$
své vlastní hodnoty a $48 slash 25448$ hodnoty oceli.

Dosazením všech hodnot do rovnice @eq:economy dostaneme
#align(center)[
  $
    o & = 5395/25448 o + 2664/30346 a + 17589 \
    a & = 48 / 25448 o + 9030 / 30346 a + 21243
  $
]

Řešením tohoto systému jsou očekávané hodnoty výstupů obou průmyslů při dané
fluktuaci vnější poptávky.

=== Elektrické sítě

Inženýři často potřebují zodpovědět otázky o elektrických sítích (v mobilu, v
autě ...) typu: "Jak silný proud prochází každým obvodem?", "Jak vysoké napětí
nepřetíží připojená zařízení" apod.

Lineární systémy mohou sloužit jako dobrý způsob studia elektrických sítí. Než
se podíváme na konkrétní příklady, shrneme víceméně intuitivním způsobem
základní vlastnosti elektrických sítí.

Jednoduchý elektrická síť sestává ze dvou typů zařízení: _baterií_ a
_resistorů_. Jejich vztah si lze představovat tak, že baterie pumpuje napětí,
dokud existuje v síti aspoň jeden uzavřený obvod a průchod elektrického proudu
resistorem napětí ve zbytku obvodu sníží. Proud jako takový lze považovat za
jakousi "rychlost" pohybu napětí po síti. Když se síť rozdělí do dvou obvodů,
proud se rozdělí též, neboť napětí zůstane v obou obvodech stejné.

Proud, napětí a odpor jsou svázány tzv. Ohmovým zákonem, který říká, že v každém
bodě obvodu platí
#align(center)[
  $"napětí" = "proud" dot "odpor"$.
]
Další ingrediencí ke studiu elektrických obvodů se nám stanou dva Kirchhoffovy
zákony: zákon _napětí_ a zákon _proudění_. Zákon napětí říká, že celkový pokles
napětí v každém obvodu je roven celkovému vzrůstu. Jinak řečeno, po průchodu
všemi resistory v obvodu musí být nulové, neboť jeho vzrůst zařizuje baterie.
Kirchhoffův zákon proudění říká, že v každém bodě, kde se síť dělí na více
obvodů, je součet velikostí proudů konstantní. Rozdělí-li se tedy jeden obvod v
jistém bodě na tři obvody, pak velikost proudu v tomto jednom obvodu musí být
rovna součtu velikostí tří proudů v obvodech následujících.

Nyní předložíme několik příkladů elektrických sítí, od jednoduchých po poněkud
komplikovanější.

Jistě nejjednodušším příkladem elektrické sítě je ta o pouze jednom obvodu.

#figure(
  zap.circuit({
    import zap: *

    capacitor("c1", (0, 0), (0, 3), label: [$"10 V"$])
    resistor("r1", (0, 3), (4, 3), label: [$"5 "Omega$])
    resistor("r2", (4, 3), (4, 0), label: [$"2 "Omega$])
    resistor("r3", (4, 0), (0, 0), label: [$"3 "Omega$])
  }),
  caption: [Jednoduchá elektrická síť o jednom obvodu.],
)

Baterie v této síti dodává napětí o velikosti 10 V. Zapojeny jsou za sebou tři
resistory o odporech #box([5, 2 a 3 $Omega$]). K výpočtu proudu procházejícího
celým obvodem nebudeme potřebovat Kirchhoffův zákon proudění (protože se síť
nedělí na více obvodů) ani lineární systém. Bude stačit jediná rovnice. Totiž,
podle Kirchhoffova zákona napětí musí celkový nárůst napětí (zde 10 V) být roven
jeho celkovému poklesu. Dohromady musejí tedy ony tři zapojené resistory
"spolknout" 10 V napětí. Protože je celkový odpor obvodu roven $5 + 2 + 3 = 10$
$Omega$ a víme, že platí $"napětí" = "proud" dot "odpor"$, můžeme spočítat, že
proud procházející obvodem je roven 1 A.

Nyní již uvážíme síť o třech obvodech: jednom vnějším (označeném modře), jednom
vnitřním (z baterky přes resistor o 4 $Omega$ a zase do baterky) a jednom bez
baterky (obdélník obsahující oba resistory).

#figure(
  zap.circuit({
    import zap: *

    capacitor("c1", (0, 0), (0, 5), label: [$"12 V"$])
    resistor(
      "r1",
      (6, 4),
      (6, 1),
      label: text(blue)[$"3 "Omega$],
      stroke: blue,
    )
    resistor("r2", (4, 4), (4, 1), label: (
      content: [$"4 "Omega$],
      anchor: "south",
    ))

    wire((4, 4), "r2.west", i: (
      content: $i_2$,
      anchor: "west",
    ))
    wire("c1.east", (0, 5), stroke: blue)
    wire((0, 5), (4, 5), (5, 5), (5, 4), (6, 4), stroke: blue, i: (
      content: $i_0$,
      anchor: "north",
    ))
    wire((6, 4), "r1.west", stroke: blue, i: (
      content: text(blue)[$i_1$],
      anchor: "east",
    ))
    wire("r1.east", (6, 1), stroke: blue)
    wire((5, 4), (4, 4))
    wire((6, 1), (5, 1), (5, 0), (0, 0), stroke: blue, i: (
      content: $i_0$,
      anchor: "north",
    ))
    wire((4, 1), (5, 1))
    wire((0, 0), "c1.west", stroke: blue)

    node("n1", (5, 4), fill: true, label: (content: $N_1$, anchor: "south"))
    node("n2", (5, 1), fill: true, label: (content: $N_2$, anchor: "north"))
  }),
  caption: [Elektrická síť o třech obvodech.],
)

Proud $i_0$ procházející sítí se v uzlu označeném $N_1$ dělí na dva: $i_1$ a
$i_2$. Podle Kirchhoffova zákona o proudění musí platit rovnost $i_0 = i_1 +
i_2$. Podobně, v uzlu $N_2$ se proudy $i_1$ a $i_2$ pojí v jeden: $i_0$. Podle
stejného zákona platí rovněž $i_1 + i_2 = i_0$.

Navíc, pro každý ze tří obvodů platí Kirchhoffův zákon napětí. V případě
vnitřního obvodu (kterým prochází proud o velikosti $i_2$) musí resistor snížit
napětí o celých 12 V. Z pravidla $"napětí" = "proud" dot "odpor"$ dostáváme
rovnici $12 = i_2 dot 4$. Podobně, modrý vnější obvod splňuje rovnici $12 = i_1
dot 3$. Nakonec zde máme obvod bez baterky. Ten má celkové napětí 0 V.
Resistorem nalevo prochází napětí $4 dot i_2$ a resistorem napravo napětí $3 dot
i_1$. Protože však elektřina proudí resistorem napravo _opačným směrem_ oproti
resistoru napravo, musíme tento fakt vykompensovat změnou znaménka. Celkový
pokles napětí v tomto obvodu je pročež #box($4 dot i_2 - 3 dot i_1$). Ten musí být
nulový, čili $4 dot i_2 - 3 dot i_1 = 0$.

Po využití obou Kirchhoffových zákonů docházíme k závěru, že proud procházející
sítí je popsán soustavou rovnic
#align(center)[
  $
            i_0 & = i_1 + i_2 \
      i_1 + i_2 & = i_0 \
           4i_2 & = 12 \
           3i_1 & = 12 \
    4i_2 - 3i_1 & = 0.
  $
]
Jak si můžete všimnout, jisté rovnice jsou tu zbytečné, třeba druhá a pátá. Na
tom by nám nemuselo záležet, dostaneme-li správný výsledek tak či tak, ale z
výpočetního hlediska je tato situace neoptimální. Totiž, v~praxi počítáme
obvykle systémy o tisících ba statisících lineárních rovnicích a zcela jistě
není vhodné nechat počítač řešit například pět tisíc rovnic, mohl-li řešit pouze
tisíc. Které rovnice jsou však zbytečné a které ne není triviální bez bližšího
studia určit. Například aspoň jednu z prvních dvou rovnic ponechat musíme, neboť
bez nich nespočítáme proud $i_0$. Dále, z posledních tří rovnic si rovněž musíme
libovolné dvě ponechat a tu třetí můžeme zanedbat. Jak problém "Které rovnice v
soustavě jsou zbytečné?" řešit zodpovíme brzy.

Řešením systému je $i_0 = 7, i_1 = 4, i_2 = 3$.

Posledním obvodem, který si ukážeme a jejž by bylo opravdu obtížné řešit bez
teorie soustav lineárních rovnic, je tzv. _Wheatstonův most_ na
#ref(<wheatstone-bridge>, supplement: "obrázku").

#figure(
  zap.circuit({
    import zap: *

    capacitor("c1", (0, 0), (0, 5), label: [$"10 V"$])
    resistor("r1", (5, 4), (4, 3), label: (
      content: [$"5 "Omega$],
      anchor: "south",
      distance: 2pt,
    ))
    resistor("r2", (6, 4), (7, 3), label: (
      content: [$"2 "Omega$],
      anchor: "north",
      distance: 2pt,
    ))
    resistor("r5", (4, 2.5), (7, 2.5), label: (
      content: [$"50 "Omega$],
      anchor: "north",
      distance: 4pt,
    ))
    resistor("r3", (4, 2), (5, 1), label: (
      content: [$"10 "Omega$],
      anchor: "south",
      distance: 2pt,
    ))
    resistor("r4", (7, 2), (6, 1), label: (
      content: [$"4 "Omega$],
      anchor: "north",
      distance: 2pt,
    ))

    wire((0, 5), (5.5, 5), (5.5, 4.5), (5, 4), i: (
      content: [$i_0$],
      anchor: "north",
    ))
    wire((5.5, 4.5), (6, 4), i: (
      content: [$i_2$],
      anchor: "north-east",
      distance: 4pt,
    ))

    wire((5, 1), (5.5, 0.5), i: (
      content: [$i_3$],
      anchor: "south-west",
      distance: 3pt,
    ))
    wire((5, 1), (5.5, 0.5), (5.5, 0), (0, 0), i: (
      content: [$i_0$],
      anchor: "south",
    ))
    wire((6, 1), (5.5, 0.5), i: (
      content: [$i_4$],
      anchor: "south-east",
      distance: 3pt,
    ))

    wire((5.5, 4.5), (5, 4), i: (
      content: [$i_1$],
      anchor: "north-west",
      distance: 3pt,
    ))
    wire((4, 3), (3.5, 2.5))
    wire((3.5, 2.5), (5, 2.5), i: (
      content: [$i_5$],
      anchor: "north-east",
      distance: 3pt,
    ))
    wire((7, 3), (7.5, 2.5))
    wire((6, 2.5), (7.5, 2.5), i: (
      content: [$i_5$],
      anchor: "north-west",
      distance: 3pt,
    ))
    wire((3.5, 2.5), (4, 2))
    wire((7.5, 2.5), (7, 2))

    node("n1", (5.5, 4.5), fill: true)
    node("n2", (5.5, 0.5), fill: true)
    node("n3", (3.5, 2.5), fill: true)
    node("n4", (7.5, 2.5), fill: true)
  }),
  caption: [Wheatstonův most.],
) <wheatstone-bridge>

Tato síť obsahuje čtyři uzly a bezpočet obvodů. Protože neznámých velikostí
proudu je šest, potřebujeme najít minimálně šest různých rovnic, ve kterých se
každá z proměnných vyskytuje celkem aspoň jednou. Aplikace Kirchhoffova zákona
na horní a spodní uzel dá rovnice
#align(center)[
  $display(
    i_0 &= i_1 + i_2\
    i_3 + i_4 &= i_0.
  )$
]
Z levého a pravého uzlu pak získáme rovnice (nesmíme zapomenout změnit znaménko,
když počítáme s velikostí proudu v "opačném" směru oproti nakreslenému)
#align(center)[
  $display(
    i_1 - i_5 &= i_3\
    i_2 + i_5 &= i_4.
  )$
]
Dále, Kirchhoffův zákon napětí použitý na vnitřní obvod s baterií dává rovnici
#align(center)[
  $display(10 = 5i_1 + 10i_3)$.
]
Naopak, z vnějšího obvodu s baterií usoudíme, že
#align(center)[
  $display(10 = 2i_2 + 4i_4)$.
]
Konečně musíme najít obvod, který nám umožní spočítat hodnotu proměnné $i_5$.
Tím je například onen "horní trojúhelník". Z něj dostaneme rovnici
#align(center)[
  $display(5i_1 + 50i_5 - 2i_2 = 0)$.
]

Celkem tedy řešíme soustavu rovnic o sedmi rovnicích a šesti neznámých:
#align(center)[
  $display(
    i_0 & = i_1 + i_2\
    i_3 + i_4 & = i_0\
    i_1 - i_5 & = i_3\
    i_2 + i_5 & = i_4\
    10 & = 5i_1 + 10i_3\
    10 & = 2i_2 + 4i_4\
    0 & = 5i_1 + 50i_5 - 2i_2,
  )$
]
jejímž řešením je $i_0 = 7 slash 3, i_1 = 2 slash 3, i_2 = 5 slash 3, i_3 = 2
slash 3, i_4 = 5 slash 3$ a $i_5 = 0$.

Wheatstonův most se často používá k měření odporu různých zařízení ve smyslu,
který si dostanete šanci rozmyslet prostřednictvím cvičení na konci kapitoly.

=== Chemické rovnice

Lineární systémy se objevují též v chemii, konkrétně při vyčíslování reakcí.
Uvažme reakci, kdy se toluen #math.mono($C_7 H_8$) slučuje s kyselinou dusičnou
#math.mono($H N O_3$) a produkuje trinitrotoluen #math.mono($C_7 H_5 O_6 N_3$) s
vodou #math.mono($H_2 O$). Počet molekul na obou stranách reakce označíme
postupně písmeny $x,y,z,w$. Pak můžeme reakci zapsat jako
#align(center)[
  $x" "mono(C_7 H_8) + y" "mono(H N O_3) arrow z" "mono(C_7 H_5 O_6 N_3) + w"
 "mono(H_2 O)$.
]
Aby taková reakce mohla nastat, musí díky zákonu zachování hmoty být počet atomů
na levé straně být roven počtu atomů na straně pravé. Jelikož v reakci vystupují
čtyři různé atomy, dostáváme systém o čtyřech rovnicích:
#align(center)[
  $display(
    mono(C): & & 7x &= 7z\
    mono(H): & 8x &+ y &= 5z &+& 2w\
    mono(N): & & y &= 3z \
    mono(O): & & 3y &= 6z & + & w
  )$
]
Všimněte si, že takový systém rovnic má *nekonečně mnoho* řešení, protože obě
strany chemické reakce závisejí na úvodním množství (aspoň jedné ze) sloučenin.
Aby měl systém se čtyřmi proměnnými přesně jedno řešení, musí obsahovat
minimálně čtyři lineární rovnice, ale -- jak vidno -- nemusí to vždy stačit.

=== Interpolace

Důležitou úlohou statistiky je schopnost aproximovat diskrétní data souvislou
křivkou dané "výpočetní složitosti". Diskrétními daty se myslí zkrátka množina
měření jisté veličiny nebo veličin v čase. Uvažme příklad hodnoty akcií firmy
NVIDIA za poslední měsíc. Měření této hodnoty každý týden v pondělní poledne dá
graf na #ref(<graf-nvidia>, supplement: "obrázku").

#let data = (
  (1, 171.65),
  (2, 168.245),
  (3, 175.65),
  (4, 179.845),
  (5, 181.85),
)
#figure(
  cetz.canvas({
    import cetz.draw: *

    line((-0.5, 0), (7, 0), mark: (end: "stealth"))
    content((7, -0.2), [týden], anchor: "north-east")
    line((0, -0.5), (0, 3), mark: (end: "stealth"))
    content((-0.2, 2.8), [hodnota akcie (v \$)], anchor: "mid-east")

    for (x, y) in data {
      let y = (y - 130) / 100 * 3

      circle((x, y), radius: 0.1, fill: purple, stroke: none)
    }
    content((1, -0.2), [1], anchor: "north")
    content((2, -0.2), [2], anchor: "north")
    content((3, -0.2), [3], anchor: "north")
    content((4, -0.2), [4], anchor: "north")
    content((5, -0.2), [5], anchor: "north")

    content((-0.2, 1.5), [180], anchor: "east")
    content((-0.2, 0.9), [160], anchor: "east")
    line((0, 1.5), (5.5, 1.5), stroke: (
      thickness: .5pt,
      dash: "dashed",
      paint: mainlight,
    ))
    line((0, 0.9), (5.5, 0.9), stroke: (
      thickness: .5pt,
      dash: "dashed",
      paint: mainlight,
    ))
  }),
  caption: [Graf hodnot akcií firmy NVIDIA za měsíc září 2026.],
) <graf-nvidia>

Jakožto finančních analytiků je naší úlohou na základě dosavadních dat zkusit
odhadnout vývoj hodnoty akcií firma NVIDIA v budoucích týdnech. Tomuto
"doplnění" daných dat o chybějící údaje (ať už mezi jednotlivými týdny nebo v
týdnech budoucích) se říká _interpolace_. Nejjednodušší (ale zato nejrychlejší)
způsob interpolace je proložení daných dat přímkou (tzv. _line of best-fit_).
Taková úloha vede přirozeně na řešení soustavy lineárních rovnic.

Totiž, přímka v rovině je dána lineární rovnicí $y = a x + b$. My máme k
dispozici pět dvojic čísel $(x, y)$ -- $x$ je číslo týdne, $y$ je hodnota akcie
-- a chceme z nich určit koeficienty $a, b$. Zapsány do tabulky, jsou hodnoty
akcií v jednotlivých týdnech následující:

#figure(
  table(
    columns: (60pt, 100pt),
    inset: 10pt,
    align: horizon,
    table.header([*týden*], [*hodnota akcie*]),
    table.hline(stroke: 0.5pt + maindef),
    table.vline(x: 1, stroke: 0.5pt + maindef),
    [$1$], [$171.65$],
    [$2$], [$168.245$],
    [$3$], [$175.65$],
    [$4$], [$179.845$],
    [$5$], [$181.85$],
  ),
  caption: [Hodnoty akcií firmy NVIDIA za měsíc září 2026.],
)

Rovnici přímky pak najdeme vyřešením soustavy rovnic
#align(center)[
  $display(
    171.65 &= a dot 1 + b\
    168.245 &= a dot 2 + b\
    175.65 &= a dot 3 + b\
    179.845 &= a dot 4 + b\
    181.85 &= a dot 5 + b.
  )$
]
Všimněte si na této soustavě jedné zásadní věci -- ona řešení ale vůbec nemá!
Totiž, z prvních dvou rovnic můžeme zjistit, že $a = -3.41$ a $b = 175$
(přibližně), avšak tato dvojice neřeší například rovnici třetí. Co s tím?
Jestliže všech pět bodů na přímce neleží, uměli bychom najít nějakou přímku,
která je jim všem "co nejblíže", ve smyslu, že součet vzdáleností všech bodů od
této přímky je nejmenší možný? Jak snad správně čekáte, odpověď na tuto otázku
je "ano". Jak přesně se takové řešení soustavy dá najít se však dozvíme až
později. Výsledkem příslušného výpočtu by byla přímka $y = 3.2x + 166$ na
#ref(<graf-nvidia-best-fit>, supplement: "obrázku").

#figure(
  cetz.canvas({
    import cetz.draw: *

    line((-0.5, 0), (7, 0), mark: (end: "stealth"))
    content((7, -0.2), [týden], anchor: "north-east")
    line((0, -0.5), (0, 3), mark: (end: "stealth"))
    content((-0.2, 2.8), [hodnota akcie (v \$)], anchor: "mid-east")

    for (x, y) in data {
      let y = (y - 130) / 100 * 3

      circle((x, y), radius: 0.1, fill: purple, stroke: none)
    }
    content((1, -0.2), [1], anchor: "north")
    content((2, -0.2), [2], anchor: "north")
    content((3, -0.2), [3], anchor: "north")
    content((4, -0.2), [4], anchor: "north")
    content((5, -0.2), [5], anchor: "north")

    content((-0.2, 1.5), [180], anchor: "east")
    content((-0.2, 0.9), [160], anchor: "east")

    line((0, 1.075), (6, 1.65144), stroke: (
      thickness: 1pt,
      paint: green,
    ))
  }),
  caption: [Aproximace hodnot akcií firmy NVIDIA přímkou.],
) <graf-nvidia-best-fit>
