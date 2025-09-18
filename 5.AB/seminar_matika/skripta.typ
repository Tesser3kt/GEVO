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

