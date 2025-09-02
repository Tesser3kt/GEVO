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
kdy veličiny na sobě závisejí #emph[přímo úměrně]. Běžným příkladem z fyziky je
závislost dráhy na čase při konstantní rychlosti: jedeme-li rychlostí 50 km/h,
pak ujetá vzdálenost (v km) je vždy přesně 50x větší, než uplynuvší čas (v
hodinách).

Jednoduše řečeno jsou lineární systémy množiny #emph[lineárních rovnic] (tedy
rovnic vyjadřujících ony vztahy přímé úměrnosti mezi veličinami). #emph[Řešením]
lineárního systému pak myslíme množinu všech možných čísel, která lze (v daném
pořadí) dosadit za proměnné, aby byly všechny rovnice splněny.

V následující úvodní sekci si ukážeme
