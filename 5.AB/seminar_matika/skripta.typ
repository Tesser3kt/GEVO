#import "template.typ": template
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

V následující úvodní sekci si ukážeme různé aplikace lineárních systémů a
nadneseme několik otázek o povaze jejich množin řešení, jež budeme chtít umět
zodpovědět.

== Pár aplikací lineárních systémů

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


