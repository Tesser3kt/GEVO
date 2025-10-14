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
] <linearni-kombinace>

#definition("Lineární rovnice")[
  Jsou-li $x_1, ..., x_n$ proměnné a $a_1, ..., a_n, b$ čísla, pak rovnost
  #align(center)[
    $display(a_1 x_1 + a_2 x_2 + ... + a_n x_n = b,)$
  ]
  kde levá strana je #link(<linearni-kombinace>, "lineární kombinace")
  proměnných $x_1, ..., x_n$.
] <linearni-rovnice>

