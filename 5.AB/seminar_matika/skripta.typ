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

    capacitor("c1", (0, 0), (0, 4), label: "Baterie")
  })
)
