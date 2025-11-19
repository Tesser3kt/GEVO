#import "../template.typ": *

= Matematická indukce
<chap:matematicka-indukce>

Matematická indukce je důkazová technika použitelná na jakákoli tvrzení
související s přirozenými čísly (zkrátka jakákoli tvrzení, kde máme nějaký
"počet" věcí). Řekněme, že dokazujeme nějaké tvrzení $T$. Jsou-li splněny
následující dvě podmínky:
#list[
  $T$ platí pro nějaké "nejmenší" přirozené číslo $n_0 in NN$;
][
  platí-li $T$ pro $n > n_0$, pak platí též pro $n + 1$,
]
pak tvrzení $T$ platí pro všechna přirozená čísla.

Jeho princip je v zásadě přímočarý. Totiž, předpokládejme, že tyto dvě podmínky
platí. Víme, že $T$ platí pro $n_0$. Ovšem, z druhé podmínky plyne, že když
platí $T$ pro $n_0$, pak platí taky pro $n_0 + 1$. Ale, když $T$ platí pro $n_0
+ 1$, pak platí taky pro $n_0 + 2$ (opět z druhé podmínky). Takto můžeme
pokračovat libovolně dlouho, takže tvrzení $T$ opravdu platí pro každé přirozené
číslo větší než $n_0$.

Jako příklad užití matematické indukce dokážeme jedno tvrzení.
#proposition[
  Pro každé $n in NN, n >= 1$ platí rovnost
  #math.equation(numbering: none, block: true)[
    $1 + 2 + ... + n = n(n+1)/2$.
  ]
]
#proof[
  Nejprve ukážeme, že je tvrzení pravdivé pro $n = 1$. Pak je na levé straně
  zkrátka číslo $1$ a na pravé $1 dot (1 + 1) slash 2 = 1$. Tedy rovnost platí.

  Nyní předpokládejme, že platí rovnost
  #math.equation(numbering: none, block: true)[
    $1 + 2 + ... + n = n(n+1)/2$
  ]
  a dokazujme, že platí též rovnost
  #math.equation(numbering: none, block: true)[
    $1 + 2 + ... + n + (n + 1) = ((n + 1)(n + 2))/2$
  ]
  (tj. tatáž rovnost pro číslo $n + 1$). Nuže, na pravé straně máme výraz $1 + 2
  + ... + n$, o kterém předpokládáme, že je roven $n(n + 1) slash 2$. Dosaďme
  tedy za něj, abychom dostali
  #math.equation(numbering: none, block: true)[
    $n(n+1) / 2 + (n + 1) = ((n+1)(n+2))/2$.
  ]
  Stačí rozpočítat obě strany. Na levé straně máme
  #math.equation(numbering: none, block: true)[
    $n(n+1)/2 + (n+1) = (n(n+1) + 2n + 2)/2 = (n^2 + n + 2n + 2)/2 = (n^2 + 3n +
    2)/2$,
  ]
  zatímco na pravé
  #math.equation(numbering: none, block: true)[
    $((n+1)(n+2))/2 = (n^2 + n + 2n + 2)/2 = (n^2 + 3n + 2)/2$,
  ]
  takže se obě strany rovnají a máme dokázáno.
]
